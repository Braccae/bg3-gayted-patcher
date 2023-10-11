import xml.etree.ElementTree as ET
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Path to input file', required=True)
parser.add_argument('-o', '--output', help='Path to output file', required=True)
parser.add_argument('-c', '--classes', nargs='+', help='Classes to match', required=True)
parser.add_argument('-l', '--levels', nargs='+', help='Levels to match', required=True)
args = parser.parse_args()

# Parse XML
tree = ET.parse(args.input)
root = tree.getroot()

# Iterate over nodes
for node in root.iter('node'):
    if node.attrib.get('id') == 'Progression':
        name = node.find("./attribute[@id='Name']")
        level = node.find("./attribute[@id='Level']")
        if name is not None and level is not None:
            if name.attrib.get('value') in args.classes and level.attrib.get('value') in args.levels:
                allow_improvement = node.find("./attribute[@id='AllowImprovement']")
                if allow_improvement is not None:
                    allow_improvement.attrib['value'] = 'True'
                else:
                    new_attr = ET.SubElement(node, 'attribute')
                    new_attr.attrib['id'] = 'AllowImprovement'
                    new_attr.attrib['type'] = 'bool'
                    new_attr.attrib['value'] = 'True'

# Write back to file
tree.write(args.output, xml_declaration=True, encoding='UTF-8')