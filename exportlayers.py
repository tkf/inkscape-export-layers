#!/usr/bin/env python

"""
Export selected layers from Inkscape SVG.
"""

from xml.dom import minidom
import codecs


def export_layers(src, dest, hide, show):
    svg = minidom.parse(open(src))
    g_hide = []
    g_show = []
    for g in svg.getElementsByTagName("g"):
        if g.attributes.has_key("inkscape:label"):
            label = g.attributes["inkscape:label"].value
            if label in hide:
                g.attributes['style'] = 'display:none'
                g_hide.append(g)
            elif label in show:
                g.attributes['style'] = 'display:inline'
                g_show.append(g)
    export = svg.toxml()
    codecs.open(dest, "w", encoding="utf8").write(export)
    print "Hide {0} node(s);  Show {1} node(s).".format(
        len(g_hide), len(g_show))


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
