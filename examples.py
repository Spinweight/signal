"""
Example usage of LED matrix animations.
This file demonstrates how to use different animation types.
"""

import time
from led_matrix_animations import (
    LEDMatrix, TurnSignalAnimation, PulseAnimation,
    WaveAnimation, FireworksAnimation, ScrollTextAnimation
)


def example_turn_signals():
    """Example: Basic turn signal usage for a van."""
    print("\n" + "="*60)
    print("Example 1: Turn Signals for Van")
    print("="*60)
    
    matrix = LEDMatrix(width=32, height=8)
    
    # Right turn signal
    print("\nActivating RIGHT turn signal...")
    right_turn = TurnSignalAnimation(matrix, direction="right", speed=2)
    
    for i in range(20):
        right_turn.update()
        if i % 5 == 0:  # Print every 5th frame
            matrix.display()
        time.sleep(0.05)
    
    # Left turn signal
    print("\nActivating LEFT turn signal...")
    left_turn = TurnSignalAnimation(matrix, direction="left", speed=2)
    
    for i in range(20):
        left_turn.update()
        if i % 5 == 0:
            matrix.display()
        time.sleep(0.05)


def example_dynamic_brake_light():
    """Example: Dynamic brake light with pulse effect."""
    print("\n" + "="*60)
    print("Example 2: Dynamic Brake Light")
    print("="*60)
    print("\nSimulating brake light with intensity variation...")
    
    matrix = LEDMatrix(width=32, height=8)
    pulse = PulseAnimation(matrix, intensity=0.5)
    
    # Simulate light brake
    print("\n[Light brake pressure]")
    pulse.set_intensity(0.5)
    for i in range(15):
        pulse.update()
        if i % 5 == 0:
            matrix.display()
        time.sleep(0.05)
    
    # Simulate hard brake
    print("\n[Hard brake pressure]")
    pulse.set_intensity(1.0)
    for i in range(15):
        pulse.update()
        if i % 5 == 0:
            matrix.display()
        time.sleep(0.05)


def example_attention_grabber():
    """Example: Attention-grabbing fireworks effect."""
    print("\n" + "="*60)
    print("Example 3: Attention-Grabbing Display (Fireworks)")
    print("="*60)
    print("\nShowing fireworks effect for special occasions...")
    
    matrix = LEDMatrix(width=32, height=8)
    fireworks = FireworksAnimation(matrix, num_fireworks=2)
    
    for i in range(50):
        fireworks.update()
        if i % 10 == 0:  # Print every 10th frame
            matrix.display()
        time.sleep(0.1)


def example_message_display():
    """Example: Scrolling message display."""
    print("\n" + "="*60)
    print("Example 4: Scrolling Message")
    print("="*60)
    print("\nDisplaying scrolling text message...")
    
    matrix = LEDMatrix(width=32, height=8)
    message = ScrollTextAnimation(matrix, text="SIGNAL", speed=1)
    
    for i in range(50):
        message.update()
        if i % 10 == 0:  # Print every 10th frame
            matrix.display()
        time.sleep(0.05)


def example_combined_effects():
    """Example: Combining multiple animations."""
    print("\n" + "="*60)
    print("Example 5: Combined Effects Scenario")
    print("="*60)
    
    matrix = LEDMatrix(width=32, height=8)
    
    # Scenario: Starting vehicle and signaling
    print("\n1. Vehicle starting (pulse effect)...")
    pulse = PulseAnimation(matrix, intensity=0.7)
    for i in range(15):
        pulse.update()
        time.sleep(0.05)
    
    time.sleep(0.3)
    
    print("\n2. Preparing to turn right (turn signal)...")
    turn = TurnSignalAnimation(matrix, direction="right", speed=3)
    for i in range(25):
        turn.update()
        if i % 5 == 0:
            matrix.display()
        time.sleep(0.05)
    
    time.sleep(0.3)
    
    print("\n3. Special celebration mode (fireworks)...")
    fireworks = FireworksAnimation(matrix, num_fireworks=2)
    for i in range(30):
        fireworks.update()
        if i % 10 == 0:
            matrix.display()
        time.sleep(0.1)


def example_wave_patterns():
    """Example: Wave patterns for ambient lighting."""
    print("\n" + "="*60)
    print("Example 6: Wave Patterns (Ambient Mode)")
    print("="*60)
    
    matrix = LEDMatrix(width=32, height=8)
    
    print("\nHorizontal wave...")
    h_wave = WaveAnimation(matrix, direction="horizontal")
    for i in range(20):
        h_wave.update()
        if i % 5 == 0:
            matrix.display()
        time.sleep(0.05)
    
    time.sleep(0.3)
    
    print("\nVertical wave...")
    v_wave = WaveAnimation(matrix, direction="vertical")
    for i in range(20):
        v_wave.update()
        if i % 5 == 0:
            matrix.display()
        time.sleep(0.05)


if __name__ == "__main__":
    print("\n" + "="*60)
    print("LED Matrix Animation Examples")
    print("Practical use cases for van turn signals and displays")
    print("="*60)
    
    # Run all examples
    example_turn_signals()
    example_dynamic_brake_light()
    example_attention_grabber()
    example_message_display()
    example_combined_effects()
    example_wave_patterns()
    
    print("\n" + "="*60)
    print("Examples complete!")
    print("="*60)
    print("\nThese animations can be adapted for:")
    print("- Turn signals (left/right)")
    print("- Brake lights (with intensity)")
    print("- Hazard lights")
    print("- Custom messages")
    print("- Celebration/event displays")
    print("- Ambient lighting effects")
    print("="*60)
