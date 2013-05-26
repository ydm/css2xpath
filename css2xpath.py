#!/usr/bin/env python3

from io import StringIO
import re
import sys


def tok2nodetest(tok, write):
    m = re.match('\\w+', tok)
    if m is None:
        write('*')
        return tok
    write(m.group())
    return tok[len(m.group()):]


def tok2predicate(tok, write):
    predicates = (
        (r'\.([\-\w_]+)', "[contains(@class, '{}')]"),
        (r'#([\-\w_]+)', "[@id='{}']"),
        (r':nth-child\((\d+)\)', '[{}]'),
        (r'():first', '{}[1]')
    )
    for regexp, fmt in predicates:
        m = re.match(regexp, tok)
        if m:
            write(fmt.format(m.group(1)))
            return tok[len(m.group()):]
    raise Exception('Unknown predicate token: {}'.format(tok))


def transform(sel):
    'Transform a css selector to xpath query string'
    buf = StringIO()
    tokens = sel.split()
    if not tokens:
        return ''
    direct = False
    for token in tokens:
        if token == '>':
            direct = True
        else:
            axis, direct = '/' if direct else '//', False
            buf.write(axis)
            token = tok2nodetest(token, buf.write)
            while token:
                token = tok2predicate(token, buf.write)
    return buf.getvalue()


def main():
    if len(sys.argv) > 1:
        for sel in sys.argv[1:]:
            print(transform(sel))
    else:
        while 1:
            try:
                sel = input()
            except EOFError:
                break
            else:
                print(transform(sel))


if __name__ == '__main__':
    main()
