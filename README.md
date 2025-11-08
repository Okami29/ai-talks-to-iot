This project connects **AI and IoT** in a simple, magical way.  
You can type natural language commands like:
- Can you blink the LED twice?
- Turn on the light please.
- Turn it off now.
  
…and your **AI assistant (Ollama)** interprets the command, then sends it to an **ESP32**, which controls the LED in real time.
## 🚀 Overview

**AI + IoT = Smart Interaction**

- 🧠 **AI (Ollama)** understands what you mean.
- ⚙️ **Python** acts as the interpreter between AI and hardware.
- 🔌 **ESP32** executes the action (LED on/off/blink).

This lesson bridges the gap between **Artificial Intelligence** and the **Internet of Things**, perfect for classrooms, workshops, and beginner AI+IoT enthusiasts.

---

## 🪛 Hardware Setup

**You’ll need:**
- 1 × ESP32 board  
- 1 × LED (or use the built-in one on GPIO 2)  
- 1 × 220Ω resistor (optional)  
- Jumper wires  
- USB cable

**Connections (if using external LED):**

| ESP32 Pin | Component | Description |
|------------|------------|--------------|
| GPIO 2     | LED (+)    | LED positive leg |
| GND        | LED (–)    | LED negative leg |

*(You can also use the onboard LED on most ESP32 boards.)*

---
