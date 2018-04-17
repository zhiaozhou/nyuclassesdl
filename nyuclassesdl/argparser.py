# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--MFA", help="choose a way for MFA", type=str)
parser.add_argument("--dir", help="choose a directory to download the files", type=str)
parser.add_argument("--un", help="NYU netid", type=str)
parser.add_argument("--ps", help="NYU password", type=str)

args = parser.parse_args()

print(args.ps)