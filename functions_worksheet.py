import xml.etree.ElementTree as ET

def get_worksheet_roots(root):
    return [worksheet for worksheet in root.find('worksheets').iter('worksheet')]

def format_worksheet_title(worksheet_root):
    layout_options = ET.Element('layout-options')
    title = ET.SubElement(layout_options, 'title')
    formatted_text = ET.SubElement(title, 'formatted-text')
    run = ET.SubElement(formatted_text, 'run', {
        'bold': 'true',
        'fontcolor': '#e1462c',
        'fontsize': '16'
    })
    run.text = '<Sheet Name>'

    # Find the table element and its index
    table_element = worksheet_root.find('table')
    if table_element is not None:
        for idx, child in enumerate(list(worksheet_root)):
            if child == table_element:
                worksheet_root.insert(idx, layout_options)
                break
    else:
        # If no table element is found, just append the layout-options
        worksheet_root.append(layout_options)
