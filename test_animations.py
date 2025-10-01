"""
Quick test to verify all animations run without errors.
"""

from led_matrix_animations import (
    LEDMatrix, TurnSignalAnimation, PulseAnimation, 
    WaveAnimation, FireworksAnimation, ScrollTextAnimation
)

def test_animation(animation, frames=10):
    """Test an animation runs without errors."""
    try:
        for _ in range(frames):
            animation.update()
        animation.reset()
        return True
    except Exception as e:
        print(f"Error in {animation.__class__.__name__}: {e}")
        return False

if __name__ == "__main__":
    matrix = LEDMatrix(width=32, height=8)
    
    tests = [
        ("Right Turn Signal", TurnSignalAnimation(matrix, direction="right")),
        ("Left Turn Signal", TurnSignalAnimation(matrix, direction="left")),
        ("Pulse Animation", PulseAnimation(matrix)),
        ("Wave Animation (Horizontal)", WaveAnimation(matrix, direction="horizontal")),
        ("Wave Animation (Vertical)", WaveAnimation(matrix, direction="vertical")),
        ("Fireworks Animation", FireworksAnimation(matrix)),
        ("Scrolling Text", ScrollTextAnimation(matrix, text="TEST")),
    ]
    
    print("Running animation tests...")
    all_passed = True
    
    for name, animation in tests:
        if test_animation(animation, frames=20):
            print(f"✓ {name}")
        else:
            print(f"✗ {name}")
            all_passed = False
    
    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")
        exit(1)
