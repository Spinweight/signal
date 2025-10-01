# Quick Installation Guide

Step-by-step guide to get your van LED lighting system up and running.

## Pre-Installation Checklist

- [ ] All parts from PARTS_LIST.md acquired
- [ ] Arduino IDE installed with ESP32 support
- [ ] Adafruit NeoPixel library installed
- [ ] FireBeetle 2 ESP32 board accessible
- [ ] Work area prepared with tools
- [ ] Vehicle manual consulted for electrical system

## Phase 1: Software Setup (30 minutes)

### 1.1 Install Arduino IDE
1. Download from [arduino.cc](https://www.arduino.cc/en/software)
2. Install for your operating system
3. Launch Arduino IDE

### 1.2 Add ESP32 Board Support
1. Open Arduino IDE
2. Go to **File → Preferences**
3. In "Additional Board Manager URLs", add:
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
4. Click **OK**
5. Go to **Tools → Board → Boards Manager**
6. Search for "esp32"
7. Install "esp32 by Espressif Systems"
8. Wait for installation to complete

### 1.3 Install Adafruit NeoPixel Library
1. Go to **Sketch → Include Library → Manage Libraries**
2. Search for "Adafruit NeoPixel"
3. Install "Adafruit NeoPixel by Adafruit"
4. Close Library Manager

### 1.4 Configure Board Settings
1. Go to **Tools → Board**
2. Select "ESP32 Dev Module" or "FireBeetle-ESP32"
3. Set the following:
   - Upload Speed: 921600
   - Flash Frequency: 80MHz
   - Partition Scheme: Default

### 1.5 Test Upload
1. Connect FireBeetle ESP32 to computer via USB
2. Select correct COM port: **Tools → Port**
3. Open **File → Examples → Basics → Blink**
4. Click **Upload** button
5. Verify onboard LED blinks (confirms board works)

## Phase 2: Bench Testing (1-2 hours)

### 2.1 Test LED Strips Individually
1. Open `examples/test_basic.ino`
2. Set `LED_PIN` to 25 (left turn signal pin)
3. Set `NUM_LEDS` to your strip's LED count
4. Upload to ESP32
5. Connect one LED strip:
   - Data to GPIO25
   - +5V to DC-DC converter output
   - GND to common ground
6. Power on and observe color cycle
7. Repeat for other strips (GPIO26, GPIO27)

### 2.2 Configure Main Sketch
1. Open `signal.ino`
2. Open `config.h`
3. Adjust settings if needed:
   - `NUM_LEDS_PER_STRIP`: Match your LED count
   - `BRIGHTNESS`: Adjust if needed (0-255)
   - Pin assignments if different

### 2.3 Bench Test Complete System
1. Wire up according to WIRING.md:
   - All three LED strips
   - Three push buttons (left, right, hazard)
   - Temporarily skip brake sensor
2. Upload `signal.ino` to ESP32
3. Power on system
4. Open Serial Monitor (115200 baud)
5. Test each function:
   - Press left button → left strip animates
   - Press right button → right strip animates
   - Press hazard button → both strips animate
   - Verify startup animation plays on power-up

### 2.4 Test Brake Signal
1. Add optocoupler circuit
2. Connect to GPIO32
3. Apply 12V to optocoupler input (simulating brake)
4. Verify brake lights illuminate brightly
5. Verify dim tail lights when brake not pressed

## Phase 3: Vehicle Preparation (2-3 hours)

### 3.1 Plan Installation
1. Decide LED strip locations:
   - Behind existing tail light lenses
   - Along rear bumper
   - Under body panels
2. Plan wire routing:
   - From rear to control location
   - Avoid hot/moving parts
   - Use existing wire channels if possible
3. Choose controller location:
   - Inside vehicle, protected from elements
   - Accessible for troubleshooting
   - Near rear of vehicle to minimize wire length

### 3.2 Prepare Mounting
1. Clean surface areas for LED strips
2. Measure and cut strips if needed
3. Test fit strips in location
4. Mark wire routing path
5. Prepare enclosure for ESP32

### 3.3 Access Existing Wiring
1. Locate turn signal wires (if integrating with existing switches)
2. Locate brake light wire (for brake detection)
3. Locate 12V power source (fuse box or direct to battery)
4. Identify good ground point

## Phase 4: Installation (3-4 hours)

### 4.1 Install Power Supply
1. Mount DC-DC converter in protected location
2. Run power wire from 12V source with inline fuse
3. Connect DC-DC converter input to 12V (with fuse!)
4. Adjust DC-DC converter output to exactly 5V
5. Test output voltage before connecting anything else

### 4.2 Run Wiring
1. Route 5V power wires to LED strip locations
2. Route data wires from ESP32 to each LED strip location
3. Use cable ties to secure wires every 6-12 inches
4. Avoid sharp edges that could cut insulation
5. Keep away from exhaust, transmission, moving parts
6. Use grommets when passing through metal panels

### 4.3 Install LED Strips
1. Clean mounting surface with isopropyl alcohol
2. Apply LED strips to prepared locations
3. Additional mounting with cable ties if needed
4. Connect power and data to each strip
5. Apply silicone sealant to all connections
6. Wait for sealant to cure before testing

### 4.4 Install Control Components
1. Mount ESP32 in weatherproof enclosure
2. Install push buttons in accessible location
3. Connect button wires to ESP32 (with labels!)
4. Install optocoupler for brake signal detection
5. Connect to vehicle brake light wire

### 4.5 Make Final Connections
1. Double-check all wiring against WIRING.md
2. Verify all grounds are connected
3. Confirm no shorts with multimeter
4. Connect power last

## Phase 5: Testing & Adjustment (1 hour)

### 5.1 Initial Power-Up
1. Have fire extinguisher ready (safety first!)
2. Turn on power
3. Watch for smoke or overheating (turn off immediately if present)
4. Verify startup animation plays
5. Check all LEDs illuminate correctly

### 5.2 Function Testing
1. Test left turn signal
2. Test right turn signal
3. Test hazard lights
4. Test brake lights (have helper press pedal)
5. Verify running lights

### 5.3 Adjustment
1. Adjust brightness if needed (in config.h)
2. Adjust blink rate if needed (legal requirement: 60-120 blinks/min)
3. Fine-tune animation speed
4. Re-upload sketch if changes made

### 5.4 Road Test
1. Park in safe area
2. Test all functions with vehicle running
3. Walk around vehicle to verify visibility
4. Test with headlights on/off
5. Verify no interference with other electrical systems

## Phase 6: Final Touches (30 minutes)

### 6.1 Secure Everything
1. Add additional cable ties as needed
2. Ensure no loose wires
3. Seal controller enclosure
4. Apply additional weatherproofing to connections

### 6.2 Documentation
1. Take photos of installation
2. Note any modifications made
3. Save customized config.h
4. Label wires for future maintenance

### 6.3 Cleanup
1. Remove temporary wires/materials
2. Clean work area
3. Dispose of waste properly

## Post-Installation

### First Week
- Monitor for any issues
- Check connections periodically
- Watch for overheating
- Verify all functions still work

### Long Term Maintenance
- Inspect connections seasonally
- Check for water intrusion
- Clean LED lenses as needed
- Verify brightness hasn't degraded

## Estimated Time Breakdown

| Phase | Time Required |
|-------|--------------|
| Software Setup | 30 minutes |
| Bench Testing | 1-2 hours |
| Vehicle Prep | 2-3 hours |
| Installation | 3-4 hours |
| Testing | 1 hour |
| Final Touches | 30 minutes |
| **Total** | **8-11 hours** |

Time varies based on experience and vehicle complexity.

## Safety Reminders

- ⚠️ Disconnect vehicle battery before working on electrical system
- ⚠️ Use proper fuses to protect circuits
- ⚠️ Verify all wiring before applying power
- ⚠️ Ensure legal compliance with local vehicle regulations
- ⚠️ Test thoroughly before driving on public roads

## Need Help?

Refer to:
- **WIRING.md** - Detailed wiring diagrams
- **TROUBLESHOOTING.md** - Common issues and solutions
- **PARTS_LIST.md** - Component specifications
- **README.md** - General information

## Legal Compliance Note

Before using on public roads:
- Verify turn signal flash rate complies with regulations (typically 60-120 per minute)
- Ensure colors are legal (amber for turn signals, red for brake)
- Check brightness requirements
- Verify visibility from required distances
- Consult local DMV/equivalent authority

Good luck with your installation! 🚐✨
