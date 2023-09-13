from PIL import Image
import sys

# Input the image filename
input_image_filename = input("Enter the image filename: ")

try:
    # Open the input image
    input_image = Image.open(input_image_filename)

    # Calculate the new dimensions while maintaining the aspect ratio
    original_width, original_height = input_image.size
    target_width, target_height = 600, 280

    # Calculate the scaling factor
    scale = min(target_width / original_width, target_height / original_height)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    # Create a white background image
    background = Image.new('RGB', (target_width, target_height), (255, 255, 255))

    # Calculate the position of the image in the center of the background
    x_offset = (target_width - new_width) // 2
    y_offset = (target_height - new_height) // 2

    # Resize the input image and paste it in the center of the background
    input_image = input_image.resize((new_width, new_height), Image.LANCZOS)
    background.paste(input_image, (x_offset, y_offset))

    # Save the resulting image
    output_image_filename = input_image_filename.replace(".", "_resized.")
    background.save(output_image_filename)

    print(f"Saved as {output_image_filename}")
except Exception as e:
    print(f"An error occurred: {e}")
