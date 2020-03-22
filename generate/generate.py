import yaml
import textwrap
import sys
import os
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import os


def svg(data):
    big_lines = into_lines(data.get('big', None), 'big')
    small_lines = into_lines(data.get('small', None), 'small')

    big_y, small_y = calc_y(len(big_lines), len(small_lines))

    big = area(big_lines, 'big', big_y)
    small = area(small_lines, 'small', small_y)

    return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
 <svg width="400" height="250"
    xmlns:svg="http://www.w3.org/2000/svg"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
    xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
>
    {big}
    {small}
</svg>
""".format(
        big=big,
        small=small)


def calc_y(big_lines, small_lines):
    big_height = big_lines * 28
    height = big_height + small_lines * 24
    if small_lines == 0:
        return (250 - height)/2.0 + 10, 0
    elif big_lines == 0:
        return 0, (250 - height)/2.0 + 20
    else:
        return 40, 40 + big_height + (250-height - 40)/2 + 10


def area(lines, size, y):
    if len(lines) == 0:
        return ''
    if size == 'big':
        start = '50%'
        font_size = 24
        middle = 'dominant-baseline="middle" text-anchor="middle"'
        dy = 28
    else:
        start = '30'
        font_size = 20
        middle = ""
        dy = 24
    spans = [line(text, start, y + dy * i) for i, text in enumerate(lines)]
    return """
      <text x="{start}" y="{y}" {middle} style="white-space: pre; font-size:{font_size}px;font-family:juliabold;">
      {spans}
  </text>
         """.format(spans='\n'.join(spans), font_size=font_size, middle=middle, y=y, start=start)


def into_lines(text, size):
    if text is None:
        return []
    if size == 'big':
        wrap = 29
    else:
        wrap = 33
    lines = [wraptext(text, wrap) for text in text.split('\n')]
    lines = sum(lines, [])
    return lines


def wraptext(text, wrap):
    if text == '':
        return ['']
    lines = textwrap.wrap(text, wrap)
    if len(lines) > 0 and len(lines[0]) >= 2 and lines[0][1] == '.':
        return [lines[0]] + ['   ' + x for x in lines[1:]]
    else:
        return lines


def line(text, start, y):
    return """
<tspan sodipodi:role="line" x="{start}" y="{y}">{text}</tspan>
""".format(text=text, start=start, y=y)


with open(sys.argv[1]) as f:
    data = yaml.safe_load(f)

if len(sys.argv) > 3:
    to_render = sys.argv[3:]
else:
    to_render = data.keys()

try:
    os.mkdir(dest)
except:
    pass
for name in to_render:
    pair = data[name]
    dest = sys.argv[2]
    with open(dest + '/' + name + '.svg', 'w') as f:
        f.write(svg(pair['question']))
    with open(dest + '/' + name + '-back.svg', 'w') as f:
        f.write(svg(pair['answer']))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


os.chdir('..')
with open('./test.html', 'w') as f:
    f.write('<html><head><body>')
    f.write(
        '<style type="text/css"> object { border: 1px #444 solid; margin-left: 50px; margin-bottom: 25px; } </style>')
    for name in to_render:
        f.write('<object type="image/svg+xml" data="%s"></object>' %
                ('generate/' + dest + '/' + name + '.svg'))
        f.write('<object type="image/svg+xml" data="%s"></object>' %
                ('generate/' + dest + '/' + name + '-back.svg'))
        f.write('<br>')
    f.write('</body></html>')
print("localhost:8000/test.html")
run()
