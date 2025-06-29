from gcode import *
from pattern_info import PatternInfo
import numpy as np
import subprocess
import time
from pathlib import Path
from constants import *




ffmpeg_cmd = [
    "ffmpeg",
    "-y",
    "-f", "mjpeg",
    "-r", str(FRAMERATE),
    "-i", MJPEG_STREAM_URL,
]

def record_pattern(info: PatternInfo, buffer_distance: float, output_directory: str) -> list:
    # send_gcode("STATUS_OFF") # Turn off LEDs
    # send_gcode("LASER_ON") # Turn on line laser
    # send_gcode("SET_LED LED=chamber_lights WHITE=0")
    time.sleep(0.5)

    lines_start_y = info.lines_start_y()
    y_values = np.asarray(lines_start_y) + CAMERA_OFFSET_Y
    scan_start_x = info.start_x + buffer_distance + CAMERA_OFFSET_X
    scan_length = info.line_length - buffer_distance * 2
    scan_end_x = scan_start_x + scan_length

    video_files = []
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    for index, y_value in enumerate(y_values):
        move_absolute(scan_start_x, y_value, LASER_FOCUS_HEIGHT, 30000)
        wait_until_printer_at_location(scan_start_x, y_value)

        video_file = f"{output_directory}/line{index}.mp4"
        video_files.append(video_file)

        with subprocess.Popen(ffmpeg_cmd + [video_file]) as ffmpeg:
            time.sleep(FFMPEG_START_DELAY)
            print(move_absolute(scan_end_x, f=400))
            wait_until_printer_at_location(scan_end_x)

            ffmpeg.terminate()
            time.sleep(FFMPEG_STOP_DELAY)

    # send_gcode("LASER_OFF")
    # send_gcode("SET_LED LED=chamber_lights WHITE=1")
    return video_files
