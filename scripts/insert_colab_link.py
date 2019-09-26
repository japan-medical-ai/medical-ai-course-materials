#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import re

import bs4

EXCEPT = [
    '01_Basic_Math_for_ML',
]


def process(html, prefix, dir):
    if not re.search('^[0-9]+_', os.path.basename(html)):
        print('{} is not a built ipynb file.'.format(html))
        return
    with open(html) as f:
        soup = bs4.BeautifulSoup(f.read(), features='html.parser')

    name, ext = os.path.splitext(os.path.basename(html))

    if name in EXCEPT:
        return

    p = soup.new_tag('p')
    a = soup.new_tag('a',
                     href='{}/blob/master/{}/{}.ipynb'.format(
                         prefix, dir, name),
                     **{'class': 'reference external'})
    img = soup.new_tag('img',
                       alt='colab-logo',
                       src='https://colab.research.google.com/assets/colab-badge.svg')
    a.append(img)
    p.append(a)

    tags = soup.findAll('h1')
    for tag in tags:
        # insert the colab link after the first h1 tag
        tag.insert_after(p)
        break

    with open(html, 'w') as f:
        f.write(str(soup))

    print('Inserted Colab link to: {}'.format(html))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('html')
    parser.add_argument('prefix')
    parser.add_argument('dir')
    args = parser.parse_args()
    process(args.html, args.prefix, args.dir)