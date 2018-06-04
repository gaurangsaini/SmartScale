import seven_segment_display
import seven_segment_spi
# SPI bus 0, Chip Enable 0
bus = seven_segment_spi.SevenSegmentSpi(0, 0)
display = seven_segment_display.SevenSegmentDisplay(bus)
display.clear_display()
display.write_int(1234)
