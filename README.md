# 🔍 PageRank Calculator with GUI

A Python project that implements a basic **PageRank algorithm** using web scraping and a graphical user interface (GUI) built with **Tkinter**. Enter a keyword, fetch top search results, build a link graph, and view PageRank-based URL rankings.

---

## 📌 Features

- **Keyword Search**: Fetches top N URLs from Google using `googlesearch`
- **Web Scraping**: Extracts outbound links from each page with `requests` + `BeautifulSoup`
- **Graph Construction**: Builds an adjacency matrix representing the hyperlink structure
- **PageRank Computation**: Uses the power-iteration method with damping factor
- **Tkinter GUI**: Simple interface for inputting keywords and displaying ranked URLs

---

## 🧰 Prerequisites

- Python 3.7+
- Internet connection (for live Google search & scraping)

---

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/PageRankCalculator.git
   cd PageRankCalculator
