import generate
import yaml
from xml.etree.ElementTree import Element
from xml.etree import ElementTree

def tostring(data):
    texts = generate.texts(data)
    svg_element = Element('svg')
    for text in texts:
        svg_element.append(text)
    return generate.prettify(svg_element)

def test_code_basic():
    wanted = """<svg>
  <text class="line big" x="200" y="69.0">when you run:</text>
  <text class="line big" x="200" y="97.0"><tspan class="code">$ kill 12345</tspan></text>
  <text class="line big" x="200" y="125.0">to stop a program, what</text>
  <text class="line big" x="200" y="153.0">happens?</text>
  </svg>
"""
    data = {'big': 'when you run:\n`$ kill 12345`\nto stop a program, what happens?\n'}
    print(tostring(data))
    assert(wanted == tostring(data))

def test_newlines():
    data = {'small': "a\n\nb"}
    wanted = """<svg>
  <text class="line small" x="30" y="99.0">a</text>
  <text class="line small" x="30" y="123.0"> </text>
  <text class="line small" x="30" y="147.0">b</text>
  </svg>
"""
    assert(wanted == tostring(data))



###def test_blah():
###    with open('sql-basics.yaml') as f:
###        data = yaml.safe_load(f)
###    data = data['where-aggregation']['answer']
###    print(repr(data))
###    print(tostring(data))
###
###    assert(False)
