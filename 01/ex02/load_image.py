import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def process_and_zoom_image(file_path: str):
    try:
        # 1. Load the image safely
        print(f"Loading image: '{file_path}'...")
        img_pil = Image.open(file_path)
        img = np.asarray(img_pil)
        
        # 2. Extract dimensions and channels safely
        shape = img.shape
        height = shape[0]
        width = shape[1]
        
        # Determine number of channels (3 for RGB, 4 for RGBA, 1 for Grayscale)
        channels = shape[2] if len(shape) == 3 else 1
        
        # 3. Print the required information
        print("\n--- Image Metadata ---")
        print(f"Size in pixels (X-axis / Width) : {width}")
        print(f"Size in pixels (Y-axis / Height): {height}")
        print(f"Number of channels              : {channels}")
        print("\n--- Pixel Content (Numerical Matrix) ---")
        print(img)
        
        # 4. Zooming effect using your Slicing skills!
        # Let's slice the center 50% area of the image to look like a zoom
        start_y, end_y = height // 4, (3 * height) // 4
        start_x, end_x = width // 4, (3 * width) // 4
        
        zoomed_img = img[start_y:end_y, start_x:end_x]
        
        # 5. Display the image with X and Y axis scales visible
        print("\nDisplaying the zoomed image...")
        plt.imshow(zoomed_img)
        
        # Ensure axis scales (ticks) are visible on the image display
        plt.axis('on') 
        plt.title("Zoomed View with Coordinate Scales")
        plt.xlabel("X Axis (Pixels)")
        plt.ylabel("Y Axis (Pixels)")
        plt.show()
        plt.savefig("zoom_img.png")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please verify the file path.", file=sys.stderr)
    except Image.UnidentifiedImageError:
        print(f"Error: '{file_path}' does not seem to be a valid image format.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# === Execution ===
if __name__ == "__main__":
    # The prompt explicitly asks for "animal.jpeg"
    process_and_zoom_image("IMG_0311.jpeg")
