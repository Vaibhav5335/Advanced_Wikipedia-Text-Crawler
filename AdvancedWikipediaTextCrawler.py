# ---------------- Install Required Packages ----------------
!pip install aiohttp beautifulsoup4 nltk nest_asyncio

# ---------------- Imports ----------------
import asyncio
import nest_asyncio
nest_asyncio.apply()

import aiohttp
import logging
import random
import re
import unicodedata
import urllib.parse
import hashlib
from collections import deque
from bs4 import BeautifulSoup
import nltk

# ---------------- Configuration ----------------
START_URL = "https://en.wikipedia.org/wiki/Argo_(oceanography)"
RATE_LIMIT_DELAY = 0.5
OUTPUT_FILE = "wikipedia_text_only.txt"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
]

ALLOWED_CHAR_REGEX = r"[^A-Za-z0-9\s\.,;:!\?'\"()\-_]"

# ---------------- Logging & NLTK ----------------
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
nltk.download("punkt")  # For optional sentence tokenization if needed

# ---------------- Helper Functions ----------------
def clean_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(ALLOWED_CHAR_REGEX, " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

def is_useful(text: str) -> bool:
    if not text or len(text) < 20 or len(text.split()) < 5:
        return False
    if sum(c.isdigit() for c in text) > len(text) * 0.3:
        return False
    if re.fullmatch(r"(.)\1{3,}", text):
        return False
    return True

def hash_text(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    scheme = (parsed.scheme or "https").lower()
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return urllib.parse.urlunsplit((scheme, netloc, path, "", ""))

def is_same_domain(url: str) -> bool:
    return urllib.parse.urlsplit(url).netloc.lower().endswith("wikipedia.org")

def should_skip_link(href: str) -> bool:
    if not href or not href.startswith("/wiki/"):
        return True
    if any(href.startswith(f"/wiki/{prefix}:") for prefix in ["File", "Template", "Portal", "Help", "Talk", "Category", "Special"]):
        return True
    return False

def extract_visible_text(html: str):
    """Extract cleaned paragraphs from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "iframe", "svg", "nav", "footer", "header"]):
        tag.decompose()
    for tag in soup.find_all(attrs={"aria-hidden": "true"}):
        tag.decompose()
    
    paragraphs = [p.get_text(separator=" ").strip() for p in soup.find_all("p") if p.get_text(strip=True)]
    ascii_paragraphs = []
    for para in paragraphs:
        cleaned = unicodedata.normalize("NFKD", para).encode("ascii", "ignore").decode("ascii")
        cleaned = re.sub(ALLOWED_CHAR_REGEX, "", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        if cleaned:
            ascii_paragraphs.append(cleaned.lower())
    return ascii_paragraphs

def extract_links(html: str):
    """Extract internal Wikipedia links for BFS traversal."""
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if should_skip_link(href):
            continue
        absolute_url = urllib.parse.urljoin("https://en.wikipedia.org", href)
        links.add(normalize_url(absolute_url))
    return links

# ---------------- Async Fetch ----------------
async def fetch(session, url):
    headers = {"User-Agent": random.choice(USER_AGENTS),
               "Accept": "text/html,application/xhtml+xml"}
    for attempt in range(3):
        try:
            async with session.get(url, headers=headers, timeout=15) as response:
                if "text/html" not in response.headers.get("Content-Type", ""):
                    return response.status, ""
                return response.status, await response.text()
        except Exception as e:
            logging.warning(f"Attempt {attempt+1}: Failed to fetch {url} - {e}")
            await asyncio.sleep(2 ** attempt)
    return 0, ""

# ---------------- Infinite BFS Crawl ----------------
async def crawl_infinite(start_url: str):
    visited_urls = set()
    seen_texts = set()
    queue = deque([normalize_url(start_url)])

    async with aiohttp.ClientSession() as session:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as out_file:
            while queue:
                current_url = queue.popleft()
                if current_url in visited_urls or not is_same_domain(current_url):
                    continue

                logging.info(f"Crawling: {current_url}")
                status, html = await fetch(session, current_url)
                if status != 200 or not html:
                    logging.warning(f"Failed to retrieve {current_url}")
                    continue

                visited_urls.add(current_url)

                # Extract and save text only
                paragraphs = extract_visible_text(html)
                for para in paragraphs:
                    if is_useful(para):
                        h = hash_text(para)
                        if h not in seen_texts:
                            seen_texts.add(h)
                            out_file.write(f"{para}\n")

                # Enqueue new links for BFS traversal
                links = extract_links(html)
                for link in links:
                    if link not in visited_urls:
                        queue.append(link)

                await asyncio.sleep(RATE_LIMIT_DELAY)

    logging.info(f"Crawling complete. All text saved to {OUTPUT_FILE}")

# ---------------- Run ----------------
asyncio.get_event_loop().run_until_complete(
    crawl_infinite(START_URL)
)
