#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line will be skipped).

After every 10 lines (including invalid ones) and/or a keyboard interruption
(CTRL + C), prints these statistics from the beginning:
    Total file size:
    format: `File size: <total size>`
    where <total size> is the sum of all previous <file size>

    Number of lines by status code:
    format: `<status code>: <number>`
    possible status codes: 200, 301, 400, 401, 403, 404, 405 and 500
    If a status code doesn't appear or is not an integer, nothing is
    printed for it. Status codes will be printed in ascending order.
"""
import re
import sys


def print_statistics(stat):
    """Prints statistics summary for status codes."""
    print('File size: {}'.format(stat["file_size"]))
    for s in status_codes:
        if s in stat:
            print('{}: {}'.format(s, stat[s]))


if __name__ == '__main__':

    pattern = r'^(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})' +\
                r'(?:\.(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})){3} - ' +\
                r'\[\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]) ' +\
                r'(?:[01]\d|2[0-3])(?::[0-5]\d){2}\.\d{6}\] ' +\
                r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    stat = {'file_size': 0, 'line_no': 0}
    try:
        for line in sys.stdin:
            # if line number is a multiple of 10 print stat
            if stat['line_no'] and stat['line_no'] % 10 == 0:
                print_statistics(stat)

            # increment count for line number
            stat['line_no'] += 1

            match = re.match(pattern, line)
            # skip line if it doesn't match pattern
            if match is None:
                continue

            # get matched groups tuple (status_code, file_size)
            match_groups = match.groups()

            # skip line if status code is not valid
            status_code = match_groups[0]
            if status_code not in status_codes:
                continue

            # increment count for status code and filesize
            stat[status_code] = stat.get(status_code, 0) + 1
            stat['file_size'] += int(match_groups[1])

        print_statistics(stat)

    except KeyboardInterrupt:
        print_statistics(stat)
