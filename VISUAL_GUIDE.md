# Visual Guide

Visual representation of how the LED lighting system works on your van.

## Van Rear View

```
                    1997 Ford E150 Van (Rear View)
                    
         ============================================
         |                                          |
         |    [Roof]                                |
         |                                          |
         |                                          |
         |    +-----------[Cargo Door]----------+   |
         |    |                                 |   |
         |    |                                 |   |
         |    |    [Rear Window]                |   |
         |    |                                 |   |
         |    +---------------------------------+   |
         |                                          |
         |    [License Plate Area]                  |
         |    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               |
         |     ← Brake LED Strip                    |
         |                                          |
    +----+------+                        +----------+----+
    |    LED    |                        |    LED       |
    |   Strip   |                        |   Strip      |
    | (Left     |                        | (Right       |
    |  Turn)    |                        |  Turn)       |
    |    ▓▓     |                        |     ▓▓       |
    |    ▓▓     |                        |     ▓▓       |
    |    ▓▓     |  [Rear Bumper]         |     ▓▓       |
    +----+------+                        +----------+----+
    
    Legend:
    ▓ = LED segments (30 LEDs per strip)
```

## LED Animation Patterns

### Left Turn Signal Animation

```
Sequential Animation (sweeps outward):

Time:  0ms     100ms    200ms    300ms    400ms    500ms
       |        |        |        |        |        |
       █        ██       ███      ████     █████    [OFF]
       ▓        ▓▓       ▓▓▓      ▓▓▓▓     ▓▓▓▓▓    [OFF]
       
Then repeats...

Visual representation of left turn signal:
    
    Interior ←──────────────────── Exterior
    (near van center)              (corner)
    
    [Step 1]  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    [Step 2]  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    [Step 3]  ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    [Step 4]  ████░░░░░░░░░░░░░░░░░░░░░░░░░░░
    [Step 5]  █████░░░░░░░░░░░░░░░░░░░░░░░░░░
    ...       (continues to edge)
    [Step 30] ██████████████████████████████
    [Repeat]  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ (OFF)
```

### Right Turn Signal Animation

```
Same as left but on right side:

    Exterior ──────────────────────→ Interior
    (corner)                         (near van center)
    
    [Step 1]  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    [Step 2]  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    [Step 3]  ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ...       (continues)
    [Step 30] ██████████████████████████████
```

### Hazard Lights

```
Both sides animate simultaneously:

    LEFT                                    RIGHT
    █░░░░░░░░░░░░░░                        ░░░░░░░░░░░░░░█
    ██░░░░░░░░░░░░                          ░░░░░░░░░░░░██
    ███░░░░░░░░░░░                          ░░░░░░░░░░░███
    ████░░░░░░░░░░                          ░░░░░░░░░░████
    █████░░░░░░░░░                          ░░░░░░░░░█████
    ...                                             ...
    ██████████████                          ██████████████
    [OFF]                                   [OFF]
```

### Brake Lights

```
Solid illumination across brake strip:

    Normal (Running lights) - Dim:
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    (Brightness: 30/255)
    
    Brake Pressed - Bright:
    ████████████████████████████
    (Brightness: 255/255)
```

## Color Indicators

```
Color Key:
    🟠 Amber (#FFB000) - Turn signals
    🔴 Red (#FF0000) - Brake/tail lights
    ⚫ Off (dim) - Running lights mode
    ⚪ Off (completely) - Signal off
```

## Startup Animation Sequence

```
System Power-On Sequence:

[Step 1] Sweep across all strips (150ms each LED)
    Left:   █░░░░░░░░░
    Right:  █░░░░░░░░░
    Brake:  █░░░░░░░░░
    
    Left:   ██░░░░░░░░
    Right:  ██░░░░░░░░
    Brake:  ██░░░░░░░░
    
    ... continues to end

[Step 2] Brief pause (200ms)
    All OFF

[Step 3] Quick flash (100ms)
    Left:   ██████████ (Amber)
    Right:  ██████████ (Amber)
    Brake:  ██████████ (Red)

[Step 4] Return to normal operation
    Running lights mode or off
```

## LED Brightness Levels

```
Visual brightness comparison:

Full Brightness (255):     ████████████  100%
Brake Light (255):         ████████████  100%
Turn Signal (200):         ██████████░░   80%
Running Light (30):        ███░░░░░░░░░   12%
Off (0):                   ░░░░░░░░░░░░    0%
```

## Mounting Locations

```
Recommended LED Strip Placement:

Rear Quarter Panel (Side View):
    
    ╔════════════════════╗
    ║ Van Body           ║
    ║                    ║
    ║  +--------------+  ║
    ║  | Tail Light   |  ║
    ║  | Housing      |  ║
    ║  |              |  ║
    ║  | [LED STRIP]  |  ║ ← Mount inside existing housing
    ║  | mounted      |  ║    or along edge
    ║  | vertically   |  ║
    ║  +--------------+  ║
    ║                    ║
    ╚════════════════════╝
    
Alternative: Along bumper edge
    ════[LED STRIP]════════════
    
Alternative: Under body (ground effects style)
         Van Body
    ___________________
    [  [LED STRIP]   ]  ← Mounted underneath
```

## Control Panel Layout

```
Suggested button placement (dashboard or steering column):

    +---------------------------+
    |  Turn Signal Controls     |
    +---------------------------+
    |                           |
    |   [←]    [⚠]    [→]      |
    |   LEFT  HAZARD  RIGHT     |
    |                           |
    +---------------------------+
    
    Where:
    [←] = Left turn signal button
    [⚠] = Hazard lights button  
    [→] = Right turn signal button
```

## System Components Layout

```
Under-hood / Interior mounting:

                    [Van Interior]
                         |
            +------------+------------+
            |                         |
    [Battery 12V] ←─── [Fuse] ───→ [DC-DC]
                                     5V ↓
                                   [ESP32]
                                      |
                    +-----------------+-----------------+
                    |                 |                 |
              [Left Strip]      [Right Strip]     [Brake Strip]
                    |                 |                 |
               (GPIO25)           (GPIO26)          (GPIO27)
```

## Power Flow Diagram

```
    12V Battery
        ║
        ╠══ [Fuse 5-10A]
        ║
        ╠══ [DC-DC Converter]
        ║      12V → 5V
        ║
    5V Output
        ║
        ╠══════════════════╦══════════════════╦══════════════════╗
        ║                  ║                  ║                  ║
    [ESP32]           [LED Strip 1]     [LED Strip 2]     [LED Strip 3]
    250-500mA          0.6-1.8A           0.6-1.8A          0.6-1.8A
        ║                  ║                  ║                  ║
        ╚══════════════════╩══════════════════╩══════════════════╝
                                  ║
                            [Common Ground]
                                  ║
                           [Vehicle Chassis]
```

## Size Reference

```
FireBeetle 2 ESP32 (DFR1145):
    +------------------+
    |                  |
    |  ┌────────────┐  |
    |  │   ESP32    │  |  ~58mm x 30mm
    |  │    Chip    │  |  (~2.3" x 1.2")
    |  └────────────┘  |
    |   ○○○○○○○○○○○○  | ← GPIO Pins
    +------------------+

LED Strip (30 LEDs, 60 LEDs/meter):
    ████████████████████████████  500mm (0.5 meter)
    30 LEDs @ 16.67mm spacing     (~19.7 inches)

LED Strip (30 LEDs, 30 LEDs/meter):
    ████████████████████████████  1000mm (1 meter)
    30 LEDs @ 33.33mm spacing     (~39.4 inches)
```

## Expected Results

### Daytime Operation
- Turn signals clearly visible in daylight
- Amber color distinguishable from brake lights
- Sequential animation catches attention

### Nighttime Operation  
- Bright enough to be seen from 500+ feet
- No glare to driver or other vehicles
- Clear distinction between signal types

### In Rain/Fog
- IP67 rated strips maintain visibility
- Waterproof connections prevent shorts
- Brightness sufficient for poor visibility conditions

## Real-World Example Scenarios

### Scenario 1: Left Turn
```
Driver presses left turn button
    ↓
Left LED strip animates (amber, sequential)
    ↓
Right strip shows dim running light (amber, dim)
    ↓
Brake strip shows tail light (red, dim)
    ↓
Driver releases button after turn
    ↓
System returns to running lights
```

### Scenario 2: Emergency Stop
```
Driver hits brake pedal
    ↓
Brake sensor activates (GPIO32 → LOW)
    ↓
Brake LED strip → BRIGHT RED (255/255)
    ↓
Turn signals continue if active
    ↓
Driver releases brake
    ↓
Brake strip → dim tail light (30/255)
```

### Scenario 3: Hazard Warning
```
Driver presses hazard button
    ↓
BOTH turn signal strips animate (amber)
    ↓
Synchronized blinking at 60 bpm
    ↓
Brake lights continue to function normally
    ↓
Driver presses hazard button again to cancel
    ↓
System returns to running lights
```

## Tips for Best Visual Effect

1. **LED Density**: 60 LEDs/meter for smoother animation
2. **Diffusion**: Use frosted cover or diffuser for even glow
3. **Brightness**: Adjust based on ambient light (use potentiometer)
4. **Animation Speed**: 50ms per step for smooth motion
5. **Color Choice**: Stick to legal colors (amber/red)

## Professional Installation Tips

- Mount strips parallel to vehicle lines for clean look
- Hide wiring in existing channels
- Use professional-grade connectors
- Apply UV-resistant clear coat over outdoor connections
- Label all wires for future maintenance

This visual guide should help you understand what the final system will look like and how it operates!
