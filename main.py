# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import requests
import json

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
    def get_lights(self):
        r = requests.get(base_url+"lights",headers=headers)
        response = r.json()
        bulb_count = len(response)
        for x in range(1,bulb_count+1):
            print(response[str(x)])

    def turn_off(self,bulb):
        payload = {"on":False}
        self.api_put(bulb,payload)

    def turn_on(self,bulb):
        payload = {"on":True}
        self.api_put(bulb,payload)

    def set_brightnes(self,bulb,brightness):
        payload = {"bri":brightness}
        self.api_put(bulb,payload)

    def set_hue(self,bulb,hue):
        payload = {"hue":hue}
        self.api_put(bulb,payload)

    def set_saturation(self,bulb,sat):
        payload = {"sat":sat}
        self.api_put(bulb,payload)

    def api_put(bulb,payload):
        r = requests.put(base_url+"lights/"+bulb+"/state",data=json.dumps(payload),headers=headers)
        print(r.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l = Lights
    l.get_lights()
#    l.turn_off(l,"1")
#    l.get_lights(l)
#    time.sleep(1)
#    l.turn_on(l,"1")
#    time.sleep(2)
#    l.set_brightnes(l,"1",254)
#    l.set_brightnes(l,"2",254)
#    for b in range(255):
#        l.set_saturation(l,"1",b)

#    for h in range(4096):
#        hue = h*16
#        l.set_hue(l,"1",(hue+21845)%65536)
#        l.set_hue(l,"2",hue)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
