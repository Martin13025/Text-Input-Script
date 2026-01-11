import pyautogui
import time


text = """Success is not measured by the destination, but by the obstacles overcome along the way. Persistence, resilience, and a positive mindset are the key ingredients to achieving one's goals, no matter how impossible they may seem."""

# Speed typing (seconds between characters)
# The smaller the number, the faster the typing
typing_speed = 0.05  # 0.05 = fast, 0.2 = slow

# Delay before start (seconds)
# Gives time to switch to the desired window
delay_before_start = 10

print(f"The script will start typing in {delay_before_start} seconds...")
print("Quickly switch to the desired window/input field!")
time.sleep(delay_before_start)

print("Starting to type...")

# Automatic typing
for char in text:
    pyautogui.write(char, interval=typing_speed)

print("\nDone!")