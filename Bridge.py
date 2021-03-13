import Bulb
import requests

headers = {'content-type': 'application/json'}

class Bridge():
    def __init__(self, bridge_ip, username):
        self.ip = bridge_ip
        self.username = username

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_ip(self, ip):
        self.ip = ip

    def get_ip(self):
        return self.ip

    def get_base_url(self):
        return "http://" + self.ip + "/api/" + self.username + "/"

    def get_bulbs(self) -> [Bulb]:
        bulbs = []
        r = requests.get(
            url=self.get_base_url() + "lights",
            headers=headers
        )
        response = r.json()
        for r in response:
            # print(response[str(r)])
            bulbs.append(Bulb.Bulb(self.get_base_url() + "lights/" + str(r) + "/"))
        return bulbs

    def __str__(self):
        return self.get_base_url()
