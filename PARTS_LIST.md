# Parts List for 97 E150 Van LED Lighting System

## Required Components

### Electronic Components

| Item | Quantity | Specifications | Notes |
|------|----------|---------------|-------|
| FireBeetle 2 ESP32 (DFR1145) | 1 | ESP32-E microcontroller | Main controller |
| WS2812B LED Strip | 3 | 30 LEDs/strip, 60 LEDs/meter | Addressable RGB |
| DC-DC Buck Converter | 1 | 12V to 5V, 5A+ capacity | LM2596 or similar |
| Optocoupler | 1 | PC817 or similar | For brake signal isolation |
| Resistors | 3 | 330Ω-470Ω, 1/4W | For LED data lines |
| Resistor | 1 | 1kΩ, 1/4W | For optocoupler LED |
| Resistor | 1 | 10kΩ, 1/4W | Pull-up for optocoupler |
| Capacitors | 3 | 1000µF, 16V+ | For LED strip power |
| Capacitor | 1 | 100µF, 16V+ | For ESP32 power |
| Push Buttons | 3 | Momentary, SPST | For left/right/hazard |
| Fuse Holder | 1 | Inline blade fuse holder | For 12V input |
| Fuse | 1 | 5A or 10A blade fuse | For overcurrent protection |

### Wiring & Connectors

| Item | Quantity | Specifications | Notes |
|------|----------|---------------|-------|
| Wire (Power) | ~10 feet | 18 AWG, stranded | Red & black for 5V/GND |
| Wire (Data) | ~15 feet | 22-24 AWG, stranded | For data signals |
| Wire (12V Input) | ~5 feet | 16-18 AWG | From vehicle to converter |
| JST Connectors | 6 | 3-pin JST-SM | For LED strip connections |
| Heat Shrink Tubing | Assorted | Various sizes | For insulation |
| Wire Connectors | 10+ | Butt splice or crimp | For secure connections |
| Weatherproof Box | 1 | Small project enclosure | For ESP32 mounting |

### Mounting Hardware

| Item | Quantity | Specifications | Notes |
|------|----------|---------------|-------|
| Cable Ties | 20+ | Various sizes | For securing wiring |
| Adhesive Mounting Tape | 1 roll | 3M VHB or similar | For LED strips |
| Screws/Standoffs | As needed | M3 or similar | For mounting enclosure |
| Silicone Sealant | 1 tube | Clear, automotive grade | For weatherproofing |

## Optional Components

| Item | Purpose | Notes |
|------|---------|-------|
| Potentiometer | Brightness control | 10kΩ linear |
| Switch | Master on/off | SPST toggle switch |
| Additional LEDs | More coverage | Same WS2812B type |
| Terminal Block | Easier wiring | Screw terminals |
| Heatsinks | DC-DC converter cooling | Small aluminum |
| Extra Fuses | Spares | Same rating as main |

## Where to Buy

### Online Retailers
- **Amazon**: Most components available
- **AliExpress**: Good prices, longer shipping
- **DigiKey/Mouser**: Electronic components, fast shipping
- **Adafruit**: Quality LED products and documentation
- **DFRobot**: Official source for FireBeetle 2
- **SparkFun**: Electronics and learning resources

### Local Sources
- **Auto parts stores**: Wire, fuses, connectors
- **Hardware stores**: Mounting supplies, enclosures
- **Electronics stores**: Components, wire

## Cost Estimate

| Category | Estimated Cost |
|----------|---------------|
| FireBeetle ESP32 | $10-15 |
| LED Strips (3x) | $30-45 |
| DC-DC Converter | $5-10 |
| Electronic Components | $10-15 |
| Wiring & Connectors | $15-25 |
| Mounting Hardware | $10-15 |
| **Total Estimate** | **$80-125** |

*Prices are approximate and vary by supplier and region*

## Recommended LED Specifications

### WS2812B LED Strip Options

**Indoor (requires weatherproofing):**
- IP30: No waterproofing, cheapest
- Requires enclosure or silicone coating

**Outdoor (recommended for vehicle):**
- IP65: Silicone coating, splash resistant
- IP67: Silicone sleeve, water resistant (recommended)
- IP68: Fully waterproof, submersible (overkill but most durable)

**Density Options:**
- 30 LEDs/meter: Standard, good for most applications
- 60 LEDs/meter: Denser, smoother animations
- 144 LEDs/meter: Very dense, may require more power

**Strip Length:**
- For turn signals: 0.5-1 meter per side (15-30 LEDs)
- For brake lights: 0.5-1 meter (15-30 LEDs)
- Total needed: 2-3 meters

## Power Supply Specifications

### DC-DC Buck Converter Requirements

**Input:**
- Voltage: 12V (vehicle electrical system)
- Must handle voltage fluctuations (9V-16V typical)

**Output:**
- Voltage: 5V (adjustable)
- Current: 5A minimum, 6A+ recommended
- Voltage regulation: ±2% or better

**Recommended Models:**
- LM2596-based modules (3A, suitable for lower LED count)
- XL4015-based modules (5A, better for full setup)
- MP1584-based modules (3A, very compact)

### Power Calculation Example

For 3 strips × 30 LEDs:
- Per LED: ~60mA at full white brightness
- Total LEDs: 90
- Maximum current: 90 × 0.06A = 5.4A
- ESP32: ~0.5A
- **Total: ~6A peak**

In practice:
- Not all LEDs at full brightness simultaneously
- Amber and red use less power than white
- Typical usage: 2-3A average

## Tools Needed

### Required Tools
- Soldering iron and solder
- Wire strippers
- Wire cutters
- Crimping tool
- Multimeter (voltage/continuity testing)
- Screwdrivers
- Heat gun (for heat shrink)

### Helpful Tools
- Helping hands/PCB holder
- Label maker (for wire identification)
- Hot glue gun (additional strain relief)
- Drill (for mounting holes)
- Fish tape (for running wires)

## Safety Equipment

- Safety glasses
- Wire ties for cable management
- Electrical tape
- Fire extinguisher (when working on vehicle)

## Before You Order

**Measure your vehicle:**
- Distance from mounting location to controller
- Length needed for each LED strip
- Wire routing path

**Consider:**
- Where will you mount the ESP32 controller?
- How will you run wires through vehicle body?
- Where will buttons be located?
- Power source location (fuse box or direct to battery?)

**Check compatibility:**
- Verify LED strip voltage (must be 5V)
- Confirm WS2812B type (not WS2811 or others)
- Match wire gauges to your current requirements
