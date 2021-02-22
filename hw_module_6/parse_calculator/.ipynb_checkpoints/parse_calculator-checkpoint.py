# -*- coding: utf8 -*-

import argparse
import getpass

parser = argparse.ArgumentParser()

parser.add_argument("-l",'--lang', type=str, default='ua',
                    help= "Choose language abbreviation! (Ex. 'ua','en')")

parser.add_argument("-c", '--keyword', type=str, default='word',
                    help= "Choose word for filter! (Ex. 'hello')")

parser.add_argument("-m", '--value', type=int, default=0,
                    help= "Choose number of the best moody for tweets! (Ex. '10', '-12')")

args = parser.parse_args()

lang = args.lang
keyword = args.keyword
value = args.value


if __name__ == '__main__':
    print ('Parcer initialized!')
    name = input("Enter name: ")
    p = getpass.getpass(prompt='Password: ')
    print (f"{lang=}, {keyword=}, {value=}, {name=}, {prompt=}")
    
