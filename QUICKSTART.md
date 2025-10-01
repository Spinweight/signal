# Quick Start Guide

Get your LED lighting system up and running in 5 minutes (bench test only).

## What You Need
- FireBeetle 2 ESP32 (DFR1145)
- 1 WS2812B LED strip (30 LEDs)
- 5V power supply (USB or DC adapter, 2A+)
- 3 wires (for connections)
- Computer with Arduino IDE

## Step 1: Software Setup (2 minutes)

1. Install Arduino IDE from [arduino.cc](https://www.arduino.cc/en/software)
2. Add ESP32 support:
   - File → Preferences
   - Add to Board Manager URLs: 
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - Tools → Board → Boards Manager → Install "esp32"
3. Install library:
   - Sketch → Include Library → Manage Libraries
   - Install "Adafruit NeoPixel"

## Step 2: Upload Test Code (2 minutes)

1. Connect FireBeetle ESP32 to computer via USB
2. Open `examples/test_basic.ino`
3. Tools → Board → Select "ESP32 Dev Module"
4. Tools → Port → Select your ESP32's port
5. Click Upload button
6. Wait for "Done uploading" message

## Step 3: Connect LED Strip (1 minute)

```
ESP32          LED Strip
=====          =========
GPIO25   →     DIN (Data)
VCC (5V) →     +5V (Power)
GND      →     GND (Ground)
```

**Important:** Make sure all three connections are secure!

## Step 4: Power On & Test

1. Keep ESP32 connected to USB (provides 5V power)
2. LED strip should cycle through colors:
   - Red
   - Green  
   - Blue
   - Amber
   - White
   - Rainbow

**Success?** LEDs are working! Ready for full installation.

**Not working?** See TROUBLESHOOTING.md

## Next Steps

Ready for full installation? Continue with:
1. **PARTS_LIST.md** - Get all components
2. **INSTALLATION_GUIDE.md** - Complete setup instructions
3. **WIRING.md** - Detailed wiring diagrams

## 5-Minute Full System Test

Want to test all features quickly?

1. Upload `signal.ino` instead of test_basic.ino
2. Connect 3 LED strips to GPIO25, GPIO26, GPIO27
3. Connect 3 buttons:
   - Left button: GPIO12 to GND
   - Right button: GPIO13 to GND  
   - Hazard button: GPIO14 to GND
4. Power on
5. Press buttons to test turn signals

## Troubleshooting Quick Fixes

**Problem:** Upload fails
- **Fix:** Select correct COM port, try different USB cable

**Problem:** LEDs don't light
- **Fix:** Check DIN connection (not DOUT), verify 5V power

**Problem:** Wrong colors
- **Fix:** Change `NEO_GRB` to `NEO_RGB` in code

**Problem:** ESP32 resets
- **Fix:** Use external 5V power supply, not just USB

## Need Help?

- **Quick issues:** Check TROUBLESHOOTING.md
- **Detailed help:** Read FAQ.md
- **Full setup:** Follow INSTALLATION_GUIDE.md

## Safety Note

⚠️ This quick start is for **BENCH TESTING ONLY**. Do not connect to vehicle without proper installation following INSTALLATION_GUIDE.md and WIRING.md.

## Ready to Install?

Once bench testing is successful:
1. Read INSTALLATION_GUIDE.md completely
2. Gather all parts from PARTS_LIST.md
3. Study WIRING.md for proper connections
4. Follow safety procedures
5. Test thoroughly before driving

Good luck! 🚐✨
