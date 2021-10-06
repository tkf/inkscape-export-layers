#!/usr/bin/env python

"""
Export selected layers from Inkscape SVG.
"""

from xml.dom import minidom
import codecs


def export_layers(src, dest, hide, show):
    """
    Export selected layers of SVG in the file `src` to the file `dest`.

    :arg  str    src:  path of the source SVG file.
    :arg  str   dest:  path to export SVG file.
    :arg  list  hide:  layers to hide. each element is a string.
    :arg  list  show:  layers to show. each element is a string.

    """
    svg = minidom.parse(open(src))
    g_hide = []
    g_show = []
    for g in svg.getElementsByTagName("g"):
        if "inkscape:label" in g.attributes:
            label = g.attributes["inkscape:label"].value
            if label in hide:
                g.attributes['style'] = 'display:none'
                g_hide.append(g)
            elif label in show:
                g.attributes['style'] = 'display:inline'
                g_show.append(g)
    export = svg.toxml()
    codecs.open(dest, "w", encoding="utf8").write(export)
    print("Hide {0} node(s);  Show {1} node(s).".format(
        len(g_hide), len(g_show)))


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        '--hide', action='append', default=[],
        help='layer to hide. this option can be specified multiple times.')
    parser.add_argument(
        '--show', action='append', default=[],
        help='layer to show. this option can be specified multiple times.')
    parser.add_argument('src', help='source SVG file.')
    parser.add_argument('dest', help='path to export SVG file.')
    args = parser.parse_args()
    export_layers(**vars(args))


if __name__ == '__main__':
    main()
