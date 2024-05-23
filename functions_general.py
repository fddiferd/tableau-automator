import xml.etree.ElementTree as ET
import subprocess


def get_xml_tree(file_path):
    return ET.parse(file_path)


def add_styles(dashboard_root: ET.Element, element: str):

    def add_style_to(style_root, element):
        style_rule = ET.SubElement(style_root, 'style-rule', {'element': element})
        ET.SubElement(style_rule, 'format', {'attr': 'color', 'value': '#56a9ac'})
        ET.SubElement(style_rule, 'format', {'attr': 'font-weight', 'value': 'bold'})
        ET.SubElement(style_rule, 'format', {'attr': 'font-size', 'value': '12'})
        ET.SubElement(style_rule, 'format', {'attr': 'text-align', 'value': 'center'})

    style_root = dashboard_root.find('style')
    if style_root is not None:
        add_style_to(style_root, element)
        # add_style_to(style_root, 'legend-title')
        # add_style_to(style_root, 'quick-filter-title')
        

def get_new_file_path(file_path) -> str:
    base_name, extension = file_path.rsplit('.', 1)
    new_file_path = f"{base_name} - New.{extension}"
    return new_file_path


def save_and_open(tree, file_path):
    new_file_path = get_new_file_path(file_path)
    tree.write(new_file_path)
    subprocess.run(['open', new_file_path])