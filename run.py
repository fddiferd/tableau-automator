import xml.etree.ElementTree as ET
from info import file_path, logo_file_path
from elements import horizontal_container

def new_file_path(file_path) -> str:
    base_name, extension = file_path.rsplit('.', 1)
    new_file_path = f"{base_name} - New.{extension}"
    return new_file_path


def get_dashboard_roots(root):
    return [dashboard for dashboard in root.iter('dashboard')]


def update_dashboard_size(dashboard_root, width: int, height: int):
    for child in dashboard_root:
        if child.tag == 'size':
            child.set('maxheight', str(height))
            child.set('maxwidth', str(width))
            child.set('minheight', str(height))
            child.set('minwidth', str(width))


def get_highest_zone_id(dashboard_root: ET.Element) -> int:
    highest_id = 0
    for zone in dashboard_root.iter('zone'):
        zone_id = int(zone.get('id', 0))
        if zone_id > highest_id:
            highest_id = zone_id
    return highest_id


def create_header(dashboard_root: ET.Element):

    starting_id = get_highest_zone_id(dashboard_root=dashboard_root)

    new_zone = ET.Element('zone', {
        'h': '100000', 
        'id': str(starting_id + 1), 
        'type-v2': 'layout-basic', 
        'w': '100000', 
        'x': '0', 
        'y': '0'
    })

    inner_zone_1 = ET.SubElement(new_zone, 'zone', {
        'h': '100000', 
        'id': str(starting_id + 2), 
        'param': 'vert', 
        'type-v2': 'layout-flow', 
        'w': '100000', 
        'x': '0', 
        'y': '0'
    })

    inner_zone_2 = ET.SubElement(inner_zone_1, 'zone', {
        'fixed-size': '67', 
        'h': '7500', 
        'id': str(starting_id + 3), 
        'is-fixed': 'true', 
        'param': 'horz', 
        'type-v2': 'layout-flow', 
        'w': '99200', 
        'x': '400', 
        'y': '400'
    })

    inner_zone_3 = ET.SubElement(inner_zone_2, 'zone', {
        'fixed-size': '192', 
        'h': '6700', 
        'id': str(starting_id + 4), 
        'is-fixed': 'true', 
        'is-scaled': '1', 
        'param': logo_file_path, 
        'type-v2': 'bitmap', 
        'w': '20000', 
        'x': '800', 
        'y': '800'
    })

    inner_zone_3_style = ET.SubElement(inner_zone_3, 'zone-style')
    ET.SubElement(inner_zone_3_style, 'format', {'attr': 'border-color', 'value': '#000000'})
    ET.SubElement(inner_zone_3_style, 'format', {'attr': 'border-style', 'value': 'none'})
    ET.SubElement(inner_zone_3_style, 'format', {'attr': 'border-width', 'value': '0'})
    ET.SubElement(inner_zone_3_style, 'format', {'attr': 'margin', 'value': '4'})

    inner_zone_4 = ET.SubElement(inner_zone_2, 'zone', {
        'forceUpdate': 'true', 
        'h': '6700', 
        'id': str(starting_id + 5), 
        'type-v2': 'text', 
        'w': '78400', 
        'x': '20800', 
        'y': '800'
    })

    formatted_text = ET.SubElement(inner_zone_4, 'formatted-text')
    run = ET.SubElement(formatted_text, 'run', {
        'bold': 'true', 
        'fontcolor': '#000000', 
        'fontsize': '28'
    })
    run.text = '<Sheet Name>'

    inner_zone_4_style = ET.SubElement(inner_zone_4, 'zone-style')
    ET.SubElement(inner_zone_4_style, 'format', {'attr': 'border-color', 'value': '#000000'})
    ET.SubElement(inner_zone_4_style, 'format', {'attr': 'border-style', 'value': 'none'})
    ET.SubElement(inner_zone_4_style, 'format', {'attr': 'border-width', 'value': '0'})
    ET.SubElement(inner_zone_4_style, 'format', {'attr': 'margin', 'value': '4'})

    inner_zone_2_style = ET.SubElement(inner_zone_2, 'zone-style')
    ET.SubElement(inner_zone_2_style, 'format', {'attr': 'border-color', 'value': '#000000'})
    ET.SubElement(inner_zone_2_style, 'format', {'attr': 'border-style', 'value': 'none'})
    ET.SubElement(inner_zone_2_style, 'format', {'attr': 'border-width', 'value': '0'})
    ET.SubElement(inner_zone_2_style, 'format', {'attr': 'margin', 'value': '4'})

    inner_zone_1_style = ET.SubElement(inner_zone_1, 'zone-style')
    ET.SubElement(inner_zone_1_style, 'format', {'attr': 'border-color', 'value': '#000000'})
    ET.SubElement(inner_zone_1_style, 'format', {'attr': 'border-style', 'value': 'none'})
    ET.SubElement(inner_zone_1_style, 'format', {'attr': 'border-width', 'value': '0'})
    ET.SubElement(inner_zone_1_style, 'format', {'attr': 'margin', 'value': '4'})

    add_to_zones(dashboard_root=dashboard_root, new_zone=new_zone, placement='first')


def add_to_zones(dashboard_root: ET.Element, new_zone: ET.Element, placement='last'):
    zones = dashboard_root.find('zones')
    if zones is None: 
        return
    if placement == 'first':
        zones.insert(0, new_zone)
    else:
        zones.append(new_zone)


def format_filters(dashboard_root: ET.Element):
    zones_element = dashboard_root.find('zones')

    filter_container = horizontal_container
    non_sheet_elements = []

    # Collect non-sheet elements and their parents
    for zone in zones_element.findall('zone'):
        if 'type-v2' in zone.attrib:
            non_sheet_elements.append(zone)

    # Sort non-sheet elements by 'param' attribute in ascending order
    non_sheet_elements = sorted(non_sheet_elements, key=lambda x: x.attrib.get('param', ''))

    # Remove non-sheet elements from their original parent
    for zone in non_sheet_elements:
        zones_element.remove(zone)

    # Add non-sheet elements to the filter container
    for zone in non_sheet_elements:
        filter_container.append(zone)

    # Append the filter container to the zones element
    zones_element.append(filter_container)




tree = ET.parse(file_path)
root = tree.getroot()


dashboards = get_dashboard_roots(root)
selected_dashboard = dashboards[0]

# actions
update_dashboard_size(dashboard_root=selected_dashboard, width=1700, height=1000)
format_filters(dashboard_root=selected_dashboard)
create_header(selected_dashboard)





tree.write(new_file_path(file_path=file_path))

   











# Save the changes back to the file
# tree.write(file_path)

 # for zone in root.iter('zone'):
    #     if 'param' in zone.attrib:
            # Update attributes
            # print(zone)
            # zone.set('mode', 'compact')  # Example value for mode
            # zone.set('show-apply', 'true')  # Example value for show-apply
            # zone.set('values', 'all')  # Example value for values
            # zone.set('margin', '10')  # Example value for margin
            
            # Update or add a title element
            # title_element = zone.find('title')
            # print(title_element)
            # if title_element is None:
            #     title_element = ET.SubElement(zone, 'title')
            # title_element.text = 'Updated Title'  # Example title value
