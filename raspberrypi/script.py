#imports
import time
import urllib.request

on_code = 201
off_code = 200

try:
    while True:
        print('Checking API...')
        url = urllib.request.urlopen('https://kurtiii.de/aquarium/api/v1.php')
        response_code = url.getcode()
        print(response_code)
        if response_code == on_code:
            print("Turning on...")

            # TODO: turn wemo on

            print("Turned on, wait 30 seconds")
            time.sleep(30)
            print("Turning off...")

            # TODO: turn wemo off

            print("Turned off, proceed with API-requests")
        else:
            print("No action required")
        time.sleep(10)
except KeyboardInterrupt:
    print('*****************************')
    print('Program stopped')
    print('*****************************')
