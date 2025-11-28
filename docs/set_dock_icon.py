"""
Set Custom Dock Icon for macOS
This changes the Python rocket icon to a custom library icon

Usage: Import this at the start of your main application
"""

import sys
import os

def set_app_icon(icon_path='library.jpeg'):
    """
    Set custom dock icon on macOS

    Args:
        icon_path: Path to icon image file
    """
    try:
        # Only works on macOS
        if sys.platform == 'darwin':
            # Using AppKit to set dock icon
            try:
                from AppKit import NSApplication, NSImage

                if os.path.exists(icon_path):
                    # Load the image
                    image = NSImage.alloc().initWithContentsOfFile_(icon_path)

                    # Set as application icon
                    NSApplication.sharedApplication().setApplicationIconImage_(image)
                    print(f"✓ Dock icon set to: {icon_path}")
                    return True
                else:
                    print(f"⚠ Icon file not found: {icon_path}")
                    return False

            except ImportError:
                print("⚠ AppKit not available (install: pip install pyobjc)")
                return False
        else:
            # Not macOS, skip
            print("ℹ Custom dock icon only works on macOS")
            return False

    except Exception as e:
        print(f"✗ Error setting icon: {e}")
        return False

if __name__ == "__main__":
    # Test the function
    set_app_icon()
