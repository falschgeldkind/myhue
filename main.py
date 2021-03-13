# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import requests
import json
import random

bridge_ip = "192.168.2.108"
bridge_username = "UZNT4nJfPTh6BqQILPw8i8qFvB6hs-gOS21WeSCK"

base_url = "http://"+bridge_ip+"/api/"+bridge_username+"/"
headers = {'content-type': 'application/json'}

#class bulb():
#    def update_bulb(self):
#        payload = {"on":True}
#        r = requests.put(base_url+"lights/"+self.id+"/state",data=json.dumps(payload),headers=headers)
#        print(r.json())

class Lights():
    def __init__(self, id):
        self.id = str(id)

    p = {}
    def add_to_payload(self,payload):
        self.p.update(payload)

    def get_lights():
        r = requests.get(base_url+"lights",headers=headers)
        response = r.json()
        bulb_count = len(response)
        lights = []
        for x in range(1,bulb_count+1):
            print(response[str(x)])
            lights.append(Lights(str(x)))
        return lights

    def turn_off(self):
        payload = {"on":False}
        self.add_to_payload(payload)

    def turn_on(self):
        payload = {"on":True}
        self.add_to_payload(payload)

    def set_brightnes(self,brightness):
        payload = {"bri":brightness}
        self.add_to_payload(payload)

    def set_hue(self,hue):
        payload = {"hue":hue}
        self.add_to_payload(payload)

    def set_saturation(self,sat):
        payload = {"sat":sat}
        self.add_to_payload(payload)

    def set_hue_inc(self,hue_inc):
        payload = {"hue_inc":hue_inc}
        self.add_to_payload(payload)

    def set_saturation_inc(self,sat_inc):
        payload = {"sat_inc":sat_inc}
        self.add_to_payload(payload)

    def set_brightnes_inc(self,bri_inc):
        payload = {"bri_inc":bri_inc}
        self.add_to_payload(payload)

    def set_transition_time(self, ttime):
        payload = {"transitiontime":ttime}
        self.add_to_payload(payload)

    def set_effect(self, effect):
        payload = {"effect":effect}
        self.add_to_payload(payload)

    def set_alert(self, alert):
        payload = {"alert":alert}
        self.add_to_payload(payload)



    def update(self):
        print(self.p)
        r = requests.put(base_url+"lights/"+self.id+"/state",data=json.dumps(self.p),headers=headers)
        print(r.json())
        self.p = {}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lights = Lights.get_lights()
    for l in lights:
        l.turn_off()
        l.update()

    #l1 = Lights("1")
    #l2 = Lights("2")
    #l1.turn_off()
    #l2.turn_off()
    #l1.update()
    #l2.update()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
