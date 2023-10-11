import os
import shutil
import argparse
import re

# Define command line arguments
parser = argparse.ArgumentParser(description='Search and copy Progressions.lsx files.')
parser.add_argument('-i', '--input', help='Input directory (rawMods).')
parser.add_argument('-o', '--output', help='Output directory (rawProgressions).')
parser.add_argument('-v', '--verbose', action='store_true', help='Print each successful operation.')

args = parser.parse_args()

# Get directories from environment variables if not provided in command line
rawMods = args.input if args.input else os.getenv('rawMods')
rawProgressions = args.output if args.output else os.getenv('rawProgressions')

# Ensure output directory exists
os.makedirs(rawProgressions, exist_ok=True)

# Walk through the directory
for root, dirs, files in os.walk(rawMods):
    # Skip any directory named "Game"
    dirs[:] = [d for d in dirs if d != "Game"]
    
    # Check if "Progressions.lsx" is in files
    if "Progressions.lsx" in files:
        # Construct the source file path
        src_file = os.path.join(root, "Progressions.lsx")
        
        # Construct the destination file path
        # Extract the folder name that is not "Game" using regex
        folder_name = re.search(r'Public\\(.+?)\\Progressions', root).group(1)
        dest_file = os.path.join(rawProgressions, f"{folder_name}_Progressions.lsx")
        
        # Copy the file
        shutil.copy2(src_file, dest_file)
        
        # Print the operation if verbose flag is set
        if args.verbose:
            print(f"Copied {src_file} to {dest_file}")