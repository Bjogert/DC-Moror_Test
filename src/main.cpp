#include <Arduino.h>

// Pin definitions
const int potPin = 34;    // Potentiometer connected to GPIO34 (A0)
const int in1Pin = 25;    // L298N IN1 (A-1A, PWM capable)
const int in2Pin = 26;    // L298N IN2 (A-1B)
const int enaPin = 25;    // ENA is same as IN1 for single channel (PWM)

void setup() {
  // Initialize pins
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  ledcAttachPin(in1Pin, 0); // Attach IN1 (PWM) to channel 0
  ledcSetup(0, 5000, 8);    // 5 kHz PWM, 8-bit resolution
  Serial.begin(9600);       // Initialize serial communication at 9600 bps
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();    switch (cmd) {
      case 'F': // Forward
        digitalWrite(in2Pin, LOW);  // Original working code
        ledcWrite(0, 255);
        break;
      case 'B': // Backward
        digitalWrite(in2Pin, HIGH); // Original working code
        ledcWrite(0, 255);
        break;
      case 'S': // Stop
        ledcWrite(0, 0);
        break;
      default:
        // Ignore unknown commands
        break;
    }
  }
  delay(10);
}