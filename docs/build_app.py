"""
Build Script for Library Management System
Creates standalone executable with custom icon

Requirements: pip install pyinstaller

Usage: python build_app.py
"""

import os
import subprocess
import sys

def build_executable():
    """Build standalone executable with custom icon"""

    print("=" * 60)
    print("Library Management System - Build Script")
    print("=" * 60)

    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller found")
    except ImportError:
        print("✗ PyInstaller not found")
        print("\nInstalling PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed")

    # Check for icon file
    icon_file = "library_icon.png"
    if not os.path.exists(icon_file):
        print(f"\n⚠ Warning: {icon_file} not found")
        print("Creating a simple icon from library.jpeg...")

        try:
            from PIL import Image
            # Create a smaller icon from library.jpeg
            img = Image.open("library.jpeg")
            img = img.resize((256, 256), Image.Resampling.LANCZOS)
            img.save(icon_file)
            print(f"✓ Created {icon_file}")
        except Exception as e:
            print(f"✗ Could not create icon: {e}")
            print("Continuing without custom icon...")
            icon_file = None
    else:
        print(f"✓ Found {icon_file}")

    # PyInstaller command
    print("\n" + "=" * 60)
    print("Building executable...")
    print("=" * 60)

    cmd = [
        "pyinstaller",
        "--name=LibraryManagementSystem",
        "--onefile",
        "--windowed",  # No console window
        "--add-data=library.jpeg:.",
        "--add-data=config.py:.",
    ]

    # Add icon if available
    if icon_file and os.path.exists(icon_file):
        cmd.append(f"--icon={icon_file}")

    cmd.append("login.py")

    print(f"Command: {' '.join(cmd)}\n")

    try:
        subprocess.check_call(cmd)
        print("\n" + "=" * 60)
        print("✓ Build successful!")
        print("=" * 60)
        print("\nExecutable location:")
        print("  → dist/LibraryManagementSystem (or .exe on Windows)")
        print("\nTo run:")
        print("  → Double-click the executable in the 'dist' folder")
        print("\nNote: Make sure MySQL is running before launching!")
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build failed: {e}")
        return False

    return True

if __name__ == "__main__":
    print("\n⚠ IMPORTANT NOTES:")
    print("1. This creates a standalone executable")
    print("2. MySQL must be installed and running")
    print("3. Database must be set up (run setup_database_final.py first)")
    print("4. config.py must have correct database credentials")
    print("\nContinue? (y/n): ", end="")

    response = input().strip().lower()
    if response == 'y':
        build_executable()
    else:
        print("Build cancelled.")
