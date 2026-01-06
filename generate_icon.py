from PIL import Image, ImageDraw, ImageFont

def create_icon():
    # Source image from project folder
    source_path = "app_icon.png"
    
    if not os.path.exists(source_path):
        print(f"Error: Source image not found at {source_path}")
        return

    try:
        img = Image.open(source_path)
        # Ensure it's RGBA
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        print("Loading generated super-icon...")
        
        # Save as ICO with multiple sizes for best Windows scaling
        img.save("icon.ico", format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
        print("Success! Premium icon.ico generated.")
        
    except Exception as e:
        print(f"Failed to convert icon: {e}")

if __name__ == "__main__":
    import os
    create_icon()
