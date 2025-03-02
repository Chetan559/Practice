import cv2
import numpy as np
import pywt
import pywt.data
import matplotlib.pyplot as plt

def apply_dwt_compression(image_path, wavelet='haar', level=2, compression_ratio=0.5):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Error loading image. Check the file path.")

    coeffs = pywt.wavedec2(image, wavelet, level=level)
    LL, detail_coeffs = coeffs[0], coeffs[1:]

    
    compressed_coeffs = [LL]  
    for details in detail_coeffs:
        compressed_details = tuple(np.multiply(c, (np.random.rand(*c.shape) > compression_ratio)) for c in details)
        compressed_coeffs.append(compressed_details) 

    compressed_img = pywt.waverec2(compressed_coeffs, wavelet)
    compressed_img = np.clip(compressed_img, 0, 255).astype(np.uint8)

    return image, compressed_img


image_path = r'C:\Users\Chetan\Downloads\Brain_MRI.jpg' 

# Apply DWT compression
original_img, compressed_img = apply_dwt_compression(image_path)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(compressed_img, cmap='gray')
plt.title("Compressed Image (DWT)")
plt.axis("off")

plt.show()
