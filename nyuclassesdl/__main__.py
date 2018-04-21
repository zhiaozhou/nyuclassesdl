#!/usr/bin/env python
# encoding: utf-8
import sys
import argparse
from firefox import run
from chrome import run_chrome

def main():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--browser", help="choose your browser (google or firefox)", type=str)
    parser.add_argument("--MFA", help="choose a way for MFA", type=str)
    parser.add_argument('--cls', help="choose a class to download the files", nargs='+')
    parser.add_argument("--dir", help="choose a directory to download the files", type=str)
    parser.add_argument("--un", help="NYU netid", type=str)
    parser.add_argument("--ps", help="NYU password", type=str)
    parser.add_argument("--exe", help="driver executable file", type=str)
    
    args = parser.parse_args()
    
    if not args.un:
        print('You should input your username')
    if not args.ps:
        print('You should input your password')
    if not args.MFA:
        print('You should choose your way for MFA validation')   
        
    if args.browser == 'firefox':
        run(args.un,args.ps,args.MFA,args.cls,args.dir)
    else:
        run_chrome(args.un,args.ps,args.MFA,args.exe,args.dir,args.cls)
    
if __name__ == '__main__':
    main()