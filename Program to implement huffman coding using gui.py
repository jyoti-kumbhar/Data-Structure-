import tkinter as tk
from collections import Counter
import heapq

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = ''.join(codebook[char] for char in data)

    return encoded_data, codebook, root

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            current_code = ""

    return decoded_data

class HuffmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding Tree")
        self.root.configure(bg="lightcoral")
        self.root.state("zoomed")

        self.data_label = tk.Label(root, text="Enter Data:", font=("Arial", 14))
        self.data_label.grid(row=0, column=0, padx=10, pady=10)

        self.data_entry = tk.Entry(root, font=("Arial", 14))
        self.data_entry.grid(row=0, column=1, padx=10, pady=10)

        self.encode_button = tk.Button(root, text="Encode", command=self.encode_data, font=("Arial", 14))
        self.encode_button.grid(row=0, column=2, padx=10, pady=10)

        self.encoded_label = tk.Label(root, text="Encoded Data:", font=("Arial", 14))
        self.encoded_label.grid(row=1, column=0, padx=10, pady=10)

        self.encoded_display = tk.Label(root, text="", font=("Arial", 14), background="lightcoral")
        self.encoded_display.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.decode_button = tk.Button(root, text="Decode", command=self.decode_data, font=("Arial", 14))
        self.decode_button.grid(row=2, column=2, padx=10, pady=10)

        self.decoded_label = tk.Label(root, text="Decoded Data:", font=("Arial", 14))
        self.decoded_label.grid(row=2, column=0, padx=10, pady=10)

        self.decoded_display = tk.Label(root, text="", font=("Arial", 14), background="lightcoral")
        self.decoded_display.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def encode_data(self):
        data = self.data_entry.get()
        encoded_data, codebook, root_node = huffman_encoding(data)
        self.encoded_display.config(text=encoded_data)
        self.canvas.delete("all")
        self.draw_tree(root_node, 400, 20, 200)

    def decode_data(self):
        encoded_data = self.encoded_display.cget("text")
        if encoded_data:
            codebook = generate_codes(build_huffman_tree(Counter(self.data_entry.get())))
            decoded_data = huffman_decoding(encoded_data, codebook)
            self.decoded_display.config(text=decoded_data)

    def draw_tree(self, node, x, y, dx):
        if node.left:
            self.canvas.create_line(x, y, x - dx, y + 60)
            self.draw_tree(node.left, x - dx, y + 60, dx // 2)
        if node.right:
            self.canvas.create_line(x, y, x + dx, y + 60)
            self.draw_tree(node.right, x + dx, y + 60, dx // 2)
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="lightblue")
        self.canvas.create_text(x, y, text=node.char if node.char else '', font=("Arial", 14))

if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanApp(root)
    root.mainloop()
