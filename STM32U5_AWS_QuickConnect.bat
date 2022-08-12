@echo off

set name=G213801835
set ssid=STTestN750
set pswd=9a1v2r73027
set key=AKIAQC3VOUARXGGMWHHO
set secretKey=7QbU0RSsSquT9Hv3SGO9VJIBfINysxmRjadiqGsS
set dummySSID=0
set dummyPSWD=0


call python utils\flash.py
call python utils\setWiFiParam.py --ssid %dummySSID% --pswd %dummyPSWD%
call python utils\provision.py --thing-name %name% --wifi-ssid %ssid% --wifi-credential %pswd%
call python utils\openDashboard.py --device-id %name% --key-id %key% --secret-key %secretKey%
call python utils\readSerial.py