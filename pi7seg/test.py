import seven_segment_display
import seven_segment_i2c
#for rev 2.0 Model B, use:
#bus = seven_segment_i2c.SevenSegmentI2cBus(1)
#for rev 1.0 Model B, use:
bus = seven_segment_i2c.SevenSegmentI2c(1)
display = seven_segment_display.SevenSegmentDisplay(bus)
display.clear_display()
display.clear_display()
display.write_int(8888)
