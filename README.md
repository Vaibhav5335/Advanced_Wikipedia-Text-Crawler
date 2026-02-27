# 🌐 Advanced_Wikipedia-Text-Crawler  
### *A High-Performance Async Web Crawler for Clean Text Extraction*

The **Advanced Wikipedia Text Crawler** is a powerful, asynchronous Python-based web crawler designed to extract **clean, structured, and high-quality textual data** from Wikipedia at scale.

Built with **asyncio and aiohttp**, this crawler goes beyond traditional scraping by implementing **infinite BFS traversal, intelligent filtering, and duplicate detection**, making it ideal for **NLP datasets, AI model training, and research applications**.

---

<p align="center">
  <strong>⚡ WikiCrawler AI</strong><br/>
  <em>Fast • Intelligent • Scalable Data Extraction</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Async-aiohttp%20%7C%20asyncio-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/NLP-Ready-lightgrey?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square"/>
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Workflow](#-workflow)
- [Technology Stack](#-technology-stack)
- [Core Components](#-core-components)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Use Cases](#-use-cases)
- [Future Enhancements](#-future-enhancements)

---

## 🌟 Overview

This project is designed to build a **scalable and intelligent web crawler** capable of extracting **clean textual data from Wikipedia** for use in:

- 🧠 NLP model training  
- 🤖 AI dataset generation  
- 📚 Knowledge base creation  
- 🔍 Research and analysis  

Unlike basic crawlers, it ensures:

- High-speed asynchronous execution  
- Clean and meaningful text extraction  
- Duplicate-free dataset generation  
- Controlled and domain-restricted crawling  

---

## ✨ Key Features

| Feature | Description |
|--------|------------|
| ⚡ **Asynchronous Crawling** | Uses `aiohttp` & `asyncio` for fast, non-blocking requests |
| 🔁 **Infinite BFS Traversal** | Structured crawling using queue-based exploration |
| 🧹 **Advanced Text Cleaning** | Removes HTML, noise, and unwanted symbols |
| 🧠 **Smart Filtering** | Eliminates low-quality and noisy text |
| 🔐 **Duplicate Detection** | Uses MD5 hashing to avoid repeated content |
| 🌍 **Domain Restriction** | Crawls only relevant Wikipedia pages |
| 📄 **Text Output** | Saves clean data into structured text file |

---

## 🏗 Architecture

The crawler follows a **modular async architecture**:

```
URL Queue → Async Fetch → HTML Parsing → Text Cleaning → Filtering → Deduplication → Storage
```

### Components:

1. **Queue System (BFS)** → Manages crawling order  
2. **Async Fetch Layer** → Handles concurrent requests  
3. **Parsing Layer** → Extracts relevant content  
4. **Cleaning Layer** → Removes noise and unwanted data  
5. **Filtering Layer** → Ensures quality  
6. **Storage Layer** → Saves processed data  

---

## 🔄 Workflow

```
1. Start from initial Wikipedia URL
2. Validate and normalize URL
3. Fetch page asynchronously
4. Extract paragraph text
5. Clean and normalize text
6. Filter low-quality content
7. Remove duplicates using hashing
8. Save cleaned text to file
9. Extract internal links
10. Add links to BFS queue
11. Repeat continuously
```

---

## 🛠 Technology Stack

| Component | Technology | Purpose |
|----------|-----------|--------|
| **Language** | Python | Core logic |
| **Async Framework** | asyncio, aiohttp | Concurrent requests |
| **HTML Parsing** | BeautifulSoup | Content extraction |
| **Text Processing** | re, unicodedata | Cleaning & normalization |
| **Hashing** | hashlib | Duplicate detection |
| **NLP Ready** | nltk | Tokenization support |

---

## 📦 Core Components

### 📌 `fetch()`
- Handles async HTTP requests  
- Includes retry mechanism  
- Manages timeouts  

---

### 📌 `extract_visible_text()`
- Extracts `<p>` tag content  
- Removes unwanted HTML elements  
- Converts text to readable format  

---

### 📌 `extract_links()`
- Extracts valid internal Wikipedia links  
- Filters irrelevant pages  
- Normalizes URLs  

---

### 📌 `clean_text()`
- Applies regex-based cleaning  
- Removes noise and unwanted characters  

---

### 📌 `is_useful()`
- Filters text based on:
  - Length  
  - Word count  
  - Noise patterns  
  - Numeric ratio  

---

### 📌 `crawl_infinite()`
- Core engine of crawler  
- BFS traversal using queue  
- Handles:
  - URL tracking  
  - Deduplication  
  - Continuous crawling  

---

## ⚙️ Configuration

```python
START_URL = "https://en.wikipedia.org/wiki/Argo_(oceanography)"
RATE_LIMIT_DELAY = 0.5
OUTPUT_FILE = "wikipedia_text_only.txt"
```

### Customizable Options:
- Starting URL  
- Crawl speed (rate limit)  
- Output file name  

---

## 📁 Project Structure

```
AdvancedWikipediaTextCrawler.py   # Main crawler script
wikipedia_text_only.txt           # Output dataset
```

---

## ⚡ How to Run

### 1️⃣ Install Dependencies
```bash
pip install aiohttp beautifulsoup4 nltk nest_asyncio
```

### 2️⃣ Run Script
```bash
python AdvancedWikipediaTextCrawler.py
```

### 3️⃣ Output File
```
wikipedia_text_only.txt
```

---

## 🎯 Use Cases

- 🧠 NLP dataset creation  
- 🤖 AI model training  
- 📚 Knowledge base generation  
- 🔍 Text mining projects  
- 📄 Research and analysis  

---

## 🌟 Highlights

✔ High-speed asynchronous crawling  
✔ Infinite BFS traversal strategy  
✔ Advanced text cleaning pipeline  
✔ Duplicate-free dataset generation  
✔ Scalable and production-ready design  

---

## ⚠️ Important Notes

- Intended for **educational and research purposes**  
- Respect **Wikipedia scraping policies**  
- Use rate limiting responsibly  

---

## 🔮 Future Enhancements

- 📂 Export structured JSON datasets  
- 🧠 Integrate NLP pipelines (spaCy, transformers)  
- ⚡ Hybrid multi-threaded + async system  
- 🌐 Build API or GUI interface  
- 📊 Add crawl depth control  

---

## 👨‍💻 Author

**Vaibhav Sharma**  
*Python Developer | Data & AI Enthusiast*

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Final Note

> Building intelligent data pipelines is the backbone of modern AI systems.

This project demonstrates how to create a **scalable, efficient, and production-ready web crawler** using modern Python techniques 🚀

---

<p align="center">
  Built with ❤️ using Python & Async Programming<br/>
  <strong>WikiCrawler AI</strong> — Powering Intelligent Data Collection
</p>
