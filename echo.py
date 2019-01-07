#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "bomazani with help in mob coding"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description='Perform transformation on input text.')
    parser.add_argument('text', type=str, help='text to be manipulated')
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase')

    return parser


def main(args):
    """Implementation of echo"""
    my_args = create_parser().parse_args(args)
    if not my_args:
        my_args.print_usage()
        sys.exit(1)

    my_string = my_args.text

    if my_args.lower:
        my_string = my_string.lower()
    if my_args.upper:
        my_string = my_string.upper()
    if my_args.title:
        my_string = my_string.title()

    return my_string


if __name__ == '__main__':
    my_args = sys.argv[1:]
    main(my_args)
