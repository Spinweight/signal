"""
LED Matrix Animation Library
Provides various animation patterns for LED matrices including turn signals, 
dynamic effects, and fireworks displays.
"""

import time
import math
import random
from typing import List, Tuple, Callable


class LEDMatrix:
    """Simulates an LED matrix for animation testing and development."""
    
    def __init__(self, width: int = 32, height: int = 8):
        """
        Initialize LED matrix.
        
        Args:
            width: Matrix width in pixels
            height: Matrix height in pixels
        """
        self.width = width
        self.height = height
        self.buffer = [[0 for _ in range(width)] for _ in range(height)]
    
    def clear(self):
        """Clear the display buffer."""
        self.buffer = [[0 for _ in range(self.width)] for _ in range(self.height)]
    
    def set_pixel(self, x: int, y: int, value: int = 1):
        """Set a pixel value (0=off, 1-255=brightness)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = max(0, min(255, value))
    
    def get_pixel(self, x: int, y: int) -> int:
        """Get a pixel value."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.buffer[y][x]
        return 0
    
    def display(self):
        """Print the current buffer to console for visualization."""
        print("\n" + "=" * (self.width + 2))
        for row in self.buffer:
            line = "|"
            for pixel in row:
                if pixel == 0:
                    line += " "
                elif pixel < 64:
                    line += "."
                elif pixel < 128:
                    line += "o"
                elif pixel < 192:
                    line += "O"
                else:
                    line += "█"
            line += "|"
            print(line)
        print("=" * (self.width + 2))


class Animation:
    """Base animation class."""
    
    def __init__(self, matrix: LEDMatrix):
        """Initialize animation with a matrix."""
        self.matrix = matrix
        self.frame = 0
    
    def update(self) -> bool:
        """
        Update animation to next frame.
        
        Returns:
            True if animation should continue, False if complete
        """
        self.frame += 1
        return True
    
    def reset(self):
        """Reset animation to initial state."""
        self.frame = 0
        self.matrix.clear()


class TurnSignalAnimation(Animation):
    """Planned animation: Classic turn signal pattern."""
    
    def __init__(self, matrix: LEDMatrix, direction: str = "right", speed: int = 3):
        """
        Initialize turn signal animation.
        
        Args:
            matrix: LED matrix to draw on
            direction: "left" or "right"
            speed: Animation speed (lower = faster)
        """
        super().__init__(matrix)
        self.direction = direction
        self.speed = speed
        self.max_width = matrix.width // 2
    
    def update(self) -> bool:
        """Draw progressive arrow pattern."""
        self.matrix.clear()
        
        # Calculate current progress (0 to max_width)
        progress = (self.frame // self.speed) % (self.max_width + 5)
        
        if progress > self.max_width:
            # Pause between cycles
            return True
        
        # Draw arrow pattern
        mid_y = self.matrix.height // 2
        
        if self.direction == "right":
            # Draw arrow pointing right
            for i in range(progress + 1):
                # Horizontal line
                self.matrix.set_pixel(i, mid_y, 255)
                
                # Arrow head
                if i == progress:
                    for offset in range(1, min(4, mid_y + 1)):
                        if mid_y - offset >= 0:
                            self.matrix.set_pixel(i - offset, mid_y - offset, 200)
                        if mid_y + offset < self.matrix.height:
                            self.matrix.set_pixel(i - offset, mid_y + offset, 200)
        else:
            # Draw arrow pointing left
            start_x = self.matrix.width - 1
            for i in range(progress + 1):
                # Horizontal line
                self.matrix.set_pixel(start_x - i, mid_y, 255)
                
                # Arrow head
                if i == progress:
                    for offset in range(1, min(4, mid_y + 1)):
                        if mid_y - offset >= 0:
                            self.matrix.set_pixel(start_x - i + offset, mid_y - offset, 200)
                        if mid_y + offset < self.matrix.height:
                            self.matrix.set_pixel(start_x - i + offset, mid_y + offset, 200)
        
        self.frame += 1
        return True


class PulseAnimation(Animation):
    """Dynamic animation: Pulsing effect responding to input."""
    
    def __init__(self, matrix: LEDMatrix, intensity: float = 1.0):
        """
        Initialize pulse animation.
        
        Args:
            matrix: LED matrix to draw on
            intensity: Pulse intensity (0.0 to 1.0)
        """
        super().__init__(matrix)
        self.intensity = intensity
    
    def update(self) -> bool:
        """Create pulsing wave effect."""
        self.matrix.clear()
        
        # Calculate pulse brightness using sine wave
        brightness = int((math.sin(self.frame * 0.2) + 1) * 127.5 * self.intensity)
        
        # Draw expanding circles or rectangles
        mid_x = self.matrix.width // 2
        mid_y = self.matrix.height // 2
        
        radius = int((self.frame % 30) / 3)
        
        # Draw filled rectangle growing from center
        for y in range(self.matrix.height):
            for x in range(self.matrix.width):
                dist = max(abs(x - mid_x), abs(y - mid_y))
                if dist <= radius:
                    # Fade based on distance
                    fade = 1.0 - (dist / (radius + 1))
                    self.matrix.set_pixel(x, y, int(brightness * fade))
        
        self.frame += 1
        return True
    
    def set_intensity(self, intensity: float):
        """Dynamically adjust intensity."""
        self.intensity = max(0.0, min(1.0, intensity))


class WaveAnimation(Animation):
    """Dynamic animation: Wave effect across the matrix."""
    
    def __init__(self, matrix: LEDMatrix, direction: str = "horizontal"):
        """
        Initialize wave animation.
        
        Args:
            matrix: LED matrix to draw on
            direction: "horizontal" or "vertical"
        """
        super().__init__(matrix)
        self.direction = direction
    
    def update(self) -> bool:
        """Create traveling wave effect."""
        self.matrix.clear()
        
        if self.direction == "horizontal":
            # Horizontal wave
            for x in range(self.matrix.width):
                # Calculate wave height
                wave_y = math.sin((x + self.frame) * 0.3) * (self.matrix.height / 4)
                center_y = self.matrix.height / 2
                
                # Draw vertical line at this x position
                pixel_y = int(center_y + wave_y)
                for dy in range(-1, 2):
                    y = pixel_y + dy
                    if 0 <= y < self.matrix.height:
                        brightness = 255 - abs(dy) * 80
                        self.matrix.set_pixel(x, y, brightness)
        else:
            # Vertical wave
            for y in range(self.matrix.height):
                # Calculate wave position
                wave_x = math.sin((y + self.frame) * 0.3) * (self.matrix.width / 4)
                center_x = self.matrix.width / 2
                
                # Draw horizontal line at this y position
                pixel_x = int(center_x + wave_x)
                for dx in range(-1, 2):
                    x = pixel_x + dx
                    if 0 <= x < self.matrix.width:
                        brightness = 255 - abs(dx) * 80
                        self.matrix.set_pixel(x, y, brightness)
        
        self.frame += 1
        return True


class Particle:
    """Particle for fireworks animation."""
    
    def __init__(self, x: float, y: float, vx: float, vy: float, life: int = 20):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = life
        self.max_life = life
    
    def update(self):
        """Update particle position."""
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2  # Gravity
        self.life -= 1
    
    def is_alive(self) -> bool:
        """Check if particle is still alive."""
        return self.life > 0
    
    def get_brightness(self) -> int:
        """Get particle brightness based on remaining life."""
        return int((self.life / self.max_life) * 255)


class FireworksAnimation(Animation):
    """Fireworks animation with explosions and particles."""
    
    def __init__(self, matrix: LEDMatrix, num_fireworks: int = 3):
        """
        Initialize fireworks animation.
        
        Args:
            matrix: LED matrix to draw on
            num_fireworks: Maximum number of concurrent fireworks
        """
        super().__init__(matrix)
        self.particles: List[Particle] = []
        self.num_fireworks = num_fireworks
        self.next_launch = 0
    
    def launch_firework(self):
        """Launch a new firework."""
        # Random launch position (bottom of screen)
        launch_x = random.randint(5, self.matrix.width - 5)
        
        # Launch upward to random height
        target_y = random.randint(1, self.matrix.height // 2)
        
        # Create explosion particles
        num_particles = random.randint(15, 25)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.5, 2.0)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed - 1.5  # Initial upward velocity
            
            life = random.randint(15, 30)
            particle = Particle(launch_x, target_y, vx, vy, life)
            self.particles.append(particle)
    
    def update(self) -> bool:
        """Update fireworks animation."""
        self.matrix.clear()
        
        # Launch new fireworks periodically
        if self.frame >= self.next_launch:
            active_fireworks = len([p for p in self.particles if p.is_alive()])
            if active_fireworks < self.num_fireworks:
                self.launch_firework()
                self.next_launch = self.frame + random.randint(15, 40)
        
        # Update and draw particles
        for particle in self.particles[:]:
            if particle.is_alive():
                particle.update()
                
                # Draw particle
                x = int(particle.x)
                y = int(particle.y)
                brightness = particle.get_brightness()
                
                self.matrix.set_pixel(x, y, brightness)
                
                # Add trailing effect
                if particle.life > 5:
                    trail_x = int(particle.x - particle.vx * 0.5)
                    trail_y = int(particle.y - particle.vy * 0.5)
                    self.matrix.set_pixel(trail_x, trail_y, brightness // 2)
            else:
                self.particles.remove(particle)
        
        self.frame += 1
        return True
    
    def reset(self):
        """Reset fireworks animation."""
        super().reset()
        self.particles.clear()
        self.next_launch = 0


class ScrollTextAnimation(Animation):
    """Scroll text across the LED matrix."""
    
    def __init__(self, matrix: LEDMatrix, text: str = "SIGNAL", speed: int = 2):
        """
        Initialize scrolling text animation.
        
        Args:
            matrix: LED matrix to draw on
            text: Text to scroll
            speed: Scroll speed (pixels per frame)
        """
        super().__init__(matrix)
        self.text = text
        self.speed = speed
        self.position = matrix.width
        
        # Simple 5x5 font (uppercase letters only)
        self.font = {
            'S': [[1,1,1,1,1], [1,0,0,0,0], [1,1,1,1,1], [0,0,0,0,1], [1,1,1,1,1]],
            'I': [[1,1,1,1,1], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [1,1,1,1,1]],
            'G': [[1,1,1,1,1], [1,0,0,0,0], [1,0,1,1,1], [1,0,0,0,1], [1,1,1,1,1]],
            'N': [[1,0,0,0,1], [1,1,0,0,1], [1,0,1,0,1], [1,0,0,1,1], [1,0,0,0,1]],
            'A': [[0,1,1,1,0], [1,0,0,0,1], [1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1]],
            'L': [[1,0,0,0,0], [1,0,0,0,0], [1,0,0,0,0], [1,0,0,0,0], [1,1,1,1,1]],
            ' ': [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
        }
    
    def update(self) -> bool:
        """Scroll text across screen."""
        self.matrix.clear()
        
        x_offset = self.position
        
        for char in self.text:
            if char.upper() in self.font:
                glyph = self.font[char.upper()]
                
                # Draw character
                for glyph_y, row in enumerate(glyph):
                    for glyph_x, pixel in enumerate(row):
                        if pixel:
                            screen_y = (self.matrix.height - len(glyph)) // 2 + glyph_y
                            self.matrix.set_pixel(x_offset + glyph_x, screen_y, 255)
                
                x_offset += len(glyph[0]) + 1  # Character width + spacing
        
        # Move position
        self.position -= 1
        
        # Reset when text scrolls off screen
        if self.position < -x_offset:
            self.position = self.matrix.width
        
        self.frame += 1
        return True


def demo_animation(animation: Animation, frames: int = 50, delay: float = 0.1):
    """
    Run a demo of an animation.
    
    Args:
        animation: Animation to demonstrate
        frames: Number of frames to show
        delay: Delay between frames in seconds
    """
    print(f"\n{'='*50}")
    print(f"Demonstrating: {animation.__class__.__name__}")
    print(f"{'='*50}")
    
    for _ in range(frames):
        animation.update()
        animation.matrix.display()
        time.sleep(delay)
    
    animation.reset()


if __name__ == "__main__":
    # Create LED matrix
    matrix = LEDMatrix(width=32, height=8)
    
    print("\nLED Matrix Animation Demo")
    print("=" * 50)
    print("This demo showcases various animation patterns")
    print("suitable for LED matrices in vehicle applications.")
    
    # Demo 1: Right turn signal (planned animation)
    print("\n\n1. RIGHT TURN SIGNAL (Planned Animation)")
    turn_right = TurnSignalAnimation(matrix, direction="right", speed=2)
    demo_animation(turn_right, frames=30, delay=0.1)
    
    # Demo 2: Left turn signal
    print("\n\n2. LEFT TURN SIGNAL (Planned Animation)")
    turn_left = TurnSignalAnimation(matrix, direction="left", speed=2)
    demo_animation(turn_left, frames=30, delay=0.1)
    
    # Demo 3: Pulse animation (dynamic)
    print("\n\n3. PULSE ANIMATION (Dynamic Animation)")
    pulse = PulseAnimation(matrix, intensity=1.0)
    demo_animation(pulse, frames=40, delay=0.05)
    
    # Demo 4: Wave animation (dynamic)
    print("\n\n4. WAVE ANIMATION (Dynamic Animation)")
    wave = WaveAnimation(matrix, direction="horizontal")
    demo_animation(wave, frames=40, delay=0.05)
    
    # Demo 5: Fireworks animation
    print("\n\n5. FIREWORKS ANIMATION")
    fireworks = FireworksAnimation(matrix, num_fireworks=2)
    demo_animation(fireworks, frames=80, delay=0.1)
    
    # Demo 6: Scrolling text
    print("\n\n6. SCROLLING TEXT ANIMATION")
    scroll = ScrollTextAnimation(matrix, text="SIGNAL", speed=1)
    demo_animation(scroll, frames=80, delay=0.05)
    
    print("\n\nDemo complete!")
    print("=" * 50)
