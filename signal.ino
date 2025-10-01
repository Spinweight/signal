/**
 * Dynamic Animated LED Lighting System for 97 E150 Van
 * 
 * Hardware:
 * - FireBeetle 2 ESP32 (DFR1145)
 * - WS2812B LED Strips
 * 
 * Features:
 * - Turn signals (left/right) with animated patterns
 * - Hazard lights
 * - Brake lights
 * - Running lights
 * - Configurable animations
 */

#include <Adafruit_NeoPixel.h>

// Pin definitions for FireBeetle 2 ESP32
#define LEFT_SIGNAL_PIN 25      // GPIO25 for left turn signal LEDs
#define RIGHT_SIGNAL_PIN 26     // GPIO26 for right turn signal LEDs
#define BRAKE_PIN 27            // GPIO27 for brake lights
#define LEFT_BUTTON_PIN 12      // GPIO12 for left turn signal button
#define RIGHT_BUTTON_PIN 13     // GPIO13 for right turn signal button
#define HAZARD_BUTTON_PIN 14    // GPIO14 for hazard button
#define BRAKE_SENSOR_PIN 32     // GPIO32 for brake pedal sensor

// LED strip configuration
#define NUM_LEDS_PER_STRIP 30   // Number of LEDs per strip
#define BRIGHTNESS 200          // LED brightness (0-255)

// Animation timing
#define BLINK_INTERVAL 500      // Blink interval in milliseconds
#define ANIMATION_SPEED 50      // Animation update interval in milliseconds

// LED strip objects
Adafruit_NeoPixel leftStrip(NUM_LEDS_PER_STRIP, LEFT_SIGNAL_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel rightStrip(NUM_LEDS_PER_STRIP, RIGHT_SIGNAL_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel brakeStrip(NUM_LEDS_PER_STRIP, BRAKE_PIN, NEO_GRB + NEO_KHZ800);

// Color definitions
#define COLOR_AMBER 0xFFB000    // Amber for turn signals
#define COLOR_RED 0xFF0000      // Red for brake lights
#define COLOR_WHITE 0xFFFFFF    // White for running lights

// State variables
enum SignalState {
  SIGNAL_OFF,
  SIGNAL_LEFT,
  SIGNAL_RIGHT,
  SIGNAL_HAZARD
};

SignalState currentSignal = SIGNAL_OFF;
bool brakeActive = false;
bool runningLightsOn = true;

unsigned long lastBlinkTime = 0;
unsigned long lastAnimationTime = 0;
bool blinkState = false;
int animationStep = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Van LED Lighting System Starting...");
  
  // Initialize LED strips
  leftStrip.begin();
  rightStrip.begin();
  brakeStrip.begin();
  
  leftStrip.setBrightness(BRIGHTNESS);
  rightStrip.setBrightness(BRIGHTNESS);
  brakeStrip.setBrightness(BRIGHTNESS);
  
  leftStrip.show();
  rightStrip.show();
  brakeStrip.show();
  
  // Initialize input pins
  pinMode(LEFT_BUTTON_PIN, INPUT_PULLUP);
  pinMode(RIGHT_BUTTON_PIN, INPUT_PULLUP);
  pinMode(HAZARD_BUTTON_PIN, INPUT_PULLUP);
  pinMode(BRAKE_SENSOR_PIN, INPUT_PULLUP);
  
  // Startup animation
  startupAnimation();
  
  Serial.println("System ready!");
}

void loop() {
  // Read input buttons
  checkInputs();
  
  // Update animations
  unsigned long currentTime = millis();
  
  // Update blink timing
  if (currentTime - lastBlinkTime >= BLINK_INTERVAL) {
    lastBlinkTime = currentTime;
    blinkState = !blinkState;
  }
  
  // Update animation timing
  if (currentTime - lastAnimationTime >= ANIMATION_SPEED) {
    lastAnimationTime = currentTime;
    animationStep = (animationStep + 1) % NUM_LEDS_PER_STRIP;
  }
  
  // Update LED displays
  updateSignals();
  updateBrakeLights();
  
  delay(10);
}

void checkInputs() {
  // Check left turn signal button
  static bool lastLeftState = HIGH;
  bool leftState = digitalRead(LEFT_BUTTON_PIN);
  if (leftState == LOW && lastLeftState == HIGH) {
    delay(50); // Debounce
    if (digitalRead(LEFT_BUTTON_PIN) == LOW) {
      if (currentSignal == SIGNAL_LEFT) {
        currentSignal = SIGNAL_OFF;
      } else {
        currentSignal = SIGNAL_LEFT;
      }
      Serial.println(currentSignal == SIGNAL_LEFT ? "Left signal ON" : "Signal OFF");
    }
  }
  lastLeftState = leftState;
  
  // Check right turn signal button
  static bool lastRightState = HIGH;
  bool rightState = digitalRead(RIGHT_BUTTON_PIN);
  if (rightState == LOW && lastRightState == HIGH) {
    delay(50); // Debounce
    if (digitalRead(RIGHT_BUTTON_PIN) == LOW) {
      if (currentSignal == SIGNAL_RIGHT) {
        currentSignal = SIGNAL_OFF;
      } else {
        currentSignal = SIGNAL_RIGHT;
      }
      Serial.println(currentSignal == SIGNAL_RIGHT ? "Right signal ON" : "Signal OFF");
    }
  }
  lastRightState = rightState;
  
  // Check hazard button
  static bool lastHazardState = HIGH;
  bool hazardState = digitalRead(HAZARD_BUTTON_PIN);
  if (hazardState == LOW && lastHazardState == HIGH) {
    delay(50); // Debounce
    if (digitalRead(HAZARD_BUTTON_PIN) == LOW) {
      if (currentSignal == SIGNAL_HAZARD) {
        currentSignal = SIGNAL_OFF;
      } else {
        currentSignal = SIGNAL_HAZARD;
      }
      Serial.println(currentSignal == SIGNAL_HAZARD ? "Hazard ON" : "Signal OFF");
    }
  }
  lastHazardState = hazardState;
  
  // Check brake sensor
  brakeActive = (digitalRead(BRAKE_SENSOR_PIN) == LOW);
}

void updateSignals() {
  switch (currentSignal) {
    case SIGNAL_OFF:
      // Show running lights only
      if (runningLightsOn) {
        setStripColor(leftStrip, COLOR_AMBER, 30);  // Dim amber running light
        setStripColor(rightStrip, COLOR_AMBER, 30);
      } else {
        leftStrip.clear();
        rightStrip.clear();
      }
      break;
      
    case SIGNAL_LEFT:
      // Animated left turn signal
      animatedTurnSignal(leftStrip, blinkState);
      if (runningLightsOn) {
        setStripColor(rightStrip, COLOR_AMBER, 30);
      } else {
        rightStrip.clear();
      }
      break;
      
    case SIGNAL_RIGHT:
      // Animated right turn signal
      if (runningLightsOn) {
        setStripColor(leftStrip, COLOR_AMBER, 30);
      } else {
        leftStrip.clear();
      }
      animatedTurnSignal(rightStrip, blinkState);
      break;
      
    case SIGNAL_HAZARD:
      // Both sides blink together
      animatedTurnSignal(leftStrip, blinkState);
      animatedTurnSignal(rightStrip, blinkState);
      break;
  }
  
  leftStrip.show();
  rightStrip.show();
}

void updateBrakeLights() {
  if (brakeActive) {
    // Bright red for brake lights
    setStripColor(brakeStrip, COLOR_RED, 255);
  } else if (runningLightsOn) {
    // Dim red for tail lights
    setStripColor(brakeStrip, COLOR_RED, 30);
  } else {
    brakeStrip.clear();
  }
  brakeStrip.show();
}

void animatedTurnSignal(Adafruit_NeoPixel &strip, bool state) {
  if (state) {
    // Sequential animation - LEDs light up in sequence
    for (int i = 0; i < NUM_LEDS_PER_STRIP; i++) {
      if (i <= animationStep) {
        strip.setPixelColor(i, COLOR_AMBER);
      } else {
        strip.setPixelColor(i, 0);
      }
    }
  } else {
    strip.clear();
  }
}

void setStripColor(Adafruit_NeoPixel &strip, uint32_t color, uint8_t brightness) {
  // Apply brightness scaling to color
  uint8_t r = (uint8_t)((color >> 16) & 0xFF) * brightness / 255;
  uint8_t g = (uint8_t)((color >> 8) & 0xFF) * brightness / 255;
  uint8_t b = (uint8_t)(color & 0xFF) * brightness / 255;
  uint32_t scaledColor = strip.Color(r, g, b);
  
  for (int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, scaledColor);
  }
}

void startupAnimation() {
  Serial.println("Running startup animation...");
  
  // Sweep animation across all strips
  for (int i = 0; i < NUM_LEDS_PER_STRIP; i++) {
    leftStrip.setPixelColor(i, COLOR_AMBER);
    rightStrip.setPixelColor(i, COLOR_AMBER);
    brakeStrip.setPixelColor(i, COLOR_RED);
    leftStrip.show();
    rightStrip.show();
    brakeStrip.show();
    delay(30);
  }
  
  delay(200);
  
  // Clear all
  leftStrip.clear();
  rightStrip.clear();
  brakeStrip.clear();
  leftStrip.show();
  rightStrip.show();
  brakeStrip.show();
  
  delay(200);
  
  // Quick blink
  setStripColor(leftStrip, COLOR_AMBER, 255);
  setStripColor(rightStrip, COLOR_AMBER, 255);
  setStripColor(brakeStrip, COLOR_RED, 255);
  leftStrip.show();
  rightStrip.show();
  brakeStrip.show();
  delay(100);
  
  leftStrip.clear();
  rightStrip.clear();
  brakeStrip.clear();
  leftStrip.show();
  rightStrip.show();
  brakeStrip.show();
}
