import Bridge
import json
import requests

bridge_ip = "192.168.2.108"
bridge_username = "UZNT4nJfPTh6BqQILPw8i8qFvB6hs-gOS21WeSCK"

if __name__ == '__main__':
    bridge = Bridge.Bridge(bridge_ip, bridge_username)
    lights = bridge.get_bulbs()

    for b in lights:
        b.turn_on()
        b.update()
    for b in lights:
        b.set_transition_time(0)
        b.set_brightnes(128)
        b.update()
    for b in lights:
        b.set_hue_inc(1337)
        b.update()

    # for l in lights:
    #   l.turn_off()
    #  l.update()

#    l1 = Lights("1")
#   l2 = Lights("2")
#  l1.turn_on()
# l2.turn_on()
# l1.update()
#    l2.update()
#   l2.set_alert("lselect")
#  l2.update()

# while(True):
#    l1.set_hue_inc(1337)
#    l1.set_transition_time(50)
#    l1.update()
#    time.sleep(5)
#    l2.set_hue_inc(4223)
#    l2.set_transition_time(50)
#    l2.update()
#    time.sleep(5)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
