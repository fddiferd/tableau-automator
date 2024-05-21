from functions_dashboard import get_dashboard_roots, update_dashboard_size, format_filters,create_header
from functions_worksheet import get_worksheet_roots, format_worksheet_title
from functions_general import get_xml_tree, save_and_open, add_styles


tree = get_xml_tree()
root = tree.getroot()

dashboard_roots = get_dashboard_roots(root)
for dashbord_root in dashboard_roots:
    update_dashboard_size(dashboard_root=dashbord_root, width=1700, height=1000)
    format_filters(dashboard_root=dashbord_root, orientation='vert')
    create_header(dashbord_root)
    add_styles(dashbord_root, 'parameter-ctrl-title')

worksheet_roots = get_worksheet_roots(root)
for worksheet_root in worksheet_roots:
    add_styles(worksheet_root.find('table'), 'legend-title')
    add_styles(worksheet_root.find('table'), 'quick-filter-title')
    format_worksheet_title(worksheet_root)

save_and_open(tree)








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
