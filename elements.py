import xml.etree.ElementTree as ET

def get_container(type='vert'):
    return ET.Element('zone', {
    'h': '35875', 'id': '17', 'layout-strategy-id': 'distribute-evenly', 
    'param': type, 'type-v2': 'layout-flow', 'w': '79200', 'x': '2500', 'y': '12500'
})