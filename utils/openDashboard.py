#******************************************************************************
# * @file           : openDashBoard.py
# * @brief          : generate the link to the dashboard and open the link in the browser
# ******************************************************************************
# * @attention
# *
# * <h2><center>&copy; Copyright (c) 2022 STMicroelectronics.
# * All rights reserved.</center></h2>
# *
# * This software component is licensed by ST under BSD 3-Clause license,
# * the "License"; You may not use this file except in compliance with the
# * License. You may obtain a copy of the License at:
# *                        opensource.org/licenses/BSD-3-Clause
# ******************************************************************************
import os, sys
import getopt
import webbrowser



HELP = ['openDashboard.py options:', 
        '\n\t-h or --help for help',
        '\n\t--key-id=[access key]', 
        '\n\t--secret-key=[secret key]', 
        '\n\t--device-id=[device name]']


def main(argv):

    key = ''
    secretKey = ''
    deviceName = ''
    bucketURL = ''

    # Collect Parameters from command line
    try:
        opts, args = getopt.getopt(argv,"h", ["help", "key-id=", "secret-key=", "device-id=", "bucket-url="])
    except getopt.GetoptError:
        print('Parameter Error')
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(*HELP)
            sys.exit(1)

        elif opt in ("--key-id"):
            key = arg

        elif opt in ("--secret-key"):
            secretKey = arg

        elif opt in ("--device-id"):
            deviceName = arg

        elif opt in ("--bucket-url"):
            bucketURL = arg

        
    
    url = bucketURL + "/?KEY_ID="+ key + "&SECRET_KEY=" + secretKey + "&DeviceID=" + deviceName
    webbrowser.open(url)

    path = os.path.join('./', "STM32U5_AWS_Dashbaord.url")
    shortcut = open(path, 'w')
    shortcut.write('[InternetShortcut]\n')
    shortcut.write('URL=%s' % url)
    shortcut.close()

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        print(e)
        sys.exit(1)

#************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/                