set name=devTest
set ssid=STTestN750
set pswd=9a1v2r73027
set key=AKIAQC3VOUARXGGMWHHO
set secretKey=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&DeviceID=G220701491


call python utils\flash.py
call python utils\clearSSID.py
call python utils\provision.py --thing-name %name% --wifi-ssid %ssid% --wifi-dredential %pswd% -v
call python utils\openDashboard.py --device-id %name% --key-id %key% --secret-key %secretKey%
call python utils\readSerial.py