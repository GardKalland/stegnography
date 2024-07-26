from PIL import Image
import numpy as np
def extract_password_from_image(image_path):
    # Open the image
    image = Image.open(image_path)
    image_data = np.array(image)

    # Flatten the image data array
    flat_image_data = image_data.flatten()

    # Extract password from image data
    binary_password = ''
    for value in flat_image_data:
        binary_password += str(value & 1)
        if binary_password[-16:] == '1111111111111110':
            break

    # Convert binary password to text
    binary_password = binary_password[:-16]  # Remove the end marker
    password = ''.join(chr(int(binary_password[i:i+8], 2)) for i in range(0, len(binary_password), 8))

    return password

# Example usage
extracted_password = extract_password_from_image('output_image.png')
print(extracted_password)


extract_password_from_image('output_image.png')
