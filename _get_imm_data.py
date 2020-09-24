#!/usr/bin/env python
from pprint import pprint
import json
import re
REG_EX = r"^L.\d[-\s]"

def strip_leading_l(ports):
    rooms_imm = []
    for port in ports:
        if re.search(REG_EX, port['Room']):
            rooms_imm.append(port['Room'][1:])
        else:
            rooms_imm.append(port['Room'])
    return rooms_imm

'''
grab latest imm data from imm.thecrick.org.
It arrives in json format so return 
the data as a dict
see https://automatetheboringstuff.com/chapter11/
'''
import requests

def update_imm_data(IMM_REPORT_URL):
    print('Getting data from {}'.format(IMM_REPORT_URL))
    res = requests.get(IMM_REPORT_URL)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    with open('ports.json', 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)


def get_imm_data(STRIP_L, CHECK_DUP, UPDATE, IMM_REPORT_URL):
    rooms_dup = ['IMM Duplicate Rooms not checked']
    if UPDATE:
        update_imm_data(IMM_REPORT_URL)
    ports_f = open('ports.json')
    ports = json.load(ports_f)
    rooms_imm = []
    rooms_d = {}
    port_room_missing_d = {}
    for port in ports:
        if port['Room'] == '':
            if port_room_missing_d.get(port['Switch']) is None:
                port_room_missing_d[port['Switch']] = []
            port_room_missing_d[port['Switch']].append(port['Switch Port'])
    # list switches and ports with missing rooms
    if STRIP_L:
        rooms_imm = strip_leading_l(ports)
    else:
        for port in ports:
            rooms_imm.append(port['Room'])
    if CHECK_DUP:
        # Data has multiple copies of rooms, set then strip
        all_rooms = []
        rooms_dup = []
        for port in ports:
            all_rooms.append(port['Room'])
        all_rooms_set = set(all_rooms)
        all_rooms_stripped = []
        for tmp_room in all_rooms_set:
            if re.search(REG_EX, tmp_room):
                tmp_room = tmp_room[1:]
            all_rooms_stripped.append(tmp_room)
        # all_rooms should no longer be unique
        for room in all_rooms_stripped:
            if all_rooms_stripped.count(room) > 1:
                rooms_dup.append(room)
    rooms_set = set(rooms_imm)
    # Create a dict with a list of switches feeding each room
    for room in rooms_set:
        rooms_d[room] = []
        my_list = []
        for port in ports:
            if room in port['Room']:
                my_list.append(port['Switch'])
            '''
            if STRIP_L:
                if room in port['Room']:
                    print(room+" and "+port['Room'])
                    my_list.append(port['Switch'])
            else:
                if port['Room'] == room:
                    print(room+" and "+port['Room'])
                    my_list.append(port['Switch'])
            '''
        rooms_d[room] = set(my_list)
    return rooms_set, ports, rooms_d, rooms_dup, port_room_missing_d
