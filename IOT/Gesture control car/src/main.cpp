#include <Arduino.h>

#include <esp_now.h>
#include <WiFi.h>

// Pin definitions for the 4 LEDs
const int ledFrontRight = 25;  // Front Right LED
const int ledFrontLeft = 26;   // Front Left LED
const int ledBackRight = 27;   // Back Right LED
const int ledBackLeft = 14;    // Back Left LED

typedef struct struct_message {
  int gesture; // Gesture info to control LED
} struct_message;

struct_message myData;

void setup() {
  Serial.begin(115200);

  pinMode(ledFrontRight, OUTPUT);
  pinMode(ledFrontLeft, OUTPUT);
  pinMode(ledBackRight, OUTPUT);
  pinMode(ledBackLeft, OUTPUT);

  WiFi.mode(WIFI_STA);
  esp_now_init();
  esp_now_register_recv_cb(OnDataRecv);
}

void loop() {
  // Main loop does nothing, as the control happens in the callback
}

void OnDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len) {
  memcpy(&myData, incomingData, sizeof(myData));

  // Control LEDs based on received gesture
  if (myData.gesture == 1) {  // Forward
    digitalWrite(ledFrontRight, HIGH);
    digitalWrite(ledFrontLeft, HIGH);
    digitalWrite(ledBackRight, LOW);
    digitalWrite(ledBackLeft, LOW);
  } else if (myData.gesture == -1) {  // Backward
    digitalWrite(ledFrontRight, LOW);
    digitalWrite(ledFrontLeft, LOW);
    digitalWrite(ledBackRight, HIGH);
    digitalWrite(ledBackLeft, HIGH);
  } else {  // Stop or no gesture
    digitalWrite(ledFrontRight, LOW);
    digitalWrite(ledFrontLeft, LOW);
    digitalWrite(ledBackRight, LOW);
    digitalWrite(ledBackLeft, LOW);
  }
}
