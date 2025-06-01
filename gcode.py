import json
import websocket
import random
import requests
from constants import *

ws = websocket.WebSocket()
ws.connect(f"ws://{HOST}:{WS_PORT}/websocket")

with open(r"pa_patterns.gcode", "r", encoding="utf-8") as file:
    GCODE_COMMANDS = file.read()


def send_to_websocket(method: str, args: dict = None):
    # This function is not thread safe.
    request_id = random.randint(0, 10000000)
    request = {
        "jsonrpc": "2.0",
        "method": method,
        "id": request_id
    }
    if args is not None:
        request["params"] = args

    print(request)
    ws.send(json.dumps(request))



def format_move(x: float = 0.0, y: float = 0.0, z: float = 0.0, f: float = 0.0):
    def format_string(value, prefix):
        return f" {prefix}{value}" if value is not None else ""
    return "".join(format_string(value, prefix) for value, prefix in [(x, "x"), (y, "y"), (z, "z"), (f, "f")])

def send_gcode(gcode: str):
    return send_to_websocket("printer.gcode.script", {"script": gcode})

def move_absolute(x: float = 0.0, y: float = 0.0, z: float = 0.0, f: float = 0.0):
    return send_gcode(f"""
    G90
    G0{format_move(x, y, z, f)}
    """)

def home():
    return send_gcode('G28')


def has_homed():
    resp = send_to_websocket("printer.objects.query", {
                             "objects": {"toolhead": None}})
    return resp["result"]["status"]["toolhead"]["homed_axes"] == "xyz"

def move_relative(x: float = 0.0, y: float = 0.0, z: float = 0.0, f: float = 0.0):
    return send_gcode(f"""
    G91
    G0{format_move(x, y, z, f)}
    """)
params = {
        "toolhead": ""
    }


# MOONRAKER_URL = "http://192.168.3.74:7125/printer/objects/query"

def query_printer_position():
    resp = send_to_websocket("printer.objects.query", {
        "objects": {"motion_report": None}})
    return resp["result"]["status"]["motion_report"]["live_position"]


def wait_until_printer_at_location(x=None, y=None, z=None):
    while True:
        position = query_printer_position()
        if x is not None and abs(x - position[0]) > 0.01:
            continue
        if y is not None and abs(y - position[1]) > 0.01:
            continue
        if z is not None and abs(z - position[2]) > 0.01:
            continue
        break


def main():
    # send_to_websocket("server.info")
    print(home())
    # print(query_printer_position())
    # do_initialization_routine()
    # print("Finished initializing")

    # # move_absolute(150, 150, 16, 1000000)
    # # move_absolute(10, 10, 20, 1000000)
    # # move_absolute(150, 150, 16, 1000000)
    # print("Done")


if __name__ == "__main__":
    main()