# Wiring Diagram for 97 E150 Van LED Lighting System

## Components Required

### Main Components
- 1x FireBeetle 2 ESP32 (DFR1145)
- 3x WS2812B LED Strips (30 LEDs each recommended)
- 1x 12V to 5V DC-DC converter (5A or higher recommended)
- 3x Push buttons (for left/right/hazard signals)
- 1x Relay or optocoupler for brake signal detection
- Wire connectors and heat shrink tubing
- Fuse holder and appropriate fuses

### Power Supply
- Vehicle 12V system
- 5V regulated power for LED strips and ESP32

## Wiring Connections

### FireBeetle 2 ESP32 to LED Strips

```
FireBeetle 2          WS2812B LED Strip
============          =================
GPIO25 (Pin)    -->   Left Turn Signal DIN (Data In)
GPIO26 (Pin)    -->   Right Turn Signal DIN (Data In)
GPIO27 (Pin)    -->   Brake/Tail Light DIN (Data In)
GND             -->   All LED strips GND (common ground)
```

### Input Buttons/Switches

```
FireBeetle 2          Button/Switch
============          ==============
GPIO12 (Pin)    -->   Left Turn Button (other side to GND)
GPIO13 (Pin)    -->   Right Turn Button (other side to GND)
GPIO14 (Pin)    -->   Hazard Button (other side to GND)
GPIO32 (Pin)    -->   Brake Signal (via relay/optocoupler from brake light circuit)
```

Note: All buttons use internal pull-up resistors (INPUT_PULLUP mode)

### Power Distribution

```
Vehicle 12V System
      |
      |--- Fuse (5A-10A depending on LED count)
      |
      v
  DC-DC Converter (12V to 5V)
      |
      |--- 5V Out --> FireBeetle ESP32 VCC
      |
      |--- 5V Out --> LED Strip 1 (+5V)
      |
      |--- 5V Out --> LED Strip 2 (+5V)
      |
      |--- 5V Out --> LED Strip 3 (+5V)
      |
      |--- GND --> Common Ground (to all components)
```

## Detailed Connection Instructions

### 1. LED Strip Installation

Each WS2812B LED strip has three wires:
- **Red (+5V)**: Connect to 5V power supply
- **White/Green (Data)**: Connect to corresponding GPIO pin on FireBeetle
- **Black (GND)**: Connect to common ground

**Left Turn Signal Strip:**
- Data wire → GPIO25
- Power (+5V) → 5V supply
- Ground → Common GND

**Right Turn Signal Strip:**
- Data wire → GPIO26
- Power (+5V) → 5V supply
- Ground → Common GND

**Brake/Tail Light Strip:**
- Data wire → GPIO27
- Power (+5V) → 5V supply
- Ground → Common GND

### 2. Button/Switch Connections

**Left Turn Signal Button:**
- One side → GPIO12
- Other side → GND
- (Internal pull-up resistor is enabled in software)

**Right Turn Signal Button:**
- One side → GPIO13
- Other side → GND

**Hazard Button:**
- One side → GPIO14
- Other side → GND

### 3. Brake Light Detection

The brake signal needs to be safely interfaced with the ESP32. Use one of these methods:

**Option A: Optocoupler (Recommended)**
```
Vehicle Brake Light (+12V when brake pressed)
      |
      |--- 1kΩ Resistor
      |
      v
  Optocoupler LED side (+)
      |
      |--- Optocoupler LED side (-)
      |
      v
  Vehicle GND

Optocoupler transistor side:
  Collector --> +5V (through 10kΩ pull-up)
  Emitter   --> GND
  Output    --> GPIO32 on FireBeetle
```

**Option B: Relay Module**
Use a 12V relay module with:
- Coil connected to vehicle brake light circuit
- NO (Normally Open) contact to pull GPIO32 to GND when activated
- 10kΩ pull-up resistor from GPIO32 to 3.3V

### 4. Power Supply Setup

**DC-DC Converter Connection:**
1. Input side:
   - Connect (+) to vehicle 12V through fuse
   - Connect (-) to vehicle chassis ground

2. Output side:
   - Set output voltage to 5V (adjust potentiometer if needed)
   - Connect 5V (+) to FireBeetle VCC pin
   - Connect 5V (+) to each LED strip's power wire
   - Connect GND (-) to common ground bus

**Important:** Use adequate wire gauge for LED power:
- 18 AWG or thicker for power distribution
- Ensure common ground between all components

### 5. Mounting Locations

**Suggested mounting for 97 E150 Van:**

- **Left LED Strip**: Inside left rear light housing or along left rear quarter panel
- **Right LED Strip**: Inside right rear light housing or along right rear quarter panel  
- **Brake LED Strip**: Center rear, above or below license plate, or inside center brake light housing
- **FireBeetle ESP32**: Inside vehicle near rear, protected from moisture (behind interior panel)
- **Buttons/Switches**: Integrate with steering column or dashboard controls, or use separate switch panel

## Power Calculations

**Power Requirements:**
- Each WS2812B LED: ~60mA at full white brightness
- 30 LEDs per strip: ~1.8A per strip at full brightness
- 3 strips total: ~5.4A maximum (worst case)
- FireBeetle ESP32: ~500mA typical

**Recommended Power Supply:**
- DC-DC converter rated for at least 5A continuous (6A+ recommended for safety margin)
- Use proper fusing (5-10A fuse on 12V side)

## Safety Considerations

1. **Fusing**: Always use appropriate fuses to protect the circuit
2. **Wire Gauge**: Use proper wire gauge for current capacity
3. **Waterproofing**: Protect all connections from moisture (use heat shrink, silicone, or IP67 connectors)
4. **Mounting**: Secure all components to prevent rattling or disconnection
5. **Testing**: Test all functions before final installation
6. **Legal Compliance**: Ensure LED colors and positioning comply with local vehicle lighting regulations

## Testing Procedure

Before final installation:

1. **Bench Test**: Connect everything on a workbench with 12V power supply
2. **Test Startup**: Verify startup animation plays
3. **Test Turn Signals**: Press left/right buttons, verify sequential animation
4. **Test Hazards**: Press hazard button, verify both sides blink
5. **Test Brake**: Activate brake input, verify brake lights illuminate brightly
6. **Test Running Lights**: With no signals active, verify dim tail lights
7. **Load Test**: Run all LEDs for 10+ minutes to check for overheating

## Troubleshooting

**LEDs don't light up:**
- Check power supply voltage (should be 5V)
- Verify data wire connections
- Check common ground connection

**Erratic LED behavior:**
- Add 330Ω-470Ω resistor between GPIO pin and LED strip data wire
- Add 1000µF capacitor across LED strip power supply
- Shorten data wire length if possible

**ESP32 keeps resetting:**
- Insufficient power supply capacity
- Add larger capacitor (1000µF or more) near ESP32 power pins

**Brake signal doesn't detect:**
- Verify optocoupler/relay wiring
- Test brake signal voltage with multimeter
- Check GPIO32 configuration
