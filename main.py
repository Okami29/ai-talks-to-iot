from langchain_ollama import OllamaLLM
import serial
import time

# === SETUP ===
# Replace COM3 with your ESP32 port (e.g., /dev/ttyUSB0 on macOS/Linux)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

llm = OllamaLLM(model="llama3.1:8b")  # or whichever model you use

print("🤖 Type commands for your AI-controlled ESP32!")
print("Example: 'Can you blink the LED twice?' or 'Turn it off please.'")
print("Type 'exit' to quit.\n")

def interpret_command(user_text):
    """Ask Ollama to translate natural language into a serial command."""
    prompt = f"""
    You are an AI interpreter for an IoT device (ESP32).
    The user will send natural language commands about controlling an LED.
    Convert them into simple serial commands for the microcontroller.

    Possible commands:
    - "LED_ON" → Turn on the LED
    - "LED_OFF" → Turn off the LED
    - "BLINK X" → Blink LED X times

    Only reply with the command text (like LED_ON, LED_OFF, or BLINK 3).
    Do NOT include explanations or punctuation.
    User said: "{user_text}"
    """
    response = llm.invoke(prompt)
    return response.strip().upper()

while True:
    user_text = input("🗣 Your command: ")
    if user_text.lower() == "exit":
        break

    command = interpret_command(user_text)
    print(f"🧠 AI interpreted as: {command}")

    ser.write((command + "\n").encode())
    time.sleep(0.5)

    feedback = ser.readline().decode().strip()
    while feedback:
        print("ESP32:", feedback)
        feedback = ser.readline().decode().strip()
