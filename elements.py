import xml.etree.ElementTree as ET

def get_container(type='vert', fixed_size=None):
    container_dict = {
        'h': '35875', 'id': '17', 'param': type, 'type-v2': 'layout-flow', 'w': '79200', 'x': '2500', 'y': '12500'
    }
    
    if fixed_size:
        container_dict['fixed-size'] = str(fixed_size)
    else:
        container_dict['layout-strategy-id'] = 'distribute-evenly'

    return ET.Element('zone', container_dict)