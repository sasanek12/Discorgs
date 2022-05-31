# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import string
import sys
import requests
import time
from bs4 import BeautifulSoup
from typing import List


def main():
    if()
    url = "https://api.discogs.com/artists/"
    url_band = url + sys.argv[1]
    response = requests.get(url_band)
    data = response.json()
    members_database = []
    groups = {}
    band_members = []
    for member in data['members']:
        if band_members.__len__() == 0:
            band_members = [member['name']]
        else:
            band_members.append(member['name'])
        timeout = True
        while timeout:
            url_member = url + str(member['id'])
            response_member = requests.get(url_member)

            if(response_member.status_code != 200):
                print("oczekiwane na reset timeouta")
                time.sleep(5)
            else:
                # print(response_member.json())
                # print(response_member.status_code)
                data_groups = response_member.json()
                for band in data_groups['groups']:
                    if band['name'] == data['name']:
                        continue

                    if band['name'] in groups:
                        groups[band['name']].append(data_groups['name'])
                    else:
                        groups[band['name']] = [data_groups['name']]
                timeout = False
    sorted_dict = dict(sorted(groups.items()))
    sorted_band_members = sorted(band_members)
    for band in sorted_dict:
        sorted_dict[band] = sorted(sorted_dict[band])
    print("Wybrany Zespół -",data['name'],":",','.join(sorted_band_members))
    print("Zespoły w których występuje dwoje lub więcej członków wybranego zespołu: ")
    for i in sorted_dict:
        if sorted_dict[i].__len__() >= 2:
            print(i,": ", ', '.join(sorted_dict[i]))


    # print(data['members'])
    # print(result)

if __name__ == "__main__":
    main()
