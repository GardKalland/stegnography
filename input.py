from PIL import image
import numpy as np

def embed_password_in_image(image_path, output_path, password):
    # Open the image
    image = Image.open(image_path)
    image_data = np.array(image)

    # Convert password to binary
    binary_password = ''.join(format(ord(char), '08b') for char in password)
    binary_password += '1111111111111110'  # Special marker to indicate the end of the password

    # Flatten the image data array
    flat_image_data = image_data.flatten()

    # Embed password into the image data
    for i in range(len(binary_password)):
        flat_image_data[i] = (flat_image_data[i] & ~1) | int(binary_password[i])

    # Reshape the flat array back into the original image shape
    modified_image_data = flat_image_data.reshape(image_data.shape)

    # Save the modified image
    modified_image = Image.fromarray(modified_image_data)
    modified_image.save(output_path)

# Example usage
embed_password_in_image('image.png', 'output_image.png', 'mypassword123')
