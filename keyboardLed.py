import os
import time


def get_available_leds():
	"""return a list of tuples of input numbers, and led indicators, e.g. [(4, "numlock"), ...]"""
	leds = []
	for led in os.listdir(KeyboardLed.SYSTEM_LED_DIR):
		if KeyboardLed.INPUT_PREFIX not in led:
			continue
		input_number, led_indicator = led.split(KeyboardLed.SPLITTER)
		input_number = input_number.replace(KeyboardLed.INPUT_PREFIX, "")
		leds.append((int(input_number), led_indicator))
	return leds

def get_leds_state(leds):
	return [l.get_state() for l in leds]

def set_leds_state(leds_state, leds):
	[led.set_state(state) for state, led in zip(leds_state, leds)]

def flash_leds_synced(leds):
	# change the values below to fit your needs
	flash_time_off = 0.08
	flash_time_on = 0.01

	leds_state = get_leds_state(leds)
	[l.on() for l in leds]
	time.sleep(flash_time_on)
	[l.off() for l in leds]
	time.sleep(flash_time_off)
	set_leds_state(leds_state, leds)

class KeyboardLed():
	"""led light such as 'numlock' and 'scrolllock' on a typical keyboard"""
	SYSTEM_LED_DIR = r"/sys/class/leds"
	INPUT_PREFIX = "input"
	SPLITTER = "::"
	LED_ON = "1"
	LED_OFF = "0"
	def __init__(self, input_number, led_indicator):
		led_top_dir_name = self.INPUT_PREFIX + str(input_number) + self.SPLITTER + led_indicator
		self._led_brightness_file = os.path.join(self.SYSTEM_LED_DIR, led_top_dir_name, "brightness")
		if not self.check_access():
			raise PermissionError("ERROR: Don't have access to '{}'".format(self._led_brightness_file))

	def check_access(self):
		return os.access(self._led_brightness_file, os.R_OK | os.W_OK)

	def flash(self):
		flash_led_time = 0.1
		self.on()
		time.sleep(flash_led_time)
		self.off()

	def on(self):
		self._write_to_led(self.LED_ON.encode("ascii"))

	def off(self):
		self._write_to_led(self.LED_OFF.encode("ascii"))

	def _write_to_led(self, to_write):
		with open(self._led_brightness_file, "wb") as outfile:
			return outfile.write(to_write)

	def get_state(self):
		with open(self._led_brightness_file, "rb") as infile:
			return infile.read()

	def set_state(self, state):
		self._write_to_led(state)
