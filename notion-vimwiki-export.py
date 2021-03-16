#!/usr/bin/env python

import validators
import yaml
import json
import urllib.parse
import panflute as pf
from typing import Union
import io
import re

first_header = True
first_par = True


def move_properties(elem: pf.Element, doc: pf.Doc) -> Union[list[pf.Element], pf.Element, None]:
    global first_par
    if first_par and isinstance(elem, pf.Para):
        first_par = False
        text_so_far = ''
        for child in elem.content:
            if isinstance(child, pf.SoftBreak):
                text_so_far += '\n'
            else:
                text_so_far += pf.tools.stringify(child)
        yaml_dict = yaml.safe_load('\n'.join(['"' + line[:line.index(':')] + '":' \
                                              + urllib.parse.unquote(line[line.index(':') + 1:])
                                              for line in text_so_far.split('\n')]))
        for key in yaml_dict:
            doc.metadata[key] = yaml_dict[key]
        return []


def decrement_headers(elem: pf.Element, doc: pf.Doc) -> Union[list[pf.Element], pf.Element, None]:
    global first_header
    if not first_header and isinstance(elem, pf.Header):
        elem.level += 1
        return elem
        # return pf.Header(elem.content, level=elem.level + 1,)
    else:
        first_header = False


def fix_local_links(elem: pf.Element, doc: pf.Doc) -> Union[list[pf.Element], pf.Element, None]:
    if isinstance(elem, pf.Link) and not validators.url(elem.url) and elem.url.split('.')[-1] == 'md':
        return pf.Link(*[subelem.walk(remove_uuids) for subelem in elem.content],
                       url=re.sub(" [\da-z]{32}", "", urllib.parse.unquote(elem.url)))


def remove_uuids(elem: pf.Element, doc: pf.Doc) -> Union[list[pf.Element], pf.Element, None]:
    if isinstance(elem, pf.Str):
        return pf.Str(re.sub(" [\da-z]{32}", "", elem.text))


def main(doc=None):
    return(pf.run_filters([move_properties, decrement_headers, fix_local_links], doc=doc))


if __name__ == '__main__':
    main()
