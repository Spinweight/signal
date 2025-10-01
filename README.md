# signal
Turn signals for Van

## LED Matrix Animations

This repository contains a collection of LED matrix animations suitable for vehicle turn signals and displays. The animations include planned patterns (like turn signals), dynamic effects, and eye-catching displays like fireworks.

## Features

### Planned Animations
- **Turn Signal Animation**: Classic arrow-style turn indicators
  - Left and right directional arrows
  - Progressive movement effect
  - Adjustable speed

### Dynamic Animations
- **Pulse Animation**: Responsive pulsing effect with adjustable intensity
- **Wave Animation**: Smooth wave motion (horizontal or vertical)
- **Scrolling Text**: Display custom text messages

### Special Effects
- **Fireworks Animation**: Particle-based fireworks with realistic physics
  - Multiple concurrent fireworks
  - Gravity and particle decay effects
  - Random launch patterns

## Installation

No external dependencies required for the basic simulator! The code uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/Spinweight/signal.git
cd signal

# Run the demo
python3 led_matrix_animations.py
```

## Usage

### Quick Demo

Run all animations with the built-in demo:

```bash
python3 led_matrix_animations.py
```

### Using Individual Animations

```python
from led_matrix_animations import LEDMatrix, TurnSignalAnimation, FireworksAnimation

# Create a 32x8 LED matrix
matrix = LEDMatrix(width=32, height=8)

# Create a right turn signal
turn_signal = TurnSignalAnimation(matrix, direction="right", speed=2)

# Run animation loop
for _ in range(50):
    turn_signal.update()
    matrix.display()
    # In real hardware, replace display() with your LED driver update
```

### Animation Examples

#### Turn Signal (Planned Animation)
```python
from led_matrix_animations import LEDMatrix, TurnSignalAnimation

matrix = LEDMatrix(width=32, height=8)

# Right turn signal
right_turn = TurnSignalAnimation(matrix, direction="right", speed=2)

# Left turn signal  
left_turn = TurnSignalAnimation(matrix, direction="left", speed=2)
```

#### Dynamic Pulse Effect
```python
from led_matrix_animations import LEDMatrix, PulseAnimation

matrix = LEDMatrix(width=32, height=8)
pulse = PulseAnimation(matrix, intensity=1.0)

# You can dynamically adjust intensity
pulse.set_intensity(0.5)  # Dim the pulse
pulse.set_intensity(1.0)  # Full brightness
```

#### Fireworks Display
```python
from led_matrix_animations import LEDMatrix, FireworksAnimation

matrix = LEDMatrix(width=32, height=8)
fireworks = FireworksAnimation(matrix, num_fireworks=3)

# Run the animation
for _ in range(100):
    fireworks.update()
    matrix.display()
```

## Hardware Integration

The `LEDMatrix` class is a simulator for development and testing. To use with real hardware:

1. Replace the `LEDMatrix` class with your hardware driver
2. Ensure your driver has similar methods: `set_pixel(x, y, brightness)`, `clear()`, etc.
3. Common hardware options:
   - **Raspberry Pi**: Use `rpi-rgb-led-matrix` library
   - **Arduino**: Use `Adafruit_NeoMatrix` or similar
   - **ESP32**: Use `FastLED` library

### Example Hardware Integration (Raspberry Pi)

```python
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from led_matrix_animations import TurnSignalAnimation

# Configure hardware matrix
options = RGBMatrixOptions()
options.rows = 8
options.cols = 32
hardware_matrix = RGBMatrix(options=options)

# Wrap it to work with our animations
class HardwareMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = matrix.width
        self.height = matrix.height
    
    def set_pixel(self, x, y, value):
        self.matrix.SetPixel(x, y, value, value, value)
    
    def clear(self):
        self.matrix.Clear()

# Use with animation
hw_matrix = HardwareMatrix(hardware_matrix)
animation = TurnSignalAnimation(hw_matrix, direction="right")
```

## Animation Classes

### TurnSignalAnimation
Progressive arrow animation for turn signals.
- `direction`: "left" or "right"
- `speed`: Animation speed (lower = faster)

### PulseAnimation
Pulsing brightness effect that can respond to external input.
- `intensity`: Pulse strength (0.0 to 1.0)
- Dynamic method: `set_intensity(intensity)`

### WaveAnimation
Sinusoidal wave traveling across the display.
- `direction`: "horizontal" or "vertical"

### FireworksAnimation
Particle-based fireworks simulation.
- `num_fireworks`: Maximum concurrent fireworks

### ScrollTextAnimation
Scrolling text display.
- `text`: Text to display (uppercase recommended)
- `speed`: Scroll speed

## Testing

Run the test suite:

```bash
python3 test_animations.py
```

## Customization

All animations inherit from the base `Animation` class. Create custom animations by:

1. Extending the `Animation` class
2. Implementing the `update()` method
3. Optionally override `reset()` for animation restart logic

Example:
```python
from led_matrix_animations import Animation, LEDMatrix

class CustomAnimation(Animation):
    def __init__(self, matrix):
        super().__init__(matrix)
        # Your initialization
    
    def update(self):
        self.matrix.clear()
        # Your animation logic
        self.frame += 1
        return True
```

## License

MIT License - Feel free to use in your projects!

## Contributing

Contributions welcome! Feel free to submit pull requests with new animations or improvements.
