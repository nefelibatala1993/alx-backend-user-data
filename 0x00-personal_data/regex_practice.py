#!/usr/bin/env python3
"""This is the test file to test the function that will be created"""
import re

target_str = 'My roll number is 25'
res = re.findall(r'\d', target_str) # match all the numbers from 0-9 in the target string
print(res, '\n')

# Always write your regex pattern that you will need to match in the target string as a raw string
print('without raw string: ')
raw_path = r'c:\example\task\new\exercises\session1'

# regex pattern
pattern = r'^c:\\example\\task\\new'

# \n and \t has a special meaning in Python
# will treat them differently
res = re.search(pattern, raw_path)
print(res.group())
