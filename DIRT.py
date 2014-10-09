#!/usr/bin/env python
"""
Main entrance point for DIRT
"""

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='DIRT.py',
                                     description='Find reused text in a corpus of text')

    parser.add_argument('input_dir',
                        help='Directory containing input corpus')
    parser.add_argument('output_dir',
                        help='Directory for output files')

    args = parser.parse_args()
