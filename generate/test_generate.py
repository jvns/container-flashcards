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

def test_code_nowrap():
    #with open('linux.yaml') as f:
    #    data = yaml.safe_load(f)
    #print(repr(data['same-address']['answer']))
    wanted = """<svg>
  <text class="line big" x="200" y="20">yes!</text>
  <text class="line small" x="30" y="29">Linux uses "virtual memory"</text>
  <text class="line small" x="30" y="53">which means that every address it</text>
  <text class="line small" x="30" y="77">gives a process is mapped to a</text>
  <text class="line small" x="30" y="101">different address in RAM</text>
  <text class="line small" style="font-family: Inconsolata;" x="30" y="125">PID   virtual address   real address</text>
  <text class="line small" style="font-family: Inconsolata;" x="30" y="149">1234  0x123400          0x18293200</text>
  <text class="line small" style="font-family: Inconsolata;" x="30" y="173">2345  0x123400</text>
  <text class="line small" x="30" y="245">0x29312000</text>
</svg>"""
    data = {'small': 'Linux uses "virtual memory"  which means that every address it gives a process is mapped to a different address in RAM\n\nCODE: PID   virtual address   real address\nCODE: 1234  0x123400          0x18293200\nCODE: 2345  0x123400          0x29312000\n', 'big': 'yes!\n'}

    assert(wanted == tostring(data))

def test_code_basic():
    wanted = """<svg>
  <text class="line big" x="200" y="69.0">when you run:</text>
  <text class="line big" style="font-family: Inconsolata;" x="200" y="97.0">$ kill 12345</text>
  <text class="line big" x="200" y="125.0">to stop a program, what</text>
  <text class="line big" x="200" y="153.0">happens?</text>
</svg>
"""
    data = {'big': 'when you run:\nCODE: $ kill 12345\nto stop a program, what happens?\n'}
    assert(wanted == tostring(data))

###def test_blah():
###    with open('linux.yaml') as f:
###        data = yaml.safe_load(f)
###    data = data['kill']['question']
###    print(repr(data))
###    print(tostring(data))
###
###    assert(False)
