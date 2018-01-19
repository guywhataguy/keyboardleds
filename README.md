#Keyboard Leds

## About
This projects mimics (to the extent possible) the flashing leds of high end gaming keyboards, on a cheap regular keyboard.
It flashes the available leds (num lock, caps lock, scroll lock) as a high end keyboard would flash other leds.

## Files
"keyboardLed.py" represents a led keyboard light in Linux. The class allows you to comfortably control a keyboard led.
"flashOnKeystroke.py" hooks the keyboard strokes and uses "keyboardLed" to flash the keyboard leds on each keystroke

## Running
simply clone or download this code, and then 
```bash
sudo python flashOnKeystroke.py
``` 
in the folder with the downloaded files

## Working With Keyboard Leds In Linux

#### to get list of available leds:
```bash
ls /sys/class/leds/
```

#### control a led manually
to turn on 
```bash
echo "1" | sudo tee /sys/class/leds/<led_name>/brightness
```
to turn off 
```bash
echo "0" | sudo tee /sys/class/leds/<led_name>/brightness
```
change "<led_name>" with an available led from your computer

#### to get names of devices with leds attached
```bash
cat /sys/class/leds/*/device/name | sort | uniq
```

## Trouble Shooting

#### ModuleNotFoundError: No module named 'pyxhook'
you're missing the module to hook keystrokes. simply 
```bash
sudo pip3 install pyxhook
```

#### Xlib.error.DisplayConnectionError: Can't connect to display ":0"
in the terminal run 
```bash
xhost + 
``` 
and then try running the program again
and when done run 
```bash
xhost -
```
to revert changes from previous command

#### PermissionError: ERROR: Don't have access to '/sys/class/leds/...'
run as root with 
```bash
sudo python flashOnKeystroke.py
```

#### No error messages, but doesn't work
instead of running 'main()' run 'test()'
if the lights flicker, the problem is in hooking the keboard with pyxhook

## Known Issues
- doesn't support windows
- holding keys down for extended periods of time will result in delayed led flashing