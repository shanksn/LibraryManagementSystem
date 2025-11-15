"""
Create Windows Icon (.ico) from Image
Converts library.jpeg to library_icon.ico for Windows executable

Requirements: pip install pillow

Usage: python create_icon.py
"""

from PIL import Image
import os

def create_windows_icon(input_image='library.jpeg', output_icon='library_icon.ico'):
    """
    Create .ico file from image for Windows executable

    Args:
        input_image: Source image file
        output_icon: Output .ico file path
    """
    try:
        print("=" * 60)
        print("Creating Windows Icon (.ico)")
        print("=" * 60)

        # Check if input exists
        if not os.path.exists(input_image):
            print(f"✗ Error: {input_image} not found")
            return False

        print(f"✓ Found input image: {input_image}")

        # Open the image
        img = Image.open(input_image)
        print(f"  Original size: {img.size}")

        # Convert to RGBA if needed
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            print("  Converted to RGBA")

        # Create icon with multiple sizes (Windows standard)
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

        print(f"\n✓ Creating icon with sizes: {icon_sizes}")

        # Save as .ico with multiple resolutions
        img.save(output_icon, format='ICO', sizes=icon_sizes)

        print(f"✓ Icon created: {output_icon}")
        print(f"  File size: {os.path.getsize(output_icon)} bytes")

        print("\n" + "=" * 60)
        print("SUCCESS! Icon file created")
        print("=" * 60)
        print(f"\nNext steps:")
        print(f"1. Icon file: {output_icon}")
        print(f"2. Run: python build_windows_exe.py")
        print(f"3. Executable will have your custom icon!")

        return True

    except Exception as e:
        print(f"\n✗ Error creating icon: {e}")
        return False

def create_simple_book_icon(output_icon='library_icon.ico'):
    """
    Create a simple book icon if library.jpeg doesn't exist
    """
    try:
        print("Creating simple book icon...")

        # Create a simple colored square as placeholder
        img = Image.new('RGBA', (256, 256), (41, 128, 185, 255))  # Blue color

        # Save as .ico
        img.save(output_icon, format='ICO', sizes=[(16,16), (32,32), (48,48), (256,256)])

        print(f"✓ Simple icon created: {output_icon}")
        print("  (You can replace this with a better icon later)")

        return True

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    print("\nLibrary Management System - Icon Creator")
    print("This will create a Windows .ico file for your executable\n")

    # Try to create from library.jpeg first
    if os.path.exists('library.jpeg'):
        success = create_windows_icon('library.jpeg', 'library_icon.ico')
    else:
        print("⚠ library.jpeg not found")
        print("Creating a simple placeholder icon instead...\n")
        success = create_simple_book_icon('library_icon.ico')

    if success:
        print("\n✓ Done! You can now build the Windows executable.")
    else:
        print("\n✗ Failed to create icon.")
