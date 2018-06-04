import seven_segment_display
import seven_segment_i2c

bus = seven_segment_i2c.SevenSegmentI2c(1)
display = seven_segment_display.SevenSegmentDisplay(bus)

display.clear_display()
display.set_brightness_level(100)
display.clear_display()

#display.write_int(99+1)
#decimalpt = [0b00000100,0b00100000]
#display.set_nondigits(decimalpt)