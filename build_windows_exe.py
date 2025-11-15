"""
Build Windows Executable for Library Management System
Creates a standalone .exe with custom icon

Requirements:
    pip install pyinstaller

Usage:
    1. First run: python create_icon.py
    2. Then run: python build_windows_exe.py

Output:
    dist/LibraryManagementSystem.exe (with custom icon!)
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if all required files and packages exist"""
    print("=" * 60)
    print("Checking Requirements...")
    print("=" * 60)

    issues = []

    # Check PyInstaller
    try:
        import PyInstaller
        print("✓ PyInstaller installed")
    except ImportError:
        print("✗ PyInstaller not found")
        issues.append("pyinstaller")

    # Check for required files
    required_files = [
        'login.py',
        'admin.py',
        'member.py',
        'add_member.py',
        'add_book.py',
        'config.py',
        'library.jpeg'
    ]

    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} missing")
            issues.append(file)

    # Check for icon
    if os.path.exists('library_icon.ico'):
        print("✓ library_icon.ico (custom icon)")
    else:
        print("⚠ library_icon.ico not found (will use default)")
        print("  Run: python create_icon.py to create one")

    return issues

def install_missing_packages(packages):
    """Install missing Python packages"""
    for package in packages:
        if package in ['pyinstaller']:
            print(f"\nInstalling {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✓ {package} installed")
            except:
                print(f"✗ Failed to install {package}")
                return False
    return True

def build_executable():
    """Build Windows executable with PyInstaller"""

    print("\n" + "=" * 60)
    print("Building Windows Executable...")
    print("=" * 60)

    # PyInstaller command
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--name=LibraryManagementSystem",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window
        "--clean",                      # Clean cache
    ]

    # Add custom icon if exists
    if os.path.exists('library_icon.ico'):
        cmd.append("--icon=library_icon.ico")
        print("✓ Using custom icon: library_icon.ico")
    else:
        print("⚠ No custom icon (using default)")

    # Add data files
    data_files = [
        ('library.jpeg', '.'),
        ('config.py', '.'),
        ('admin.py', '.'),
        ('member.py', '.'),
        ('add_member.py', '.'),
        ('add_book.py', '.'),
    ]

    for src, dest in data_files:
        if os.path.exists(src):
            cmd.append(f"--add-data={src}{os.pathsep}{dest}")

    # Main script
    cmd.append("login.py")

    # Print command
    print(f"\nCommand:")
    print(f"  {' '.join(cmd)}\n")

    # Execute
    try:
        subprocess.check_call(cmd)

        print("\n" + "=" * 60)
        print("✓ BUILD SUCCESSFUL!")
        print("=" * 60)

        print("\n📁 Output files:")
        print("  → dist/LibraryManagementSystem.exe")
        print("  → This is your standalone executable!")

        print("\n🚀 To run:")
        print("  1. Copy the .exe to your Windows machine")
        print("  2. Make sure MySQL is installed and running")
        print("  3. Run setup_database_final.py to create database")
        print("  4. Update config.py with your MySQL password")
        print("  5. Double-click LibraryManagementSystem.exe")

        print("\n📦 Distribution:")
        print("  → You can distribute just the .exe file")
        print("  → Users need MySQL installed")
        print("  → Database must be set up first")

        print("\n✨ Features:")
        print("  ✓ Custom library icon")
        print("  ✓ No Python installation required")
        print("  ✓ Single executable file")
        print("  ✓ No console window")

        return True

    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 60)
        print("✗ BUILD FAILED")
        print("=" * 60)
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("  1. Make sure all .py files are present")
        print("  2. Run: python create_icon.py first")
        print("  3. Check for error messages above")
        return False

def main():
    """Main build process"""

    print("\n" + "=" * 60)
    print("Library Management System - Windows Executable Builder")
    print("=" * 60)

    # Check requirements
    issues = check_requirements()

    # Install missing packages
    if 'pyinstaller' in issues:
        print("\n⚠ Missing packages detected")
        response = input("Install missing packages? (y/n): ").strip().lower()
        if response == 'y':
            if not install_missing_packages(['pyinstaller']):
                print("\n✗ Failed to install packages. Exiting.")
                return
        else:
            print("Build cancelled.")
            return

    # Check for critical missing files
    critical_files = [f for f in issues if f.endswith('.py')]
    if critical_files:
        print(f"\n✗ Missing critical files: {critical_files}")
        print("Cannot build without these files.")
        return

    # Confirm build
    print("\n" + "=" * 60)
    print("Ready to build!")
    print("=" * 60)
    print("\nThis will create:")
    print("  → dist/LibraryManagementSystem.exe")
    print("  → with custom library icon (if .ico exists)")
    print("  → standalone executable for Windows")

    response = input("\nContinue with build? (y/n): ").strip().lower()

    if response == 'y':
        success = build_executable()
        if success:
            print("\n✓ Build complete! Check the 'dist' folder.")
        else:
            print("\n✗ Build failed. See errors above.")
    else:
        print("\nBuild cancelled.")

if __name__ == "__main__":
    main()
