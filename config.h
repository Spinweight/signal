/**
 * Configuration file for Van LED Lighting System
 * Adjust these settings to match your specific setup
 */

#ifndef CONFIG_H
#define CONFIG_H

// ===== HARDWARE CONFIGURATION =====

// LED Strip Pins (FireBeetle 2 ESP32 GPIO pins)
#define LEFT_SIGNAL_PIN 25      // Left turn signal LED strip
#define RIGHT_SIGNAL_PIN 26     // Right turn signal LED strip  
#define BRAKE_PIN 27            // Brake/tail light LED strip

// Input Pins
#define LEFT_BUTTON_PIN 12      // Left turn signal button/switch
#define RIGHT_BUTTON_PIN 13     // Right turn signal button/switch
#define HAZARD_BUTTON_PIN 14    // Hazard lights button
#define BRAKE_SENSOR_PIN 32     // Brake pedal sensor input

// ===== LED CONFIGURATION =====

// Number of LEDs per strip
#define NUM_LEDS_PER_STRIP 30   // Adjust based on your LED strip length

// Brightness levels (0-255)
#define BRIGHTNESS 200          // Maximum brightness
#define RUNNING_LIGHT_BRIGHTNESS 30  // Brightness for running/tail lights

// ===== TIMING CONFIGURATION =====

// Turn signal timing
#define BLINK_INTERVAL 500      // Blink rate in milliseconds (500ms = 0.5 sec on/off)
#define ANIMATION_SPEED 50      // Animation update speed in milliseconds

// ===== COLOR CONFIGURATION =====

// Colors in RGB hex format (0xRRGGBB)
#define COLOR_AMBER 0xFFB000    // Amber/orange for turn signals
#define COLOR_RED 0xFF0000      // Red for brake lights
#define COLOR_WHITE 0xFFFFFF    // White (optional, for additional features)

// ===== FEATURE CONFIGURATION =====

// Enable/disable features
#define ENABLE_RUNNING_LIGHTS true   // Enable running lights when signals are off
#define ENABLE_STARTUP_ANIMATION true  // Show animation on startup

// Animation style selection (uncomment one)
#define ANIMATION_SEQUENTIAL    // LEDs light up in sequence
// #define ANIMATION_FILL         // LEDs fill from start to end
// #define ANIMATION_BOUNCE       // LEDs bounce back and forth
// #define ANIMATION_CLASSIC      // Simple on/off blink

#endif // CONFIG_H
