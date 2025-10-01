# Changelog

All notable changes to the Van LED Lighting System will be documented in this file.

## [1.0.0] - 2024-12-19

### Added
- Initial release of dynamic LED lighting system for 1997 E150 Van
- Main Arduino sketch (signal.ino) for FireBeetle 2 ESP32 (DFR1145)
- WS2812B LED strip control using Adafruit NeoPixel library
- Turn signal animations (left, right, hazard) with sequential pattern
- Brake light functionality with automatic brightness control
- Running/marker light modes for tail lights
- Startup animation sequence for visual confirmation
- Configuration file (config.h) for easy customization
- Button inputs for turn signals and hazard lights
- Brake pedal sensor integration via optocoupler
- Test example sketch (test_basic.ino) for LED strip validation

### Documentation
- Comprehensive README with feature overview and setup instructions
- Detailed WIRING.md with circuit diagrams and connections
- INSTALLATION_GUIDE.md with step-by-step installation process
- TROUBLESHOOTING.md for common issues and solutions
- PARTS_LIST.md with component specifications and cost estimates
- SCHEMATIC.md with ASCII art diagrams of system architecture
- FAQ.md answering common questions
- QUICKSTART.md for rapid bench testing
- VISUAL_GUIDE.md with LED animation patterns and mounting locations
- libraries.txt listing required Arduino libraries
- LICENSE (MIT) for open source distribution

### Features
- Sequential LED animation sweeping from inner to outer
- Configurable blink rate (default 500ms, 60 blinks/minute)
- Adjustable brightness levels (0-255)
- Customizable LED count per strip
- Hazard light mode with synchronized blinking
- Debounced button inputs for reliable switching
- Serial debug output for troubleshooting
- Low power consumption with ESP32
- Compatible with 12V vehicle electrical systems

### Safety Features
- Fuse protection on 12V input
- Regulated 5V power for LED protection
- Optocoupler isolation for brake signal
- Proper debouncing to prevent false triggers
- Running lights for visibility when not signaling

## [Unreleased]

### Planned Features
- WiFi/Bluetooth control via smartphone app
- Multiple animation patterns (fill, bounce, chase)
- Automatic brightness adjustment based on ambient light
- OTA (Over-The-Air) firmware updates
- Integration with reverse lights
- Custom color schemes
- Sound-reactive mode
- Diagnostic mode with status LEDs
- Configuration portal for web-based settings
- Battery voltage monitoring
- Low power sleep mode

### Potential Improvements
- PCB design for cleaner installation
- 3D-printed enclosure models
- Additional animation algorithms
- Support for other ESP32 boards
- Support for other LED types (APA102, SK6812)
- Mobile app development (iOS/Android)
- Cloud integration for remote monitoring
- Multi-vehicle support in single app

## Version History

- **1.0.0** (2024-12-19): Initial release - Full featured LED lighting system

---

## Contributing

Found a bug or have a feature request? Please open an issue on GitHub.

Want to contribute? Pull requests are welcome! Please ensure:
- Code follows existing style
- Documentation is updated
- Changes are tested on actual hardware
- Commit messages are descriptive

## Support

For questions or help:
1. Check FAQ.md for common questions
2. Review TROUBLESHOOTING.md for issues
3. Open an issue on GitHub
4. Provide details: hardware, symptoms, serial output

---

### Version Numbering

This project follows [Semantic Versioning](https://semver.org/):
- MAJOR version: Incompatible API changes
- MINOR version: New functionality (backwards compatible)
- PATCH version: Bug fixes (backwards compatible)

Example: v1.2.3
- 1 = Major version
- 2 = Minor version  
- 3 = Patch version
