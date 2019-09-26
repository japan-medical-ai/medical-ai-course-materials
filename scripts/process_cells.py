#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import argparse
import os
import json


metadata = {
    "colab": {
      "name": "Medical AI Course Materials : {}",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.7.2"
    }
}


def process(ipynb, dirname, notebook_urlbase):
    try:
        nb = json.load(open(ipynb))
    except Exception as e:
        print(str(type(e)), e)
        print(ipynb)
        raise e
    nb['metadata'] = metadata
    nb['metadata']['colab']['name'] = nb['metadata']['colab']['name'].format(os.path.basename(ipynb))
    count = 1
    for i, cell in enumerate(nb['cells']):
        if 'execution_count' in cell:
            nb['cells'][i]['execution_count'] = count
            count += 1

        if cell['cell_type'] == 'markdown':
            for line_i, line in enumerate(cell['source']):
                ret = re.search('(!*)\[([^\]]+)\]\(([^\)]+)\)', line)
                if not ret:
                    continue
                is_image_tag, text, url = ret.groups()

                if is_image_tag:
                    if '_' in text:
                        raise ValueError(
                            'The alt text for an image tag should not contain \'_\', '
                            'but this tag contains it: {} \n'
                            'in {}'.format(line, ipynb))
                # Link
                else:
                    # Relative URL to another notebook
                    if not url.startswith('http') and '.html' in url:
                        absolute_url = os.path.join(notebook_urlbase, url)
                        nb['cells'][i]['source'][line_i] = line.replace(url, absolute_url)
                        print(url, '=>', absolute_url)

    json.dump(nb, open(os.path.join(dirname, os.path.basename(ipynb)), 'w'),
              indent=1, ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ipynb')
    parser.add_argument('dirname')
    parser.add_argument('notebook_urlbase')
    args = parser.parse_args()

    os.makedirs(args.dirname, exist_ok=True)

    process(args.ipynb, args.dirname, args.notebook_urlbase)