from xml.etree import ElementTree

def indent(elem, level=0):
    if elem.tag == 'tspan':
        return
    i = "\n" + level*"  "
    if len(elem):
        if elem.tag != 'text' and (not elem.text or not elem.text.strip()):
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if elem.tag != 'text' and (not elem.text or not elem.text.strip()):
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def svgize(elem):
    if elem.tag == 'p':
        elem.tag = 'text'
    elif elem.tag == 'code':
        elem.tag = 'tspan'
        elem.attrib['class'] = 'code'
    for elem in elem:
        svgize(elem)

def myindent(src):
    root = ElementTree.parse('/tmp/xmlfile').getroot()
    indent(root)
    return ElementTree.dump(root)
