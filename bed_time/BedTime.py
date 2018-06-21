import requests
import json
import time
from subprocess import call

print("Start")

address = "http://<IP_ADDRESS>"
username = "<HUE_BRIDGE_USERNAME>"
url = address + "/api/" + username + "/lights/"

Lights = {"Stehlampe": 11, "Nachttisch": 14}

data_on = {"on": True}
data_off = {"on": False}
data_bedtime_init = {"on": True, "ct": 500, "bri": 200}


def bed_time(id, time_to_sleep):
    for x in range(0, time_to_sleep):

        json_data = {"on": True, "ct": 500, "bri": (int)(200 - x * 200 / time_to_sleep)}
        # print(json_data)

        for light in id:
            requests.put(url + str(light) + "/state", json.dumps(json_data), timeout=5)

        time.sleep(3)

    for light in id:
        requests.put(url + str(light) + "/state", json.dumps(data_off), timeout=5)

    return


bed_time([11, 14], 15)

#############################
### SHUTDOWN Raspberry Pi ###
#############################

# #call("sudo shutdown -h now", shell=True)
