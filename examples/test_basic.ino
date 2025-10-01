/**
 * Basic LED Test Sketch
 * 
 * Use this to verify your LED strips are working correctly
 * before running the full system.
 * 
 * This will cycle through different colors on all LED strips.
 */

#include <Adafruit_NeoPixel.h>

// Pin definitions - adjust to match your setup
#define LED_PIN 25              // Test with one strip at a time
#define NUM_LEDS 30             // Number of LEDs in your strip

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(115200);
  Serial.println("LED Strip Test Starting...");
  
  strip.begin();
  strip.setBrightness(200);  // Set brightness (0-255)
  strip.show();              // Initialize all pixels to 'off'
  
  Serial.println("Test ready. Will cycle through colors.");
}

void loop() {
  Serial.println("Red");
  colorWipe(strip.Color(255, 0, 0), 50);  // Red
  delay(500);
  
  Serial.println("Green");
  colorWipe(strip.Color(0, 255, 0), 50);  // Green
  delay(500);
  
  Serial.println("Blue");
  colorWipe(strip.Color(0, 0, 255), 50);  // Blue
  delay(500);
  
  Serial.println("Amber");
  colorWipe(strip.Color(255, 176, 0), 50);  // Amber
  delay(500);
  
  Serial.println("White");
  colorWipe(strip.Color(255, 255, 255), 50);  // White
  delay(500);
  
  Serial.println("Rainbow");
  rainbow(10);
  delay(500);
  
  Serial.println("Off");
  strip.clear();
  strip.show();
  delay(1000);
}

// Fill strip with a color, one pixel at a time
void colorWipe(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, color);
    strip.show();
    delay(wait);
  }
}

// Rainbow cycle
void rainbow(int wait) {
  for(long firstPixelHue = 0; firstPixelHue < 65536; firstPixelHue += 256) {
    for(int i=0; i<strip.numPixels(); i++) {
      int pixelHue = firstPixelHue + (i * 65536L / strip.numPixels());
      strip.setPixelColor(i, strip.gamma32(strip.ColorHSV(pixelHue)));
    }
    strip.show();
    delay(wait);
  }
}
