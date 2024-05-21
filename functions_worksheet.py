import xml.etree.ElementTree as ET

def get_worksheet_roots(root):
    return [worksheet for worksheet in root.find('worksheets').iter('worksheet')]
