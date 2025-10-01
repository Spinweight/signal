# Troubleshooting Guide

Common issues and solutions for the Van LED Lighting System.

## Power Issues

### Problem: LEDs don't light up at all

**Possible Causes:**
1. No power to LED strips
2. Incorrect voltage (needs 5V, not 12V directly)
3. Poor connection

**Solutions:**
- Measure voltage at LED strip power wires (should be 5V ±0.25V)
- Check DC-DC converter is set to 5V output
- Verify fuse is not blown
- Check all ground connections are secure
- Test with multimeter: measure voltage across LED strip power and ground

### Problem: ESP32 keeps resetting or not staying on

**Possible Causes:**
1. Insufficient power supply
2. Power supply voltage drop when LEDs turn on
3. No common ground

**Solutions:**
- Use DC-DC converter rated for at least 5A (6A+ recommended)
- Add large capacitor (1000µF-2200µF) across power supply output
- Add capacitor (100µF-470µF) near ESP32 VCC/GND pins
- Ensure ground wire is adequate gauge (18 AWG minimum)
- Verify all components share common ground

## LED Issues

### Problem: LEDs show wrong colors

**Possible Causes:**
1. Wrong LED type specified in code
2. Color order mismatch (RGB vs GRB vs others)

**Solutions:**
- Verify LED type: most WS2812B use GRB order
- Try changing `NEO_GRB` to `NEO_RGB` in code if colors are wrong
- Test with example sketch first (examples/test_basic.ino)

### Problem: Random flickering or glitching LEDs

**Possible Causes:**
1. Data line interference or noise
2. Power supply issues
3. Long data wire runs
4. Ground issues

**Solutions:**
- Add 330Ω-470Ω resistor between GPIO pin and LED data wire
- Add 1000µF capacitor across LED strip power supply (close to strip)
- Keep data wires short (under 6 feet if possible)
- Use shielded cable for data wires if near other electrical systems
- Ensure solid common ground connection
- Lower LED brightness to reduce current draw

### Problem: First LED works but rest don't

**Possible Causes:**
1. Incorrect data direction
2. Damaged first LED
3. Bad solder joint between first and second LED

**Solutions:**
- Verify you're connected to "DIN" (Data In) not "DOUT" (Data Out)
- Check LED strip orientation (arrow shows data direction)
- Try cutting off first LED and connecting to second LED
- Inspect solder joints on LED strip for damage

### Problem: Only some LEDs light up

**Possible Causes:**
1. Insufficient power supply
2. NUM_LEDS setting incorrect
3. Damaged section of strip

**Solutions:**
- Check power supply capacity (each LED uses ~60mA at full white)
- Verify NUM_LEDS_PER_STRIP matches your actual LED count
- Test with fewer LEDs to see if it's power related
- Try powering LED strip from both ends (for long strips)
- Measure voltage at far end of strip (should be close to 5V)

## Input Issues

### Problem: Buttons don't work

**Possible Causes:**
1. Incorrect wiring
2. Button not making good contact
3. Missing pull-up configuration

**Solutions:**
- Verify button connects GPIO pin to GND when pressed
- Check that INPUT_PULLUP is set in code (already configured)
- Test button with multimeter (resistance should drop when pressed)
- Try different GPIO pin to rule out damaged pin
- Add external 10kΩ pull-up resistor if internal pull-up not working

### Problem: Brake lights don't activate

**Possible Causes:**
1. Optocoupler/relay not wired correctly
2. No signal from brake light circuit
3. Incorrect GPIO configuration

**Solutions:**
- Verify brake light voltage (should be 12V when pedal pressed)
- Test optocoupler: LED side should have ~12V when brake pressed
- Check transistor output side connects GPIO32 to GND when activated
- Add debugging: print GPIO32 state to Serial Monitor
- Try different GPIO pin to test

### Problem: Buttons trigger multiple times (bouncing)

**Possible Causes:**
1. Mechanical switch bounce
2. Insufficient debounce delay

**Solutions:**
- Increase debounce delay in code (currently 50ms)
- Add 100nF capacitor across button terminals
- Use better quality switches
- Implement software debouncing with longer delay

## Animation Issues

### Problem: Animation too fast or too slow

**Solutions:**
- Adjust BLINK_INTERVAL in config.h (default 500ms)
- Adjust ANIMATION_SPEED in config.h (default 50ms)
- Typical turn signal rate: 60-120 blinks per minute
- 500ms interval = 120 blinks/minute (60 on cycles + 60 off cycles)

### Problem: Animation not smooth

**Solutions:**
- Reduce ANIMATION_SPEED value (faster updates)
- Increase NUM_LEDS_PER_STRIP for finer animation steps
- Check for power supply voltage drop during operation

## Upload Issues

### Problem: Can't upload sketch to ESP32

**Possible Causes:**
1. Wrong COM port selected
2. Driver issues
3. Boot mode not entered

**Solutions:**
- Select correct port in Arduino IDE (Tools → Port)
- Install CP2102 or CH340 USB driver (depending on your board)
- Press and hold BOOT button while clicking Upload
- Try lower upload speed (921600 → 115200)
- Try different USB cable (data cable, not charge-only)
- Disconnect all peripherals during upload

### Problem: Upload successful but code doesn't run

**Solutions:**
- Press RESET button after upload completes
- Check Serial Monitor for startup messages (115200 baud)
- Verify board selection matches your hardware
- Try re-uploading sketch

## Electrical Issues

### Problem: Fuse keeps blowing

**Possible Causes:**
1. Short circuit
2. Fuse rating too low
3. Excessive current draw

**Solutions:**
- Inspect all connections for shorts
- Calculate total current: 3 strips × 30 LEDs × 60mA = 5.4A max
- Use appropriate fuse (5-10A on 12V side)
- Check DC-DC converter not damaged
- Test with LEDs disconnected to isolate problem

### Problem: Wires getting hot

**Solutions:**
- Use heavier gauge wire (18 AWG minimum for LED power)
- Reduce brightness to lower current draw
- Check for poor connections (high resistance = heat)
- Distribute power to LED strips from multiple points

## Diagnostic Commands

### Serial Monitor Testing

Open Serial Monitor (115200 baud) and look for:

```
Van LED Lighting System Starting...
Running startup animation...
System ready!
```

When pressing buttons you should see:
```
Left signal ON
Signal OFF
Right signal ON
Hazard ON
```

### Multimeter Testing Points

1. **Power Supply Output**: Should measure 5.0V ±0.25V
2. **LED Strip Power**: Should measure 4.75V-5.25V at LED strip
3. **GPIO Pins**: Should measure 3.3V when high, 0V when low
4. **Button Pins**: 3.3V when not pressed, 0V when pressed
5. **Brake Input**: 0V when not pressed, pulled low when pressed

## Still Having Issues?

1. Start with test_basic.ino example to verify LED strips work
2. Test one component at a time
3. Use Serial Monitor for debugging
4. Check connections with multimeter
5. Take photos of your setup for troubleshooting
6. Double-check wiring against WIRING.md diagram

## Getting Help

When asking for help, provide:
- Detailed description of the problem
- What troubleshooting steps you've tried
- Serial Monitor output
- Photos of your wiring
- Voltage measurements at key points
- LED strip specifications (model, length)
- Power supply specifications
