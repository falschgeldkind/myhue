import requests
import json

class Bulb:
    '''    on = bool
    bri = int
    hue = int
    sat = int
    effect = str
    alert = str
    bri_int = int
    hue_inc = int
    sat_inc = int
    '''
    payload = {}

    def __init__(self,url):
        self.url = url

    def update(self):
        print(self.payload)
        r = requests.put(
            url=self.url+"state",
            data=json.dumps(self.payload),
            headers={'content-type': 'application/json'}
        )
        print(r.json())
        self.payload.clear()

    '''def set_state(self,on):
'''

    def turn_off(self):
        payload = {"on":False}
        self.payload.update(payload)

    def turn_on(self):
        payload = {"on":True}
        self.payload.update(payload)

    def set_brightnes(self,brightness):
        payload = {"bri":brightness}
        self.payload.update(payload)

    def set_hue(self,hue):
        payload = {"hue":hue}
        self.payload.update(payload)

    def set_saturation(self,sat):
        payload = {"sat":sat}
        self.payload.update(payload)

    def set_hue_inc(self,hue_inc):
        payload = {"hue_inc":hue_inc}
        self.payload.update(payload)

    def set_saturation_inc(self,sat_inc):
        payload = {"sat_inc":sat_inc}
        self.payload.update(payload)

    def set_brightnes_inc(self,bri_inc):
        payload = {"bri_inc":bri_inc}
        self.payload.update(payload)

    def set_transition_time(self, ttime):
        payload = {"transitiontime":ttime}
        self.payload.update(payload)

    def set_effect(self, effect):
        payload = {"effect":effect}
        self.payload.update(payload)

    def set_alert(self, alert):
        payload = {"alert":alert}
        self.payload.update(payload)
