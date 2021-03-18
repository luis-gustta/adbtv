import adbtv.base as adb # import the module

adb.PATH = r'path_to_adb' # USUALLY only required in Windows

#adb.kill() # may be needed
adb.connect('adb_device_ip-adress', 5555) # connect to the device; default port [5555]
adb.press_key('key') # key from "key names" (string or integer)
adb.disconnect() # disconncect
#adb.kill() # may be needed