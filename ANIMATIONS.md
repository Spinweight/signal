# LED Matrix Animation Gallery

This document showcases the available animations with visual examples.

## 1. Turn Signal Animation (Planned Animation)

The turn signal animation creates a progressive arrow effect that moves across the display. This is ideal for vehicle turn indicators.

### Features:
- Directional arrows (left or right)
- Progressive build-up effect
- Adjustable speed
- Clear visual indication

### Visual Pattern (Right Turn):
```
Frame 1:    Frame 2:    Frame 3:    Frame 4:
            
    |           |           |           |
    |           |         █ |         █ |
    █           █        █  |        █  |
    |           |      ███  |       █   |
    |           |█        █ |     ████  |
                          █ |       █   |
                          █ |        █  |
                            |         █ |
```

### Use Cases:
- Turn signal indicators
- Directional navigation cues
- Progress indicators

---

## 2. Pulse Animation (Dynamic Animation)

A pulsing brightness effect that can respond to input intensity. Perfect for brake lights or attention-grabbing displays.

### Features:
- Smooth sine wave brightness control
- Adjustable intensity (0.0 to 1.0)
- Dynamic response to input
- Expanding/contracting pattern

### Visual Pattern:
```
Dim:          Medium:       Bright:       Medium:
              
 . . . .      o o o o      █ █ █ █      o o o o
 . . . .      o o o o      █ █ █ █      o o o o
 . . . .      o o o o      █ █ █ █      o o o o
```

### Use Cases:
- Dynamic brake lights (intensity based on brake pressure)
- Heartbeat/status indicators
- Attention-grabbing effects

---

## 3. Wave Animation (Dynamic Animation)

A sinusoidal wave that travels across the display, creating a smooth flowing effect.

### Features:
- Horizontal or vertical wave motion
- Continuous smooth motion
- Adjustable wave parameters

### Visual Pattern (Horizontal):
```
Frame 1:       Frame 2:       Frame 3:
               
    █              █               █
  █   █          █   █           █   █
█       █      █       █       █       █
  █   █          █   █           █   █
    █              █               █
```

### Use Cases:
- Ambient lighting effects
- Status indicators
- Visual feedback for audio/sensor input

---

## 4. Fireworks Animation (Special Effects)

A particle-based fireworks simulation with realistic physics including gravity and decay.

### Features:
- Multiple concurrent fireworks
- Particle-based explosions
- Gravity simulation
- Trail effects
- Random launch patterns

### Visual Pattern:
```
Launch:        Explosion:     Fade:          Next:

               . █ o O █ .
                O █ █ O                      .
    █            █ █ █         . o .         █
    █            o O o           .           o
    █          . o . o .                   . █ .
               .   .   .                     o
```

### Use Cases:
- Celebration displays
- Special event notifications
- Eye-catching demonstrations
- Entertainment mode

---

## 5. Scrolling Text Animation (Planned Animation)

Displays text that scrolls horizontally across the display.

### Features:
- Custom text messages
- Adjustable scroll speed
- 5x5 bitmap font
- Supports uppercase letters

### Visual Pattern:
```
Frame 1:       Frame 2:       Frame 3:
               
  █ █ █ █      █ █ █ █       █ █ █ █
  █            █             █
  █ █ █ █       █ █ █ █       █ █ █ █
  █                █                 █
  █ █ █ █      █ █ █ █       █ █ █ █
```

### Use Cases:
- Custom message display
- Status text
- Vehicle identification
- Event announcements

---

## Animation Comparison

| Animation Type | Category | Complexity | CPU Usage | Best For |
|---------------|----------|------------|-----------|----------|
| Turn Signal | Planned | Low | Low | Directional indicators |
| Pulse | Dynamic | Low | Low | Status/intensity display |
| Wave | Dynamic | Medium | Medium | Ambient effects |
| Fireworks | Special | High | High | Entertainment/celebration |
| Scrolling Text | Planned | Medium | Low | Information display |

---

## Implementation Notes

### Performance Considerations

1. **Turn Signal**: Minimal CPU usage, suitable for continuous operation
2. **Pulse**: Very efficient, can run alongside other animations
3. **Wave**: Moderate CPU for sine calculations, acceptable for continuous use
4. **Fireworks**: Highest CPU due to particle simulation, best for occasional use
5. **Scrolling Text**: Low CPU, minimal memory for font data

### Hardware Recommendations

For a **32x8 LED matrix** (as demonstrated):
- **Microcontroller**: ESP32, Raspberry Pi, or Arduino Mega
- **LED Type**: WS2812B (NeoPixel), APA102, or similar
- **Power**: 5V, 2-4A depending on brightness
- **Refresh Rate**: 30-60 FPS recommended

### Customization Tips

1. **Adjust Speed**: Modify the `speed` parameter or frame skip logic
2. **Change Colors**: Add RGB support by modifying `set_pixel()` calls
3. **Combine Animations**: Layer multiple animations with alpha blending
4. **Add Interactivity**: Connect to sensors or input devices
5. **Create Patterns**: Mix animation primitives for unique effects

---

## Quick Start Examples

### Basic Turn Signal
```python
matrix = LEDMatrix(32, 8)
turn = TurnSignalAnimation(matrix, direction="right", speed=2)

while True:
    turn.update()
    matrix.display()  # Replace with hardware update
    time.sleep(0.05)
```

### Dynamic Brake Light
```python
matrix = LEDMatrix(32, 8)
brake = PulseAnimation(matrix, intensity=0.5)

# React to brake pedal pressure (0.0 to 1.0)
brake.set_intensity(brake_pressure)
brake.update()
```

### Celebration Mode
```python
matrix = LEDMatrix(32, 8)
party = FireworksAnimation(matrix, num_fireworks=3)

for _ in range(100):
    party.update()
    matrix.display()
    time.sleep(0.1)
```

---

## Future Animation Ideas

Potential additions for the library:

1. **Knight Rider Effect**: Scanning LED pattern
2. **Rainbow Cycle**: Color cycling effect
3. **Matrix Rain**: Digital rain effect
4. **Sparkle**: Random twinkling effect
5. **Chase**: Sequential LED chase pattern
6. **Breathe**: Smooth fade in/out
7. **Strobe**: High-intensity flash pattern
8. **Ripple**: Water ripple effect from center
9. **Snake**: Moving line pattern
10. **Plasma**: Smooth plasma effect

---

## Resources

- [Main Implementation](led_matrix_animations.py)
- [Usage Examples](examples.py)
- [Test Suite](test_animations.py)
- [README](README.md)

## License

MIT License - Free to use and modify for your projects!
