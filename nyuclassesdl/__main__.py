#!/usr/bin/env python
# encoding: utf-8
import sys
import argparse
from nyuclassesdl import run

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--MFA", help="choose a way for MFA", type=str)
    parser.add_argument("--dir", help="choose a directory to download the files", type=str)
    parser.add_argument("--un", help="NYU netid", type=str)
    parser.add_argument("--ps", help="NYU password", type=str)

    args = parser.parse_args()
    
    if not args.un:
        print('You should input your username')
    if not args.ps:
        print('You should input your password')
    if not args.MFA:
        print('You should choose your way for MFA validation')   
    run(args.un,args.ps,args.MFA,args.dir)

if __name__ == '__main__':
    main()