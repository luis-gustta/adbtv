import adbtv.base as adb # import the module

adb.PATH = r'path_to_adb' # USUALLY only required in Windows

#adb.kill() # may be needed
adb.connect('adb_device_ip-adress', 5555) # connect to the device; default port [5555]
adb.launch_app_monkey('app_name') # app_name from "application names"
'''monkey usually worth to try if if the app you're trying to launch isn't in the 
   "application names" list and you have no idea about possible intents/action'''
adb.disconnect() # disconncect
#adb.kill() # may be needed