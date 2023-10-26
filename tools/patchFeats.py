import os
import shutil

class FeatsPatcher:
    def __init__(self, input_dir, output_dir, levels, classes):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.levels = levels
        self.classes = classes

    def patch_feats(self):
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        for level in self.levels:
            for class_name in self.classes:
                # Construct the input and output file paths
                input_file = os.path.join(self.input_dir, f"feats_{level}_{class_name}.txt")
                output_file = os.path.join(self.output_dir, f"patched_feats_{level}_{class_name}.txt")

                # Patch the feats file
                self._patch_file(input_file, output_file)

    def _patch_file(self, input_file, output_file):
        # Perform the desired patching logic here
        # This is just a placeholder, replace it with your actual logic
        shutil.copy2(input_file, output_file)

# Example usage
input_dir = 'input_directory'
output_dir = 'output_directory'
levels = [1, 2, 3]
classes = ['class1', 'class2', 'class3']

feats_patcher = FeatsPatcher(input_dir, output_dir, levels, classes)
feats_patcher.patch_feats()