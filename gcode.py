import json
import requests
from constants import *

with open(r"pa_patterns.gcode", "r", encoding="utf-8") as file:
    GCODE_COMMANDS = file.read()


def format_move(x: float = 0.0, y: float = 0.0, z: float = 0.0, f: float = 0.0):
    def format_string(value, prefix):
        return f" {prefix}{value}" if value is not None else ""
    return "".join(format_string(value, prefix) for value, prefix in [(x, "x"), (y, "y"), (z, "z"), (f, "f")])

def send_gcode(gcode: str):
    url = f"{MOONRAKER_URL}/printer/gcode/script"
    payload = {"script": gcode}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("G-code sent successfully:", response.json())
        return response.json()
    except requests.RequestException as e:
        print("Failed to send G-code:", e)

def move_absolute(x: float = 0.0, y: float = 0.0, z: float = 0.0, f: float = 0.0):
    return send_gcode(f"""
    G90
    G0{format_move(x, y, z, f)}
    """)


def move_relative(x: float = 0.0, y: float = 0.0, z: float = 0.0, f: float = 0.0):
    return send_gcode(f"""
    G91
    G0{format_move(x, y, z, f)}
    """)
params = {
        "toolhead": ""
    }


MOONRAKER_URL = "http://192.168.3.74:7125/printer/objects/query"

def query_printer_position():
    try:
        # Correct POST format for Moonraker
        response = requests.post(MOONRAKER_URL, json={
            "objects": {
                "toolhead": ""
            }
        })
        response.raise_for_status()
        data = response.json()

        toolhead = data.get("result", {}).get("status", {}).get("toolhead")

        if toolhead and "position" in toolhead:
            print("Position (X, Y, Z):", toolhead["position"])
        else:
            print("Toolhead position not available. Is the printer homed?")
            print("Full response:", data)
    except Exception as e:
        print("Error:", e)
query_printer_position()
