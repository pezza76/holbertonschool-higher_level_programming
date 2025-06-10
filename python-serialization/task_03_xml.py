#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')

    for i, j in dictionary.items():
        child = ET.SubElement(root, i)
        value = str(j)
        child.text = value
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='unicode')

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()


    result = {}
    for child in root:
        result[child.tag] = child.text
    return result

