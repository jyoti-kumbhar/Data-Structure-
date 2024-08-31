# Huffman Coding tree
import heapq
from collections import defaultdict, Counter
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
def generate_code(node, prefix="", codebook={}):
  if node:
    if node.char is not None:
      codebook[node.char]=prefix
    generate_code(node.left, prefix+"0",codebook)
    generate_code(node.right, prefix+"1",codebook)
  return codebook
def huffman_encoding(data):
    if not data:
        return "", {}
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_code(root)
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook
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
def operations():
  while True:
    print("\nHuffman Coding Tree\n 1.Encode\n 2.Decode\n 3.Exit")
    choice = int(input("Enter your choice(1-3): "))
    if choice == 1:
      data = input("Enter your data: ")
      encoded_data, codebook = huffman_encoding(data)
      print("Encoded data:", encoded_data)
      print("Codebook:", codebook)
    elif choice == 2:
        encoded_data = input("Enter the encoded data (as a string of bits): ")
        codebook = {}
        num_entries = int(input("Enter the number of entries you want to add to the codebook: "))

        for i in range(num_entries):
            key = input("Enter key (character): ")
            value = input("Enter value (binary code): ")
            codebook[key] = value

        print("Codebook after adding user input:", codebook)
        decoded_data = huffman_decoding(encoded_data, codebook)
        print("Decoded data:", decoded_data)
    elif choice == 3:
      print('exiting')
      break
    else:
      print("Enter a valid choice.")
operations()