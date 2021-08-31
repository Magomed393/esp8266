import network
ssid = "******"
password = "******"
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid,password)
print(sta.ifconfig())
