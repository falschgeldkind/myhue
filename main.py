import time
import Bridge
import json
import schedule
import Bulb

class Control:
    s = schedule

    def __init__(self):
        self.bulbs = []
        self.color_bulbs = []
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
        self.bulbs = bridges[0].get_bulbs()
        self.color_bulbs.append(self.bulbs[0])
        self.color_bulbs.append(self.bulbs[1])

    def update_bulbs(self):
        for b in self.bulbs:
            b.update()

    def update_color_bulbs(self):
        for b in self.color_bulbs:
            b.update()

    def colorchange(self,bulb:Bulb, duration:int):
        update_frequency = 2
        update_count = duration / update_frequency
        color_increment = 65536/update_count
        bulb.set_transition_time(update_frequency*10)
        bulb.set_hue_inc(int(color_increment))
        self.s.every(update_frequency).seconds.do(bulb.update)

    def loop(self):
        while(True):
            self.s.run_pending()
            self.s.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    control = Control()

    control.color_bulbs[0].turn_on()
    control.color_bulbs[1].turn_on()
    control.color_bulbs[0].set_hue(0)
    control.color_bulbs[1].set_hue(0)
    control.color_bulbs[0].set_brightnes(254)
    control.color_bulbs[1].set_brightnes(254)
    control.update_color_bulbs()
    control.color_bulbs[0].clear_payload()
    control.color_bulbs[1].clear_payload()

    control.colorchange(control.color_bulbs[0],60)
    control.colorchange(control.color_bulbs[1],120)
    control.loop()

