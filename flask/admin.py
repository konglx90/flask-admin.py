# -*- coding: utf-8 -*-
import argparse
import sys

__author__ = 'kong90'

APP_DESC = """
flask-admin.py startproject hello
"""
print(APP_DESC)


# 其他执行逻辑

def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--startproject', type=str, default='',
                        help="start project")
    parser.add_argument('-a', '--startapp', type=str, default='', help="create a new app")
    args = parser.parse_args()
    if args.startproject:
        print("p")

    if args.startapp:
        print('a')

if __name__ == "__main__":
    main()
