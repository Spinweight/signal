# Dynamic LED Lighting System for 97 E150 Van

A dynamic animated LED lighting system for 1997 Ford E150 van using FireBeetle 2 ESP32 (DFR1145) and WS2812B addressable RGB LEDs.

## Features

- 🔄 **Animated Turn Signals**: Sequential LED animation for left and right turn signals
- ⚠️ **Hazard Lights**: Both sides blink together for emergency situations
- 🛑 **Brake Lights**: Bright red brake lights with automatic activation
- 💡 **Running Lights**: Dim tail/marker lights when not signaling
- ⚡ **Startup Animation**: Visual confirmation on system power-up
- 🎨 **Customizable**: Easy-to-configure colors, brightness, and timing

## Hardware Requirements

### Components
- **FireBeetle 2 ESP32** (DFR1145) - Main microcontroller
- **WS2812B LED Strips** - 3 strips (30 LEDs each recommended)
  - 1 strip for left turn signal
  - 1 strip for right turn signal
  - 1 strip for brake/tail lights
- **DC-DC Buck Converter** - 12V to 5V, 5A+ capacity
- **Push Buttons** - 3 buttons for left/right/hazard controls
- **Optocoupler or Relay** - For brake signal detection
- **Wiring & Connectors** - Heat shrink, fuse holder, fuses

### Power Supply
- Vehicle 12V electrical system
- 5V regulated for LEDs and ESP32 (via DC-DC converter)
- Recommended 5A+ capacity for full brightness operation

## Software Requirements

### Arduino IDE Setup
1. Install [Arduino IDE](https://www.arduino.cc/en/software) (version 1.8.x or 2.x)
2. Add ESP32 board support:
   - Go to **File → Preferences**
   - Add to "Additional Board Manager URLs": 
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - Go to **Tools → Board → Boards Manager**
   - Search for "esp32" and install "esp32 by Espressif Systems"

3. Install required libraries:
   - Go to **Sketch → Include Library → Manage Libraries**
   - Search and install **"Adafruit NeoPixel"** by Adafruit

### Board Configuration
- **Board**: "FireBeetle-ESP32" or "ESP32 Dev Module"
- **Upload Speed**: 921600
- **Flash Frequency**: 80MHz
- **Partition Scheme**: Default

## Installation

### 1. Software Setup

1. Clone or download this repository
2. Open `signal.ino` in Arduino IDE
3. Adjust settings in `config.h` if needed (LED count, pins, colors, etc.)
4. Select the correct board and port in Arduino IDE
5. Upload the sketch to your FireBeetle 2 ESP32

### 2. Hardware Setup

See [WIRING.md](WIRING.md) for detailed wiring diagrams and connection instructions.

**Quick Connection Summary:**
- Left turn signal LED strip → GPIO25
- Right turn signal LED strip → GPIO26
- Brake light LED strip → GPIO27
- Left button → GPIO12 (to GND)
- Right button → GPIO13 (to GND)
- Hazard button → GPIO14 (to GND)
- Brake sensor → GPIO32 (via optocoupler from brake light circuit)

### 3. Power Distribution

1. Connect vehicle 12V to DC-DC converter input (through fuse!)
2. Set DC-DC converter output to 5V
3. Connect 5V output to FireBeetle ESP32 VCC
4. Connect 5V to all LED strip power wires
5. Connect all grounds together (common ground)

## Configuration

Edit `config.h` to customize your setup:

```cpp
// Adjust LED count per strip
#define NUM_LEDS_PER_STRIP 30

// Adjust brightness (0-255)
#define BRIGHTNESS 200

// Adjust blink timing (milliseconds)
#define BLINK_INTERVAL 500

// Change colors (RGB hex values)
#define COLOR_AMBER 0xFFB000
#define COLOR_RED 0xFF0000
```

## Usage

### Controls
- **Left Turn Button**: Activate/deactivate left turn signal
- **Right Turn Button**: Activate/deactivate right turn signal
- **Hazard Button**: Activate/deactivate hazard lights (both sides)
- **Brake Pedal**: Automatically activates bright brake lights

### Behavior
- **Turn Signals**: Sequential animation sweeps from inner to outer LED
- **Hazard Lights**: Both sides blink together in sync
- **Brake Lights**: Immediately illuminate to full brightness when brake pressed
- **Running Lights**: Dim tail lights visible when no signals active
- **Startup**: Brief animation sequence confirms system is working

## Testing

Before installing in vehicle:

1. **Bench Test**: Power the system with 12V power supply on workbench
2. **Visual Test**: Verify all LEDs light up correctly
3. **Button Test**: Test each button for proper signal activation
4. **Brake Test**: Verify brake input triggers bright brake lights
5. **Timing Test**: Confirm blink rate is appropriate (~60 blinks/minute)

## Troubleshooting

### LEDs don't light up
- Check 5V power supply voltage
- Verify data wire connections (correct GPIO pins)
- Ensure common ground between ESP32 and LED strips

### Random LED flickering
- Add 330Ω-470Ω resistor between GPIO and LED data wire
- Add 1000µF capacitor across LED strip power supply
- Check for loose connections

### ESP32 keeps resetting
- Power supply insufficient - use higher capacity converter
- Add capacitor (1000µF+) near ESP32 power pins
- Check for short circuits

### Brake lights don't activate
- Verify optocoupler/relay circuit
- Test brake wire voltage with multimeter
- Check GPIO32 pin configuration

## Legal Considerations

⚖️ **Important**: Ensure your LED installation complies with local vehicle lighting regulations:
- Turn signal color (typically amber/yellow)
- Brake light color (red only)
- Visibility requirements
- Flash rate regulations (typically 60-120 flashes/minute)

Check your local Department of Motor Vehicles (DMV) or equivalent authority for specific requirements.

## Safety Notes

- Always use appropriate fuses to protect circuits
- Use proper wire gauge for current capacity
- Waterproof all connections (heat shrink, silicone sealant)
- Secure all components to prevent damage from vibration
- Test thoroughly before driving on public roads

## License

This project is open source. Feel free to modify and adapt for your own use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Credits

Created for 1997 Ford E150 Van LED lighting upgrade using:
- FireBeetle 2 ESP32 (DFR1145) by DFRobot
- WS2812B addressable RGB LEDs
- Adafruit NeoPixel library
