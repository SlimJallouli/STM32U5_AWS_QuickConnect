set name=techTour
set ssid=MySSID
set pswd=MyPSWD
set key=test
set secretKey=test

call python utils\flash.py
call python utils\clearSSID.py
call python utils\provision.py --thing-name %name% --wifi-ssid %ssid% --wifi-dredential %pswd% -v
call python utils\openDashboard.py --device-id=%name% --key-id=%key% --secret-key=%secretKey%
call python utils\readSerial.py