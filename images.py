from PIL import Image
import numpy as np

image_name = 'kilime.jpg'

# Open the image file of me.
kilime = Image.open(image_name)

# Print some key details to check what we're working with.
print(f"Your image '{image_name}' has format: {kilime.format}; size: {kilime.size}; and mode: {kilime.mode}.")

# Convert to a numpy array for simpler manipulation
km_arr = np.array(kilime)
print(f"{image_name} as a numpy array has shape: {km_arr.shape}.")

# # Flatten into a single vector
# np_km = np.reshape(np_km_raw.shape[0], -1).T
# print(np_km.shape)
# print(np.len(np_km))

# GOAL: Find 4 random points in the image, and fill in everything inside with the average value for each R, G, B layer.

pic_height = km_arr.shape[0]
pic_width = km_arr.shape[1]
print(f"Array height is {pic_height} and array width is {pic_width}.")

def random_rectangle(height, width):
    horizontal1 = np.random.randint(0, width)
    horizontal2 = np.random.randint(0, width)
    vertical1 = np.random.randint(0, height)
    vertical2 = np.random.randint(0, height)

    horizontal = np.empty([1,1])
    vertical = np.empty([1,1])

    np.insert(horizontal, 0, horizontal1, axis = 0)
    np.insert(horizontal, 0, horizontal2, axis = 0)
    np.insert(vertical, 0, vertical1, axis = 0)
    np.insert(vertical, 0, vertical2, axis = 0)

    horizontal = np.sort(horizontal)
    vertical = np.sort(vertical)

    return horizontal, vertical

hor, ver = random_rectangle(pic_height, pic_width)

print(hor, ver)
