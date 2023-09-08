import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, SINCLAIR_FONT



def main():
	serial = spi(port=0, device=0, gpio=noop())
	device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=True)
	device.contrast(16)
	
	msg= "Casier 1 Ouvert"

	show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT), scroll_delay=0.1)


main()
