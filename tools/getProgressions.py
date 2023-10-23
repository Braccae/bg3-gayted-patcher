import os
import shutil
import argparse
import re
import sys

class ProgressionsExtractor:
    def __init__(self, rawMods, rawProgressions):
        self.rawMods = rawMods
        self.rawProgressions = rawProgressions
        # Define command line arguments
        self.parser = argparse.ArgumentParser(description='Search and copy Progressions.lsx files.')
        self.parser.add_argument('-v', '--verbose', action='store_true', help='Print each successful operation.')

    def extract_progressions(self):
        # Ensure output directory exists
        os.makedirs(self.rawProgressions, exist_ok=True)

        # Walk through the directory
        for root, dirs, files in os.walk(self.rawMods):
            # Skip any directory named "Game"
            dirs[:] = [d for d in dirs if d != "Game"]
            
            # Check if "Progressions.lsx" is in files
            if "Progressions.lsx" in files:
                # Get the folder name from the root directory
                folder_name = os.path.basename(root)
                
                # Construct the destination file path
                dest_file = os.path.join(self.rawProgressions, f"{folder_name}_Progressions.lsx")
                
                # Copy the file
                shutil.copy2(os.path.join(root, "Progressions.lsx"), dest_file)
                
                # Print the operation if verbose flag is set
                if args.verbose:
                    print(f"Copied {root}/Progressions.lsx to {dest_file}", file=sys.stdout)

# Example usage
rawMods = 'rawmods'
rawProgressions = 'rawprogressions'

#extractor = ProgressionsExtractor(rawMods, rawProgressions)
#extractor.extract_progressions()