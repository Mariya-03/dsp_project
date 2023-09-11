from PIL import Image
import numpy as np

# Function to convert an image to grayscale
def grayscale_image(input_image):
    img = Image.open(input_image).convert('L')
    return img

# Function to embed the secret image into the cover image using LSB insertion
def embed_LSB(secret_image, cover_image):
    secret_data = np.array(secret_image)
    cover_data = np.array(cover_image)
    
    # Ensure the secret image fits into the cover image
    if secret_data.shape != cover_data.shape:
        raise ValueError("Secret image and cover image must have the same dimensions.")

    # Swap LSB and MSB in the secret data
    secret_data = np.right_shift(secret_data, 7)

    # Embed the secret data into the LSB of the cover data
    stego_data = np.bitwise_or(cover_data, secret_data)
    stego_image = Image.fromarray(stego_data)

    return stego_image

# Load the cover image and the grayscale secret image
cover_image = grayscale_image("dsp_project\cover img.jpg")
secret_image = grayscale_image("dsp_project\secret img.jpg")

# Embed the secret image into the cover image
stego_image = embed_LSB(secret_image, cover_image)

# Save the stego image
stego_image.save("dsp_project\stego_image.jpg")
stego_image.show()

print("LSB insertion steganography with MSB/LSB swap complete.")




