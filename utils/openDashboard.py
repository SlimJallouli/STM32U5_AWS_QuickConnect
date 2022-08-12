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

    # Collect Parameters from command line
    try:
        opts, args = getopt.getopt(argv,"h", ["help", "key-id=", "secret-key=", "device-id="])
    except getopt.GetoptError:
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(*HELP)
            sys.exit()

        elif opt in ("--key-id"):
            key = arg

        elif opt in ("--secret-key"):
            secretKey = arg

        elif opt in ("--device-id"):
            deviceName = arg

        
    
    url ="http://stm32u5-aws-dashboard.s3-website-us-east-1.amazonaws.com/?KEY_ID="+ key + "&SECRET_KEY=" + secretKey + "&DeviceID=" + deviceName
    webbrowser.open(url)

    path = os.path.join('.\\', "STM32U5_AWS_Dashbaord.url")
    shortcut = open(path, 'w')
    shortcut.write('[InternetShortcut]\n')
    shortcut.write('URL=%s' % url)
    shortcut.close()

if __name__ == "__main__":
    main(sys.argv[1:])