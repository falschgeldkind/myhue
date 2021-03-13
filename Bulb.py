import requests
import json

class Bulb:
    def __init__(self,url):
        self.url = url
        self.payload = {}

    def update(self):
        print(self.payload)
        r = requests.put(
            url=self.url+"state",
            data=json.dumps(self.payload),
            headers={'content-type': 'application/json'}
        )
        print(r.json())

    def clear_payload(self):
        self.payload.clear()

    def update_and_clear(self):
        self.update()
        self.clear_payload()

    def turn_off(self):
        self.payload.update({"on":False})

    def turn_on(self):
        self.payload.update({"on":True})

    def set_brightnes(self,brightness):
        self.payload.update({"bri":brightness})

    def set_hue(self,hue):
        self.payload.update({"hue":hue})

    def set_saturation(self,sat):
        self.payload.update({"sat":sat})

    def set_hue_inc(self,hue_inc):
        self.payload.update({"hue_inc":hue_inc})

    def set_saturation_inc(self,sat_inc):
        self.payload.update({"sat_inc":sat_inc})

    def set_brightnes_inc(self,bri_inc):
        self.payload.update({"bri_inc":bri_inc})

    def set_transition_time(self, ttime):
        self.payload.update({"transitiontime":ttime})

    def set_effect(self, effect):
        self.payload.update({"effect":effect})

    def set_alert(self, alert):
        self.payload.update({"alert":alert})
