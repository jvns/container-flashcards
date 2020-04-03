#!/usr/bin/env python3

import yaml
import textwrap
import sys
import os
import subprocess
import os
from xml.etree.ElementTree import Element
from xml.etree import ElementTree
from myxml import indent

def texts(data, back=False):
    big_lines = into_lines(data.get('big', None), 'big')
    small_lines = into_lines(data.get('small', None), 'small')

    big_y, small_y = calc_y(len(big_lines), len(small_lines))

    big = area(big_lines, 'big', big_y, back=back)
    small = area(small_lines, 'small', small_y, back=back)
    return big + small

def svg(data, back=False):
    svg_element = Element('svg', {
        'viewBox':"0 0 400 250",
        'xmlns:svg':"http://www.w3.org/2000/svg",
        'xmlns':"http://www.w3.org/2000/svg",
        'xmlns:sodipodi':"http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
        'xmlns:inkscape':"http://www.inkscape.org/namespaces/inkscape",
    })
    if back:
        svg_element.append(Element('rect', {
            'width': '100%',
            'height': '100%',
            'fill': '#265c91',
        }))
    style_elt = Element('style')
    style_elt.text = """
@import url("/fonts/stylesheet.css");
.big {
    white-space: pre;
    font-size: 24px;
    text-anchor: middle;
}
.line {
    dominant-baseline: hanging;
    font-family: 'juliabold';
}
.small {
    white-space: pre;
    font-size: 20px;
}
"""
    svg_element.append(style_elt)
    for text in texts(data, back=back):
        svg_element.append(text)
    return svg_element


def calc_y(big_lines, small_lines):
    big_height = big_lines * 28
    height = big_height + small_lines * 24
    if small_lines == 0:
        return (250 - height)/2.0, 0
    elif big_lines == 0:
        return 0, (250 - height)/2.0 + 10
    else:
        return 20, 20 + big_height + (250-height - 40)/2 + 10


def area(lines, size, y, back=False):
    if len(lines) == 0:
        return []
    attributes = dict(y=str(y))
    if size == 'big':
        x = '200'
        dy = 28
    else:
        x = '30'
        dy = 24
    texts = []
    for i, text in enumerate(lines):
        line_attributes = {
            'x': x,
            'y': str(y + dy * i),
            'class': 'line ' + size,
        }
        texts.append(line(text, line_attributes, back=back))
    return texts


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
        return []
    lines = textwrap.wrap(text, wrap)
    if len(lines) > 0 and len(lines[0]) >= 2 and lines[0][1] == '.' and lines[0][0] != '.':
        return [lines[0]] + ['   ' + x for x in lines[1:]]
    else:
        return lines

def format_styles(styles):
    return ''.join('{}: {};'.format(key, val) for key, val in styles.items())

def line(text, attributes, back=False):
    styles = {}
    if text.startswith('CODE: '):
        text = text.lstrip('CODE: ')
        styles['font-family'] = 'Inconsolata'
    if back:
        styles['fill'] = 'white'
    if len(styles) > 0:
        attributes['style'] = format_styles(styles)
    elt = Element('text', attributes)
    elt.text = text
    return elt

def prettify(top):
    indent(top)
    return ElementTree.tostring(top, 'utf-8').decode('utf-8')

def parse_args():
    set_name = sys.argv[1]
    with open(set_name + '.yaml') as f:
        data = yaml.safe_load(f)

    if len(sys.argv) > 2:
        to_render = sys.argv[2:]
    else:
        to_render = data.keys()
    return data, set_name, to_render


def render(data, set_name, to_render):
    dest = '../public/cards/' + set_name
    for name in to_render:
        pair = data[name]
        with open(dest + '/' + name + '.svg', 'w') as f:
            top = svg(pair['question'])
            f.write(prettify(top))
        with open(dest + '/' + name + '-back.svg', 'w') as f:
            top = svg(pair['answer'], back=True)
            f.write(prettify(top))


    os.chdir('..')
    with open('preview/' + set_name + '.html', 'w') as f:
        f.write('<html><head><body>')
        f.write(
            '<style type="text/css"> object { border: 1px #444 solid; margin-left: 50px; margin-bottom: 25px; } </style>')
        for name in to_render:
            f.write('<object width="400px" type="image/svg+xml" data="%s"></object>' %
                    (dest + '/' + name + '.svg'))
            f.write('<object width="400px" type="image/svg+xml" data="%s"></object>' %
                    (dest + '/' + name + '-back.svg'))
            f.write('<br>')
        f.write('</body></html>')

    with open('./test_old.html', 'w') as f:
        dest = '../public/cards/tls_old'
        f.write('<html><head><body>')
        f.write(
            '<style type="text/css"> object { border: 1px #444 solid; margin-left: 50px; margin-bottom: 25px; } </style>')
        for name in to_render:
            f.write('<object type="image/svg+xml" data="%s"></object>' %
                    (dest + '/' + name + '.svg'))
            f.write('<object type="image/svg+xml" data="%s"></object>' %
                    (dest + '/' + name + '-back.svg'))
            f.write('<br>')
        f.write('</body></html>')

if __name__ == '__main__':
    data, set_name, to_render = parse_args()
    render(data, set_name, to_render)
