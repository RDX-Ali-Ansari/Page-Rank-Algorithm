import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PageRank import get_urls, build_adjacency_matrix, page_rank

def run_program():
    keyword = keyword_entry.get()
    if keyword:
        try:
            urls = get_urls(keyword)
            adj_matrix = build_adjacency_matrix(urls)
            # col_sums = adj_matrix.sum(axis=0)
            # M = adj_matrix
            ranks = page_rank(adj_matrix)
            url_ranks = {urls[i]: ranks[i, 0] for i in range(len(urls))}
            sorted_url_ranks = sorted(url_ranks.items(), key=lambda item: item[1], reverse=True)
            result_text.delete(1.0, tk.END)
            for url, rank in sorted_url_ranks:
                result_text.insert(tk.END, f"{url}: {rank}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "Please enter a keyword")

# Create the main window
root = tk.Tk()
root.title("PageRank Calculator")

# Create and layout widgets
keyword_label = ttk.Label(root, text="Enter Keyword:")
keyword_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
keyword_entry = ttk.Entry(root, width=30)
keyword_entry.grid(row=0, column=1, padx=5, pady=5)
run_button = ttk.Button(root, text="Run", command=run_program)
run_button.grid(row=0, column=2, padx=5, pady=5)

result_label = ttk.Label(root, text="Ranked URLs:")
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="w")
result_text = tk.Text(root, width=80, height=20)
result_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Start the main event loop
root.mainloop()