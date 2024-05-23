from functions_dashboard import get_dashboard_roots, update_dashboard_size, create_dashboard
from functions_worksheet import get_worksheet_roots, format_worksheet_title
from functions_general import get_xml_tree, save_and_open, add_styles
from file_picker import select_file
from info import filter_oreintation

file_path = select_file()

tree = get_xml_tree(file_path)
root = tree.getroot()

dashboard_roots = get_dashboard_roots(root)
for dashboard_root in dashboard_roots:
    update_dashboard_size(dashboard_root=dashboard_root, width=1700, height=1000)
    create_dashboard(dashboard_root=dashboard_root, filter_orientation=filter_oreintation)
    add_styles(dashboard_root, 'parameter-ctrl-title')

worksheet_roots = get_worksheet_roots(root)
for worksheet_root in worksheet_roots:
    add_styles(worksheet_root.find('table'), 'legend-title')
    add_styles(worksheet_root.find('table'), 'quick-filter-title')
    format_worksheet_title(worksheet_root)

save_and_open(tree, file_path)

