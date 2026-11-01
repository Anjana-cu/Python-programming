
import numpy as np

# Create an image using a matrix of pixel values
image = np.array([
    [50, 100, 150],
    [60, 110, 160],
    [70, 120, 170]
])

print("Original Image:")
print(image)

# 1. Reshaping the image
reshaped = image.reshape(1, 9)
print("\nReshaped Image:")
print(reshaped)

# 2. Slicing a specific region
sliced = image[0:2, 0:2]
print("\nSliced Image:")
print(sliced)

# 3. Brightness adjustment using broadcasting
bright_image = image + 30
print("\nBrightness Adjusted Image:")
print(bright_image)

# 4. Matrix multiplication for transformation
matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

transformed = np.dot(image, matrix)
print("\nTransformed Image:")
print(transformed)
