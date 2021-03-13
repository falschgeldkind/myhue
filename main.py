import time

import Bridge
import json
import requests
import re


#bridge_ip = "192.168.2.108"
#bridge_username = "UZNT4nJfPTh6BqQILPw8i8qFvB6hs-gOS21WeSCK"

if __name__ == '__main__':
    bridges = []
    with open('config.json') as config_file:
        json_bridges = json.load(config_file)
        for json_bridge in json_bridges:
            bridges.append(
                Bridge.Bridge(
                    json_bridges[json_bridge]["bridge_ip"],
                    json_bridges[json_bridge]["username"]
                )
            )
    '''for b in bridges:
        print(b)
        bulbs = b.get_bulbs()
        bulbs[0].set_hue_inc(8000)
        bulbs[0].update()
        time.sleep(2)
        for bu in  bulbs:
            bu.set_hue_inc(-4000)
            bu.update()
'''
