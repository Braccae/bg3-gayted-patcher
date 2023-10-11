import xml.etree.ElementTree as ET
import argparse
import re
from collections import Counter

def parse_xml(input_file, output_file, filter_file, verbose, count):
    # Parse XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Extract unique values
    unique_values = Counter()
    for attribute in root.iter('attribute'):
        if attribute.attrib.get('id') == 'Name':
            value = attribute.attrib.get('value')
            if verbose and value not in unique_values:
                print(f'New class found: {value}')
            unique_values[value] += 1

    # Apply filters if filter file is provided
    if filter_file:
        with open(filter_file, 'r') as f:
            filters = [line.strip() for line in f.readlines()]
            for filter_pattern in filters:
                unique_values = {value: count for value, count in unique_values.items() if not re.match(filter_pattern, value)}

    # Write unique values to output file
    with open(output_file, 'w') as f:
        for value, count in unique_values.items():
            if count:  # replace count_flag with count
                f.write(f'{value} {count}\n')
            else:
                f.write(f'{value}\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract unique class names from XML file.')
    parser.add_argument('-i', '--input', required=True, help='Path to input XML file.')
    parser.add_argument('-o', '--output', required=True, help='Path to output text file.')
    parser.add_argument('-f', '--filter', help='Path to filter text file.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode.')
    parser.add_argument('-c', '--count', action='store_true', help='Count the number of occurrences of each unique value.')
    args = parser.parse_args()

    parse_xml(args.input, args.output, args.filter, args.verbose, args.count)