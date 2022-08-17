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

        
    
    url ="http://stm32u5-dashboard.s3-website-us-west-1.amazonaws.com/?KEY_ID="+ key + "&SECRET_KEY=" + secretKey + "&DeviceID=" + deviceName
    webbrowser.open(url)

    path = os.path.join('.\\', "STM32U5_AWS_Dashbaord.url")
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
