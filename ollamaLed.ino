// === AI-Controlled ESP32 ===
// Simple serial command listener

int ledPin = 2;  // Built-in LED or external one on GPIO 2

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  Serial.println("ESP32 ready for commands...");
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();  // Remove whitespace

    Serial.print("Received: ");
    Serial.println(command);

    if (command.equalsIgnoreCase("LED_ON")) {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned ON");
    }
    else if (command.equalsIgnoreCase("LED_OFF")) {
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned OFF");
    }
    else if (command.startsWith("BLINK")) {
      int times = 3;  // Default blink times
      int index = command.indexOf(' ');
      if (index > 0) {
        times = command.substring(index + 1).toInt();
        if (times <= 0) times = 3;
      }
      Serial.print("Blinking ");
      Serial.print(times);
      Serial.println(" times...");
      for (int i = 0; i < times; i++) {
        digitalWrite(ledPin, HIGH);
        delay(300);
        digitalWrite(ledPin, LOW);
        delay(300);
      }
    }
    else {
      Serial.println("Unknown command");
    }
  }
}
