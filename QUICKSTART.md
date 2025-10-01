# Quick Start Guide

Get your LED matrix animations running in 5 minutes!

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Spinweight/signal.git
cd signal
```

2. No dependencies needed! Uses only Python standard library.

## Run the Demo

See all animations in action:
```bash
python3 led_matrix_animations.py
```

## Try the Examples

See practical use cases:
```bash
python3 examples.py
```

## Your First Animation

Create a file called `my_animation.py`:

```python
from led_matrix_animations import LEDMatrix, TurnSignalAnimation
import time

# Create a 32x8 LED matrix
matrix = LEDMatrix(width=32, height=8)

# Create a turn signal animation
signal = TurnSignalAnimation(matrix, direction="right", speed=2)

# Run the animation
print("Right turn signal active!")
for _ in range(50):
    signal.update()
    matrix.display()
    time.sleep(0.1)
```

Run it:
```bash
python3 my_animation.py
```

## Available Animations

### 1. Turn Signal (Perfect for vehicles!)
```python
from led_matrix_animations import TurnSignalAnimation

# Right turn
right_turn = TurnSignalAnimation(matrix, direction="right", speed=2)

# Left turn
left_turn = TurnSignalAnimation(matrix, direction="left", speed=2)
```

### 2. Fireworks (Celebration mode!)
```python
from led_matrix_animations import FireworksAnimation

fireworks = FireworksAnimation(matrix, num_fireworks=3)

for _ in range(100):
    fireworks.update()
    matrix.display()
    time.sleep(0.1)
```

### 3. Pulse (Dynamic brake lights!)
```python
from led_matrix_animations import PulseAnimation

pulse = PulseAnimation(matrix, intensity=1.0)

# Change intensity dynamically
pulse.set_intensity(0.5)  # Dim
pulse.set_intensity(1.0)  # Bright
```

### 4. Wave (Ambient effects!)
```python
from led_matrix_animations import WaveAnimation

wave = WaveAnimation(matrix, direction="horizontal")
```

### 5. Scrolling Text (Messages!)
```python
from led_matrix_animations import ScrollTextAnimation

text = ScrollTextAnimation(matrix, text="HELLO", speed=1)
```

## Hardware Integration

### Using with Real LED Matrix

Replace the simulator with your hardware driver:

```python
# Instead of:
from led_matrix_animations import LEDMatrix
matrix = LEDMatrix(width=32, height=8)

# Use your hardware:
from your_led_driver import YourMatrix
matrix = YourMatrix(width=32, height=8)

# Make sure your driver has these methods:
# - set_pixel(x, y, brightness)
# - clear()
# - width and height properties
```

### Popular Hardware Options

**Raspberry Pi:**
```bash
pip install rpi-rgb-led-matrix
```

**Arduino:**
Use Adafruit NeoMatrix library

**ESP32:**
Use FastLED library

## Testing

Run the test suite:
```bash
python3 test_animations.py
```

## Next Steps

1. Read [README.md](README.md) for detailed documentation
2. Check [ANIMATIONS.md](ANIMATIONS.md) for animation showcase
3. Explore [examples.py](examples.py) for practical use cases
4. Customize animations for your specific needs

## Common Use Cases

### Vehicle Turn Signals
```python
turn_right = TurnSignalAnimation(matrix, "right", speed=2)
turn_left = TurnSignalAnimation(matrix, "left", speed=2)
```

### Dynamic Brake Lights
```python
brake = PulseAnimation(matrix, intensity=0.5)
# Adjust based on brake pedal pressure
brake.set_intensity(pedal_pressure)
```

### Hazard Lights
```python
# Alternate between left and right
while hazard_active:
    left_turn.update()
    matrix.display()
    time.sleep(0.1)
    right_turn.update()
    matrix.display()
    time.sleep(0.1)
```

### Custom Messages
```python
message = ScrollTextAnimation(matrix, text="VAN SIGNAL")
```

## Troubleshooting

**Problem**: Animations run too fast/slow
**Solution**: Adjust the `time.sleep()` delay or animation `speed` parameter

**Problem**: Display looks wrong
**Solution**: Check matrix dimensions match your hardware (width, height)

**Problem**: Import errors
**Solution**: Make sure you're in the correct directory with the .py files

## Tips

- Start with the demo to see all animations
- Use the test file to verify everything works
- Adjust animation speed to match your display refresh rate
- Combine animations for unique effects
- Create custom animations by extending the Animation class

## Support

- Check the [full documentation](README.md)
- Review [animation examples](examples.py)
- See [visual gallery](ANIMATIONS.md)

Happy animating! 🎉
