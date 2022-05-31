# -*- coding: utf-8 -*-

import sys
import time

import requests


def main():
    if (sys.argv.__len__() != 2):
        print("Program otrzymał nieprawidłową liczbę argumentów")
        sys.exit(1)
    url = "https://api.discogs.com/artists/"
    url_band = url + sys.argv[1]
    response = requests.get(url_band)
    while (response.status_code != 200):
        response = requests.get(url_band)
        if (response.status_code == 429):
            print("oczekiwane na reset timeouta")
            time.sleep(5)
        else:
            print("Błąd API, komunikat błędu:", response)
            sys.exit(1)
    data = response.json()
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

            if (response_member.status_code != 200):
                if (response_member.status_code == 429):
                    print("oczekiwane na reset timeouta")
                    time.sleep(5)
                else:
                    print("Błąd API, komunikat błędu:", response)
                    sys.exit(1)
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
    print("Wybrany Zespół -", data['name'], ":", ', '.join(sorted_band_members))
    print("Zespoły w których występuje dwoje lub więcej członków wybranego zespołu: ")
    for i in sorted_dict:
        if sorted_dict[i].__len__() >= 2:
            print(i, ": ", ', '.join(sorted_dict[i]))

    # print(data['members'])
    # print(result)


if __name__ == "__main__":
    main()
