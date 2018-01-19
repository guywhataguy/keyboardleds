from keyboardLed import KeyboardLed, flash_leds_synced, get_available_leds
import pyxhook
import os

def test():
	"""test the flickering leds effect"""
	leds = [KeyboardLed(number, indicator) for number, indicator in get_available_leds()]
	import time
	for i in range(3):
		time.sleep(0.2)
		flash_leds_synced(leds)

def main():
	"""hook the keboard and flicker the led lights on keystrokes"""
	leds = [KeyboardLed(number, indicator) for number, indicator in get_available_leds()]

	keyboard_hook = pyxhook.HookManager()
	keyboard_hook.KeyDown = lambda event: flash_leds_synced(leds) 
	keyboard_hook.HookKeyboard()

	keyboard_hook.start()

if __name__ == '__main__':
	main()