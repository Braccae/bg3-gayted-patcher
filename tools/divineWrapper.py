import os
import subprocess

class DivineWrapper:
    def __init__(self):
        self.divineTool = os.getenv('divineTool', 'path_to_divine.exe')

    def extract_package(self, source_file, target_dir):
        """
        Extracts a .pak file to a target directory.
        """
        command = [self.divineTool, '-a', 'extract-package', '-g', 'bg3', '-s', source_file, '-d', target_dir]
        subprocess.run(command, check=True)

    def create_package(self, source_dir, target_file):
        """
        Creates a .pak file from a source directory.
        """
        command = [self.divineTool, '-a', 'create-package', '-g', 'bg3', '-s', source_dir, '-d', target_file]
        subprocess.run(command, check=True)

    def extract_packages(self, source_dir, target_dir):
        """
        Extracts multiple .pak files from a source directory to a target directory.
        """
        command = [self.divineTool, '-a', 'extract-packages', '-g', 'bg3', '-s', source_dir, '-d', target_dir]
        subprocess.run(command, check=True)