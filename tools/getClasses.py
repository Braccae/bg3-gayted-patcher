import sys

class ClassFilter:
    def __init__(self, input_file, output_file, filtered_classes, count=False, verbose=False):
        self.input_file = input_file
        self.output_file = output_file
        self.filtered_classes = filtered_classes
        self.count = count
        self.verbose = verbose

    def filter_classes(self):
        # Redirect console output to STDOUT
        sys.stdout = open(self.output_file, 'w')

        # Read the input file
        with open(self.input_file, 'r') as file:
            lines = file.readlines()

        # Filter the lines based on the filtered classes
        filtered_lines = [line for line in lines if any(class_name in line for class_name in self.filtered_classes)]

        # Write the filtered lines to the output file
        with open(self.output_file, 'w') as file:
            file.writelines(filtered_lines)

        # Restore console output
        sys.stdout = sys.__stdout__

        # Print the count if count flag is set
        if self.count:
            print(f"Filtered classes count: {len(filtered_lines)}")

        # Print the filtered lines if verbose flag is set
        if self.verbose:
            print("Filtered lines:")
            for line in filtered_lines:
                print(line.rstrip())

# Example usage
#input_file = 'input.txt'
#output_file = 'output.txt'
#filtered_classes = ['class1', 'class2', 'class3']
#count = True
#verbose = True

#class_filter = ClassFilter(input_file, output_file, filtered_classes, count=count, verbose=verbose)
#class_filter.filter_classes()