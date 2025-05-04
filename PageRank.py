from googlesearch import search
import requests
from bs4 import BeautifulSoup
import numpy as np

def get_urls(keyword, num_results=10):
    urls = list(search(keyword, num_results=num_results))
    return urls

def get_links(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            link = a['href']
            if link.startswith('http'):
                links.append(link)
        return links
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return []

def build_adjacency_matrix(urls):
    n = len(urls)
    adjacency_matrix = np.zeros((n, n))
    url_index = {url: i for i, url in enumerate(urls)}
    
    for i, url in enumerate(urls):
        links = get_links(url)
        for link in links:
            if link in url_index:
                j = url_index[link]
                adjacency_matrix[i][j] = 1  # A link from URL i to URL j
    return adjacency_matrix

def page_rank(M, beta=0.85, threshold=1e-10, max_iter=1000):
    n = M.shape[0]
    r = np.ones((n, 1)) / n
    uniform_r = (1 - beta) * r
    
    for i in range(max_iter):
        r_next = beta * np.matmul(M, r) + uniform_r
        diff = np.sum(np.abs(r_next - r))
        if diff < threshold:
            break
        r = r_next
    return r

# keyword = "Artificial Intelligence"
# urls = get_urls(keyword)
# print("URLs:")
# print(urls)

# adj_matrix = build_adjacency_matrix(urls)
# print("\nAdjacency Matrix:")
# print(adj_matrix)

# # Compute PageRank
# ranks = page_rank(adj_matrix)
# print("\nFinal PageRank vector:")
# print(ranks.flatten())

# # Map ranks to URLs
# url_ranks = {urls[i]: ranks[i, 0] for i in range(len(urls))}
# sorted_url_ranks = sorted(url_ranks.items(), key=lambda item: item[1], reverse=True)

# print("\nURLs ranked by PageRank:")
# for url, rank in sorted_url_ranks:
#     print(f"{url}: {rank}")