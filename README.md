# Advanced_Wikipedia-Text-Crawler
It is made for data crawling for model's training that is essential in which data given to algorithm for training the model is to be accurately correct and clean.

# 🌐 Advanced Wikipedia Text Crawler (Async BFS Version)

### High-Performance Python Web Crawler for Clean Text Extraction

---

## 📌 Overview

The **Advanced Wikipedia Text Crawler** is a **high-performance, asynchronous web crawler** built in Python that extracts **clean, structured textual data from Wikipedia pages**.

Unlike basic scrapers, this crawler implements:

* ⚡ **Asynchronous requests (aiohttp)**
* 🔁 **Infinite BFS (Breadth-First Search) crawling**
* 🧹 **Advanced text cleaning & filtering**
* 🧠 **Duplicate detection using hashing**
* 🌍 **Domain-restricted intelligent crawling**

This makes it suitable for **large-scale data collection, NLP pipelines, and research applications**.

---

## 🚀 Key Features

### ⚡ Asynchronous Crawling

* Uses `aiohttp` + `asyncio` for non-blocking requests
* Handles multiple pages efficiently

---

### 🔁 BFS-Based Infinite Crawling

* Uses queue (`deque`) for traversal
* Continuously explores new Wikipedia pages
* Ensures structured crawling flow

---

### 🧹 Advanced Text Cleaning

* Removes:

  * HTML tags
  * URLs
  * Emails
  * Special characters
* Normalizes text to ASCII
* Converts text to lowercase

---

### 🧠 Smart Filtering System

* Removes:

  * Very short text
  * Noise / repeated characters
  * Numeric-heavy content

---

### 🔐 Duplicate Detection

* Uses **MD5 hashing** to avoid duplicate paragraphs

---

### 🌍 Domain Restriction

* Crawls only **Wikipedia domain**
* Skips unwanted links like:

  * `/wiki/File:`
  * `/wiki/Category:`
  * `/wiki/Help:`

---

### 📄 Output Storage

* Saves cleaned text into:

```id="outputfile"
wikipedia_text_only.txt
```

---

## 🏗️ Project Structure

```id="crawlerstructure"
AdvancedWikipediaTextCrawler.py   # Main script
wikipedia_text_only.txt           # Output file (generated)
```

---

## 🖥️ Tech Stack

### 🐍 Core Language

* Python

### ⚙️ Libraries Used

* `aiohttp` → Async HTTP requests
* `asyncio` → Event loop management
* `BeautifulSoup` → HTML parsing
* `re` → Regex-based cleaning
* `unicodedata` → Text normalization
* `hashlib` → Duplicate detection
* `nltk` → NLP support (tokenization ready)

---

## ⚙️ Configuration

```python id="configblock"
START_URL = "https://en.wikipedia.org/wiki/Argo_(oceanography)"
RATE_LIMIT_DELAY = 0.5
OUTPUT_FILE = "wikipedia_text_only.txt"
```

### 🔧 Customizable:

* Starting page
* Crawl speed (rate limit)
* Output file name

---

## 🔄 Working Pipeline

```id="pipelineflow"
1. Start from initial Wikipedia URL
2. Normalize and validate URL
3. Fetch page asynchronously
4. Extract visible paragraph text
5. Clean and filter text
6. Hash text to remove duplicates
7. Save valid text to file
8. Extract internal Wikipedia links
9. Add new links to BFS queue
10. Repeat infinitely
```

---

## 📜 Core Components Explained

### 📌 `fetch()`

* Async HTTP request handler
* Retry mechanism (3 attempts)
* Handles timeouts and failures

---

### 📌 `extract_visible_text()`

* Removes unwanted HTML elements
* Extracts `<p>` tag content
* Converts text to clean ASCII format

---

### 📌 `extract_links()`

* Extracts internal Wikipedia links
* Filters irrelevant pages
* Normalizes URLs

---

### 📌 `clean_text()`

* Removes noise using regex
* Ensures readable output

---

### 📌 `is_useful()`

Filters text based on:

* Length
* Word count
* Numeric ratio
* Noise patterns

---

### 📌 `crawl_infinite()`

* Core engine of crawler
* BFS traversal using queue
* Handles:

  * URL tracking
  * Text deduplication
  * Continuous crawling

---

## ⚡ How to Run

### 1️⃣ Install Dependencies

```bash id="installcrawler"
pip install aiohttp beautifulsoup4 nltk nest_asyncio
```

---

### 2️⃣ Run Script

```bash id="runcrawler"
python AdvancedWikipediaTextCrawler.py
```

---

### 3️⃣ Output

* Extracted text will be saved in:

```
wikipedia_text_only.txt
```

---

## 📊 Use Cases

* 🧠 NLP dataset creation
* 📚 Knowledge base generation
* 🤖 Chatbot training data
* 📄 Text mining projects
* 🔍 Research and analysis

---

## 🌟 Highlights

✔ Asynchronous high-speed crawler
✔ Infinite BFS traversal
✔ Advanced text cleaning pipeline
✔ Duplicate-free dataset generation
✔ Scalable & production-ready logic

---

## ⚠️ Important Notes

* Designed for **educational and research use**
* Always respect **Wikipedia’s usage policies**
* Use rate limiting responsibly

---

## 🧩 Future Enhancements

* 📂 Save structured JSON output
* 🧠 Integrate NLP pipelines (spaCy, transformers)
* ⚡ Multi-threaded + async hybrid
* 🌐 Add GUI or API interface
* 📊 Add crawl depth control

---

## 👨‍💻 Author

**Vaibhav Sharma**

* Python Developer | Data & AI Enthusiast
* Specialized in Web Scraping & Automation

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Final Note

This project goes beyond basic scraping and demonstrates how to build a **scalable, intelligent crawler system** using modern Python techniques.

A powerful addition to any **Data Science / Backend / AI portfolio 🚀**

---
