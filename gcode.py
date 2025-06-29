import json
import websocket
import random
from constants import *
import time
# Helper function to automatically generate the coordinate strings
# for G0 commands.
def format_move(x: float = None, y: float = None, z: float = None, f: float = None):
    def format_string(value, prefix):
        return f" {prefix}{value}" if value is not None else ""
    return "".join(format_string(value, prefix) for value, prefix in [(x, "x"), (y, "y"), (z, "z"), (f, "f")])


def move_absolute(x: float = None, y: float = None, z: float = None, f: float = None):
    return send_gcode(f"""
    G90
    G0{format_move(x, y, z, f)}
    """)


def move_relative(x: float = None, y: float = None, z: float = None, f: float = None):
    return send_gcode(f"""
    G91
    G0{format_move(x, y, z, f)}
    """)


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

    # print(request)
    ws.send(json.dumps(request))
    while True:
        raw = ws.recv()
        if not raw:
            print("WebSocket returned empty response!")
            continue  # or handle/reconnect as appropriate

        try:
            resp = json.loads(raw)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {raw}")
            continue  # or handle/reconnect as appropriate

        if "id" in resp and resp["id"] == request_id:
            return resp


ws = websocket.WebSocket()
ws.connect(f"ws://{HOST}:{WS_PORT}/websocket")
def connect_ws():

    ws = websocket.WebSocket()
    ws.connect(f"ws://{HOST}:{WS_PORT}/websocket")
    return ws

def send_gcode(gcode: str):
    return send_to_websocket("printer.gcode.script", {"script": gcode})

def send_gcode_with_retry(gcode, retries=3, delay=2):
    global ws
    for attempt in range(retries):
        try:
            send_gcode(gcode)
            return
        except (ConnectionResetError, websocket.WebSocketConnectionClosedException, OSError) as e:
            print(f"WebSocket error: {e} (attempt {attempt+1} of {retries})")
            try:
                ws.close()
            except Exception:
                pass
            ws = connect_ws()
            time.sleep(delay)
    print("Failed to send G-code after several retries.")



def home():
    return send_gcode('G28')


def has_homed():
    resp = send_to_websocket("printer.objects.query", {
                             "objects": {"toolhead": None}})
    return resp["result"]["status"]["toolhead"]["homed_axes"] == "xyz"


# def do_initialization_routine():
#     if not has_homed():
#         print("Homing")
#         home()
#         # print("Quad Gantry Level")
#         # send_gcode("QUAD_GANTRY_LEVEL")
#         # print("Rehoming Z")
#         # send_gcode("G28 Z")


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
    print(has_homed())
    move_absolute(150, 150, 16, 1000000)
    move_absolute(10, 10, 20, 1000000)
    move_absolute(150, 150, 16, 1000000)
    print("Done")


if __name__ == "__main__":
    main()

# start at x=45, y=305, end at x=109 (leaving 8mm off the start and end for now)