import os
import time
from typing import Union
import adbtv.adbcte as adbcte

PATH = ''

def os_adb(p: str) -> None:
    '''
    Execute ADB from the `PATH`, with some parameter `p`.
    '''
    if os.name == 'nt':
        os.system(f'{PATH}adb.exe {str(p)}')
    else:
        os.system('adb ' + str(p))

def command(cmd: str) -> None:
    '''
    Execute a terminal command `cmd`. Elimines the needing of import `os` again.
    '''
    os.system(str(cmd))

def connect(ip: str, port: int = 5555) -> None:
    '''
    Connect to a device with a given `ip` and `port` default [:5555].
    '''
    os_adb(f'connect {str(ip)}:{str(port)}')

def disconnect() -> None:
    '''
    Disconnect of the device. Doesn't kill the running server.
    '''
    os_adb(f'disconnect')

def kill() -> None:
    '''
    Kill ADB running server.
    '''
    os.system('adb kill-server')

def shell() -> None:
    '''
    Open ADB shell.
    '''
    os_adb(f'shell')

def shell_exit() -> None:
    '''
    Close ADB shell.
    '''
    os.system('exit')

def shell_cmd(cmd: str) -> None:
    '''
    Run an ADB shell command `cmd`. No need to open ADB shell neither to close.
    '''
    os_adb(f'shell {str(cmd)}')

def wake_up() -> None:
    shell_cmd('input keyevent KEYCODE_WAKEUP')

def press_key(key: str, p: int = 1) -> None:
    '''
    Press a `key` (see "key names") with it's ADB code. Parameter `p` (default=1) wakes up the device;
    set `p` to any other value to disable the device wake up command.
    '''
    if p == 1:
        wake_up()
    shell_cmd(f'input keyevent {str(key)}')

def multipress_key(key: str, n, p: int = 1) -> None:
    '''
    Press a `key` (see "key names") with it's ADB code `n` times. Parameter `p` (default=1) wakes up the device;
    set `p` to any other value to disable the device wake up command.
    '''
    if p == 1:
        wake_up()
    for i in range(n):
        shell_cmd(f'input keyevent {str(key)}')

def press(x: float, y: float, p: int = 1) -> None:
    '''
    "Touch" the screen in a given `x` and `y` positions. Parameter `p` (default=1) wakes up the device;
    set `p` to any other value to disable the device wake up command.
    '''
    if p == 1:
        wake_up()
    shell_cmd(f'input tap {str(x)} {str(y)}')

def multipress(x: float, y: float, n: int, p: int = 1) -> None:
    '''
    "Touch" the screen in a given `x` and `y` positions `n` times. Parameter `p` (default=1) wakes up the device;
    set `p` to any other value to disable the device wake up command.
    '''
    if p == 1:
        wake_up()
    for i in range(n):
        shell_cmd(f'input tap {str(x)} {str(y)}')

def type(text: str, p: int = 1) -> None:
    '''
    Type a given `text` on a selected field. Parameter `p` (default=1) wakes up the device;
    set `p` to any other value to disable the device wake up command.
    '''
    if p == 1:
        wake_up()
    shell_cmd(f'input text "{str(text)}"')

def launch_app(app: str, action: Union[str, None] = None, p: int = 1, intent: str = 'android.intent.action.VIEW') -> None:
    '''
    Launch an `app` using `am` with a given app name (see "application names") with it's respective, or user-specified, action name `action` if in `adbct.action_list`.
    Parameter `p` (default=1) wakes up the device; set `p` to any other value to disable the device wake up command.
    '''    
    if p == 1:
        wake_up()
        if action == None:
            shell_cmd(f'am start -a {str(intent)} -n {adbcte.app(str(app))}/{adbcte.view_action(str(app))}')
        else:
            shell_cmd(f'am start -a {str(intent)} -n {str(app)}/{str(action)}')
    else:
        if action == None:
            shell_cmd(f'am start -a {str(intent)} -n {adbcte.app(str(app))}/{adbcte.view_action(str(app))}')
        else:
            shell_cmd(f'am start -a {str(intent)} -n {str(app)}/{str(action)}')

def launch_app_monkey(app: str, p: int = 1, intent: str = 'android.intent.category.LAUNCHER') -> None:
    '''
    Launch an `app` using `monkey` with a given app name (see "application names") with the default or user-specified `intent`.
    Parameter `p` (default=1) wakes up the device; set `p` to any other value to disable the device wake up command.
    '''    
    if p == 1:
        wake_up()
    shell_cmd(f'monkey -p {str(app)} -c {intent} 1')

def stop_app(i: str, p: int = 1) -> None:
    '''
    Stop an `app` with a given app name (see "application names"). Parameter `p` (default=1) wakes up the device; set `p` to any other value to disable the device wake up command.
    '''
    if p == 1:
        wake_up()
    shell_cmd(f'adb shell am force-stop {str(i)}')

def restart_app(app: str, p: int = 1) -> None:
    '''
    Restart an `app` with a given app name (see "application names"). Parameter `p` (default=1) wakes up the device; set `p` to any other value to disable the device wake up command.
    
    Note: This function uses `launch_app_monkey(app)` to start the application.
    '''
    if p == 1:
        wake_up()
    shell_cmd(f'am force-stop {str(app)}')
    time.sleep(5)
    shell_cmd(f'monkey -p {str(app)} -c android.intent.category.LAUNCHER 1')

def get_action(app: str = 'all') -> str:
    '''
    ----
    NOT WORKING BY DEFAULT!
    ----
    Get the action name of an `app` with a given app name (see "application names") or, by default, get the action name of all instaled applications.
    Parameter `p` (default=1) wakes up the device; set `p` to any other value to disable the device wake up command.
    '''
    if str(app) == 'all':
        shell_cmd('pm list packages | sed -e "s/package://" | while read x; do cmd package resolve-activity --brief $x | tail -n 1 | grep -v "No activity found"; done')
    else:
        string = r'{print $2}'
        shell_cmd(f'echo pm dump {adbcte.app(str(app))} | grep -A 1 "MAIN" | grep {adbcte.app(str(app))} | awk "{string}" | grep {adbcte.app(str(app))}')
    return("")