from PIL import Image

def decrypt_image(input_path, output_path, key):
    try:
        # Load the image
        image = Image.open(input_path)
        pixels = image.load()

        # Get image dimensions
        width, height = image.size

        # Decrypt the image
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Subtract key from each pixel component and ensure it stays within [0, 255]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[x, y] = (r, g, b)

        # Save the decrypted image
        image.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with the encrypted image path
decrypt_image("encrypted_image.jpeg", "decrypted_image.jpeg", 50)
