#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
## [create_portlists.py](create_portlists_py.html)

Creates portlists for ansible-nas

- extracts via `grep -r` a list of lines which contain `port }}:`
- from this list extracts the application name and the port definition
- builds an md file `portslist_apps.md` sorted by applications
- builds an md file `portslist_ports.md` sorted by ports

### Remarks
- the regex used in make_port_list was created using
    [regex101](https://regex101.com/r/rB7yPs/1)
- for handling the entry of "ispyagentdvr", a trick was used ;-)

### Used Libraries

#### Standard

- [operator](https://docs.python.org/3/library/operator.html)
- [os](https://docs.python.org/3/library/os.html)
- [re](https://docs.python.org/3/library/re.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)

#### Third-party

#### Local

"""
# Standard library | third-party | local imports
import operator
import os
# import pprint
import re
import subprocess

# some constants
(DQ, SL, caret, dot, ddot, empty, NL, EB, cur) = (
    '"',
    "/",
    "^",
    ".",
    "..",
    "",
    "\n",
    "        ",
    "€",
)

# Multiple blanks
(OB, TB, FB, SB, EB) = (" ", 2 * " ", 4 * " ", 6 * " ", 8 * " ")

# global variables
root_dir = '/media/EDV/repos/github/forked/ansible-nas/'
roles_dir = root_dir + 'roles/'
app_file = 'portlist_apps.md'
port_file = 'portlist_ports.md'

grep_cmd = ["grep", "-r", "port }}:", "."]

apps_header = '| App | Portname | Portnumber | Type |'
apps_format = '|-----|----------|-----------:|------|'
ports_header = '| Portnumber | App | Portname | Type |'
ports_format = '|-----------:|-----|----------|------|'

port_range = '50000-50010'

# regular expressions
entry_regex = r"\.\/([^\/]*)[^{]*{{ (\S*)[^:]*:([\d-]*)\/*(\w*)\""


def search_port_entries():
    os.chdir(f'{roles_dir}')
    grep_list = subprocess.run(
        grep_cmd, capture_output='True'
    ).stdout.decode()
    entries = NL.join(sorted(grep_list.split(NL)))
    return entries


def make_port_list(entries):
    matches = re.finditer(entry_regex, entries, re.MULTILINE)
    port_list = []
    for matchNum, match in enumerate(matches, start=1):
        (entry, group) = ({}, [])
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            group.insert(groupNum, match.group(groupNum))
        if '-' not in group[2]:
            group[2] = int(group[2])
            (entry['app'], entry['name'], entry['number'], entry['type']) = (
                group[0], group[1], group[2], group[3]
            )
        else:
            (entry['app'], entry['name'], entry['number'], entry['type']) = (
                group[0], group[1], 44444, group[3]
            )
        port_list += [entry]
    port_list_srt = sorted(
        port_list, key=operator.itemgetter('number')
    )
    return (port_list, port_list_srt)


def create_app_file(port_list):
    app_path = root_dir + app_file
    with open(app_path, 'w') as fa:
        fa.write(f'{apps_header}{NL}{apps_format}{NL}')
        for entry in port_list:
            fa.write(
                f'| {entry["app"]} | {entry["name"]} | {entry["number"]} '
                f'| {entry["type"]} |{NL}'
            )
    if os.path.isfile(f'{app_path}'):
        print(f'{app_path} created')
    return


def create_port_file(port_list_srt):
    port_path = root_dir + port_file
    with open(port_path, 'w') as fp:
        fp.write(f'{ports_header}{NL}{ports_format}{NL}')
        for entry in port_list_srt:
            if entry["number"] == 44444:
                entry["number"] = "50000-50010"
            fp.write(
                f'| {entry["number"]} | {entry["app"]} | {entry["name"]} '
                f'| {entry["type"]} |{NL}'
            )
    if os.path.isfile(f'{port_path}'):
        print(f'{port_path} created')
    return


def main():
    entries = search_port_entries()
    (port_list, port_list_srt) = make_port_list(entries)
    create_app_file(port_list)
    create_port_file(port_list_srt)
    return


if __name__ == "__main__":
    main()
