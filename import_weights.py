from xml.etree.ElementTree import ElementTree,Element

def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8", xml_declaration=True)

def if_match(node, kv_map):
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True

def find_nodes(tree, path):
    return tree.findall(path)

def get_node_by_keyvalue(nodelist, kv_map):
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


def change_node_text(nodelist, text, is_add=False, is_delete=False):
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text

def create_node(tag, property_map, content):
    element = Element(tag, property_map)
    element.text = content
    return element

def add_child_node(nodelist, element):
    for node in nodelist:
        node.append(element)

"""
We could use change_mode_text function to change, add or delete the text of a node.
We could use create_node and add_child_node functions to construct a new node.
Based on the xml file of fundamental FNN's UPPAAL model, we could model complicated FNNs and CNNs which are able to deal with 
MNIST DataSet. Actually, we could model complicated RNNs based on fundamental RNN,s UPPAAL model.
"""


