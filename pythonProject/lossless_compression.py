import cv2
import numpy as np
import zlib
import lzma
from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter, namedtuple
import heapq

# Huffman Tree Node
class Node(namedtuple("Node", ["value", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(frequencies):
    heap = [Node(value=k, freq=v, left=None, right=None) for k, v in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left, right = heapq.heappop(heap), heapq.heappop(heap)
        parent = Node(value=None, freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, parent)
    return heap[0]

# Generate Huffman Codes
def generate_huffman_codes(tree, prefix="", codebook={}):
    if tree:
        if tree.value is not None:
            codebook[tree.value] = prefix
        generate_huffman_codes(tree.left, prefix + "0", codebook)
        generate_huffman_codes(tree.right, prefix + "1", codebook)
    return codebook

# Huffman Encoding
def huffman_compress(image):
    flat_pixels = image.flatten()
    frequencies = Counter(flat_pixels)
    tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(tree)
    compressed_data = "".join(huffman_codes[pixel] for pixel in flat_pixels)
    return compressed_data, tree

# Huffman Decoding
def huffman_decompress(compressed_data, tree, shape):
    decoded_pixels = []
    node = tree
    for bit in compressed_data:
        node = node.left if bit == "0" else node.right
        if node.value is not None:
            decoded_pixels.append(node.value)
            node = tree
    return np.array(decoded_pixels, dtype=np.uint8).reshape(shape)

# LZW Compression
def lzw_compress(image):
    image_data = image.tobytes()
    compressed_data = lzma.compress(image_data)
    return compressed_data

# LZW Decompression
def lzw_decompress(compressed_data, shape):
    decompressed_data = lzma.decompress(compressed_data)
    return np.frombuffer(decompressed_data, dtype=np.uint8).reshape(shape)

# Load image
image_path = r'C:\Users\Chetan\Downloads\Brain_MRI.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Huffman Compression
huff_compressed, huff_tree = huffman_compress(image)
huff_decompressed = huffman_decompress(huff_compressed, huff_tree, image.shape)

# LZW Compression
lzw_compressed = lzw_compress(image)
lzw_decompressed = lzw_decompress(lzw_compressed, image.shape)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(huff_decompressed, cmap="gray")
plt.title("Huffman Decompressed")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(lzw_decompressed, cmap="gray")
plt.title("LZW Decompressed")
plt.axis("off")

plt.show()
