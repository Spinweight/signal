# System Schematic Diagram

## Overall System Architecture

```
                        1997 E150 Van Electrical System
                                    |
                              [12V Battery]
                                    |
                            [5A-10A Fuse]
                                    |
                            +-------+-------+
                            |               |
                     [DC-DC Converter]      |
                      (12V → 5V, 5A)        |
                            |               |
                          [5V]       [Optocoupler]
                            |        (Brake Signal)
          +-----------------+----------------+         |
          |                 |                |         |
    [FireBeetle 2]    [LED Strip 1]   [LED Strip 2]  [LED Strip 3]
      ESP32 DFR1145      (Left)          (Right)       (Brake)
          |                                             
    [Control Buttons]                                  
```

## Detailed Power Distribution

```
Vehicle 12V
    |
    +--[Fuse 5-10A]--+
                     |
            +--------+--------+
            |   DC-DC Conv    |
            | 12V → 5V Output |
            +--------+--------+
                     |
                   [5V]
                     |
         +-----------+-----------+-----------+
         |           |           |           |
    [ESP32 VCC]  [LED1 +5V]  [LED2 +5V]  [LED3 +5V]
         |           |           |           |
    [Bypass Cap] [Filter Cap] [Filter Cap] [Filter Cap]
      100µF       1000µF       1000µF       1000µF
         |           |           |           |
         +===========+===========+===========+
                     |
                [Common GND]
                     |
              [Vehicle Chassis]
```

## FireBeetle 2 ESP32 Pin Connections

```
                    +-------------------+
                    |  FireBeetle 2     |
                    |  ESP32 (DFR1145)  |
                    |                   |
         5V---------|VCC            GND|----------GND (Common)
                    |                   |
  [Left Button]----|GPIO12      GPIO25|----------[LED Strip 1 Data]
 [Right Button]----|GPIO13      GPIO26|----------[LED Strip 2 Data]
[Hazard Button]----|GPIO14      GPIO27|----------[LED Strip 3 Data]
                    |                   |
 [Brake Signal]----|GPIO32            |
 (Optocoupler)      |                   |
                    |             GPIO2 |----------[Onboard LED]
                    |                   |
                    +-------------------+

Note: All buttons use internal pull-up resistors (INPUT_PULLUP)
      Buttons connect to GND when pressed
```

## WS2812B LED Strip Connections

Each LED strip has 3 wires:

```
LED Strip (Left Turn Signal - GPIO25):
    +---------+
    | WS2812B |
    | Strip   |
    +---------+
        |  |  |
       +5V DIN GND
        |   |   |
        |   |   +-------------------[Common GND]
        |   |
        |   +------[330Ω]----------[ESP32 GPIO25]
        |
        +---------------------------[+5V from DC-DC]

LED Strip (Right Turn Signal - GPIO26):
    Same as above, but DIN to GPIO26

LED Strip (Brake/Tail - GPIO27):
    Same as above, but DIN to GPIO27
```

## Button Wiring (with debounce)

```
Left Turn Signal Button:
    
    +3.3V (Internal Pull-up)
       |
       +---[10kΩ]---+
                    |
    [ESP32 GPIO12]--+
                    |
              +-----+-----+
              |  Button   |
              | (Normally |
              |   Open)   |
              +-----------+
                    |
                 [GND]

Optional external capacitor for better debouncing:
    
    GPIO12 ----+----[100nF]---- GND
               |
           [Button]
               |
             [GND]

Same configuration for:
- Right button → GPIO13
- Hazard button → GPIO14
```

## Brake Light Detection Circuit

### Using PC817 Optocoupler (Recommended)

```
Vehicle Brake Light Circuit (12V):
    
    [Brake Light +12V]
            |
            +---[1kΩ]---+
                        |
                    +---+---+
                    |  LED  | PC817 Optocoupler
                    | Anode |
                    +-------+
                    |Cathode|
                    +---+---+
                        |
              [Vehicle GND]


    Transistor Side (ESP32 side):
    
    +5V (or +3.3V)
     |
     +---[10kΩ]---+
                  |
    [GPIO32]------+--------[Collector]
                           |         | PC817
                           |  Photo  |
                           | Transis.|
                           |         |
                  [Emitter]---------[GND]

When brake pressed:
- Optocoupler LED turns on (12V side)
- Photo transistor conducts
- GPIO32 pulled to GND (LOW = brake on)
```

### Alternative: Using Relay Module

```
Vehicle Brake Light:
    
    [+12V when brake pressed]
            |
      +-----+-----+
      | 12V Relay |
      | Module    |
      +-----+-----+
            |
      [Vehicle GND]

    Relay Contacts:
    
    +5V (or 3.3V)
     |
     +---[10kΩ]---+
                  |
    [GPIO32]------+-----[NO Contact]
                        |
                   [COM Contact]
                        |
                      [GND]

When brake pressed:
- Relay energizes
- Contacts close
- GPIO32 pulled to GND (LOW = brake on)
```

## Complete System Wiring Diagram

```
                    VEHICLE ELECTRICAL SYSTEM
    
    +12V Battery---[Fuse]---+
         |                  |
         |           +------+-------+
         |           | DC-DC Conv   |
         |           | 12V → 5V     |
         |           +------+-------+
         |                  |
         |                  +------ +5V Rail
         |                            |
         |                    +-------+-------+-------+
         |                    |       |       |       |
         |             +------+  +----+  +----+  +----+
         |             | ESP32|  |LED1|  |LED2|  |LED3|
         |             +------+  +----+  +----+  +----+
         |                |        |       |       |
         |                |        |       |       |
         |         GPIO25-+--------+       |       |
         |         GPIO26-+----------------+       |
         |         GPIO27-+------------------------+
         |                |
         |         GPIO12-+---[Button 1]---GND
         |         GPIO13-+---[Button 2]---GND
         |         GPIO14-+---[Button 3]---GND
         |                |
         |         GPIO32-+---[Optocoupler]
         |                              |
         |                       [Brake +12V]
         |                              |
         +------------------------------+
                                        |
                              [Common Ground/Chassis]
```

## LED Data Signal Flow

```
Sequential Animation Example (Left Turn):

ESP32 GPIO25 → [330Ω] → LED 1 → LED 2 → LED 3 → ... → LED 30
    |                      ↓       ↓       ↓            ↓
  Signal                 DIN → DOUT → DIN → ... → Last LED
    |
    +--> Data packet: [LED1 color][LED2 color]...[LED30 color]

Timing:
- ESP32 sends 24-bit color data per LED (8-bit R, 8-bit G, 8-bit B)
- Data rate: 800 kHz
- Sequential update creates animation effect
```

## Power Budget Calculation

```
Component Power Requirements:

FireBeetle ESP32:
    Active:     ~250-500mA @ 5V
    WiFi off:   ~150mA @ 5V
    
WS2812B LED (per LED):
    Off:        ~1mA @ 5V
    Full White: ~60mA @ 5V
    Amber:      ~40mA @ 5V
    Red:        ~20mA @ 5V

Example System (3 strips × 30 LEDs = 90 LEDs):

Scenario 1: Turn Signal (30 LEDs amber)
    30 LEDs × 40mA = 1200mA
    ESP32 = 150mA
    Other 60 LEDs dim = 60 × 1mA = 60mA
    Total: ~1.4A

Scenario 2: Hazard (60 LEDs amber)
    60 LEDs × 40mA = 2400mA
    ESP32 = 150mA
    Other 30 LEDs = 30mA
    Total: ~2.6A

Scenario 3: All Brake (30 LEDs red, full bright)
    30 LEDs × 20mA = 600mA
    ESP32 = 150mA
    Other 60 LEDs dim = 60mA
    Total: ~0.8A

Worst Case (all LEDs full white):
    90 LEDs × 60mA = 5400mA
    ESP32 = 500mA
    Total: ~5.9A

Recommended Power Supply: 5A minimum, 6A+ preferred
```

## Grounding Scheme

```
                [Vehicle Chassis Ground]
                         |
            +------------+------------+
            |            |            |
      [DC-DC GND]   [ESP32 GND]  [LED Strips GND]
            |            |            |
            +------------+------------+
                         |
                  [Common Ground Bus]
                  (Star grounding)

Important:
- Single point ground connection to chassis
- Use heavy gauge wire for ground (18 AWG minimum)
- Keep ground paths short
- Avoid ground loops
```

## Protection Components

```
Input Protection:
    12V---[Fuse 5-10A]---[DC-DC Input]

LED Data Line Protection:
    ESP32 GPIO---[330-470Ω]---[LED Strip DIN]

Power Supply Filtering:
    +5V---[1000µF Cap]---GND  (at each LED strip)
    +5V---[100µF Cap]---GND   (at ESP32)

Reverse Polarity Protection:
    Option 1: Use diode on 12V input (adds voltage drop)
    Option 2: Use fuse (will blow if reversed)
    Option 3: Use DC-DC converter with built-in protection
```

## Signal Timing Diagram

```
Turn Signal Blink Pattern (500ms interval):

Time:     0ms        500ms       1000ms      1500ms
          |           |            |           |
Signal:   |████████████|____________|████████████|______
          ON          OFF          ON          OFF

Sequential Animation (50ms per step):

LED1:  █░░░░░░░░░░█░░░░░░░░░░█
LED2:  ░█░░░░░░░░░░█░░░░░░░░░░█
LED3:  ░░█░░░░░░░░░░█░░░░░░░░░░
...    ... (continues for all 30 LEDs)
LED30: ░░░░░░░░░░█░░░░░░░░░░█░

Full cycle: 30 steps × 50ms = 1500ms
Blink rate: 500ms on + 500ms off = 1Hz (60 bpm)
```

## Troubleshooting Test Points

```
Test Points for Multimeter:

TP1: DC-DC Output
    Expected: 5.0V ± 0.25V DC

TP2: ESP32 VCC
    Expected: 5.0V ± 0.25V DC (when powered)

TP3: LED Strip Power (at strip)
    Expected: 4.75V - 5.25V DC (some drop acceptable)

TP4: GPIO Output (when signal active)
    Expected: 3.3V high, 0V low, ~3MHz data pulses

TP5: Button Input (not pressed)
    Expected: 3.3V (pulled high)

TP6: Button Input (pressed)
    Expected: 0V (pulled to ground)

TP7: Brake Signal (brake not pressed)
    Expected: 5V or 3.3V (pulled high)

TP8: Brake Signal (brake pressed)
    Expected: 0V (pulled low via optocoupler)
```

## Notes

- All wire gauges assume runs under 10 feet
- Use heavier gauge for longer runs
- Waterproof all outdoor connections
- Test continuity before applying power
- Measure voltages at multiple points during operation
- Monitor for voltage drop under load
