#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line will be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), prints these
statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>

    Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

If a status code doesn't appear or is not an integer, nothing is printed for it
    format: <status code>: <number>
status codes will be printed in ascending order"""
import datetime
import re
from shlex import split
import sys


# status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
# request = 'GET /projects/260 HTTP/1.1'
# try:
#     stat = {}
#     while True:
#         # print(split(sys.stdin.readline()))
#         line = split(sys.stdin.readline())
#         # check if line has proper format, if not skip
#         if len(line) != 6 or line[1] != '-' or line[3] != request:
#             continue

#         ip = line[0]
# except KeyboardInterrupt as e:
#     print('interrupted')
#     raise e

# pattern = """\
# ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \
# \[\d{4}-[0-1]{1}[0-2]{1}-[0-3]{1}\d{1} \
# [0-2]{1}\d{1}:[0-5]{1}\d{1}:[0-5]{1}\d{1}.\d{6}\] \
# "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$\
# """
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - ' +\
            r'\[\d{4}-[0-1]{1}[0-2]{1}-[0-3]{1}\d{1} ' +\
            r'[0-2]{1}\d{1}:[0-5]{1}\d{1}:[0-5]{1}\d{1}.\d{6}\] ' +\
            r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

# input = '99.115.145.159 - [2024-01-25 '
# match = re.match(pattern, input)
# print(match)
# print(match.group())
# print(match.groups())
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    stat = {'file_size': 0, 'line_no': 0}
    while True:
        # print(stat)
        match = re.match(pattern, sys.stdin.readline())
        # skip line if it doesn't match pattern
        if match is None:
            continue

        # get matched groups tuple (status_code, file_size)
        match_groups = match.groups()

        # skip line if status code is not valid
        status_code = match_groups[0]
        if status_code not in status_codes:
            continue

        # increment count for status code, filesize and line number
        stat[status_code] = stat.get(status_code, 0) + 1
        stat['file_size'] += int(match_groups[1])
        stat['line_no'] += 1

        # if line number is a multiple of 10 print stat
        if stat['line_no'] and stat['line_no'] % 10 == 0:
            print(f'File size: {stat["file_size"]}')
            sorted_codes = [i for i in status_codes if i in stat]
            sorted_codes.sort(key=lambda x: stat[x], reverse=True)
            for s in sorted_codes:
                print(f'{s}: {stat[s]}')


except KeyboardInterrupt as e:
    print(f'File size: {stat["file_size"]}')
    sorted_codes = [i for i in status_codes if i in stat]
    sorted_codes.sort(key=lambda x: stat[x], reverse=True)
    for s in sorted_codes:
        print(f'{s}: {stat[s]}')
    sys.stdout.flush()
    sys.stdin.flush()
    raise e
