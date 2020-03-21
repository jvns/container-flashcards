import yaml
import textwrap
import sys
import os

def svg(data):
    return """
    <svg width="400" height="250"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
>
    {big}
    {small}
</svg>
""".format(
        big=area(data.get('big', None), 'big'),
        small = area(data.get('small', None), 'small'))


def area(text, size):
    if size == 'big':
        start = '50%'
        wrap = 29
        font_size=24
        middle = 'dominant-baseline="middle" text-anchor="middle"'
        y = 80
        dy = 28
    else:
        start = '20'
        wrap = 33
        font_size=20
        middle = ""
        y=140
        dy=24
    if text is None:
        return ''
    lines = [wraptext(text, wrap) for text in text.split('\n')]
    lines = sum(lines, [])
    spans = [line(text, start, y + dy * i) for i, text in enumerate(lines)]
    return """
      <text x="{start}" y="{y}" {middle} style="white-space: pre; font-size:{font_size}px;font-family:juliabold;">
      {spans}
  </text>
         """.format(spans='\n'.join(spans), font_size=font_size, middle=middle, y=y, start=start)

def wraptext(text, wrap):
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


