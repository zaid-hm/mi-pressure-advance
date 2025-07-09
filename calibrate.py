import tempfile
from gcode import *
from generate_results import generate_pa_results_for_pattern
from pa import *
from pa_result import PaResult
from record import record_pattern
from pattern_info import PatternInfo
from analysis import generate_height_data_from_video
import shutil
import subprocess
import numpy as np


# send_gcode("LASER_OFF")
# send_gcode(PRINT_START)
# send_gcode("PURGE_LINE")

normal_pattern = PatternInfo(
    0, 0.06,
    65, 30,
    10,
    30, 4
)
# gcode= generate_pa_tune_gcode(normal_pattern)
# send_gcode(PRINT_START)
# send_gcode(gcode)
# send_gcode("G90;")
# send_gcode(f"G1 X{FINISHED_X} Y{FINISHED_Y} F30000")
# wait_until_printer_at_location(FINISHED_X, FINISHED_Y)
# send_gcode("M104 S0; let the hotend cool")



results = []
home()
send_gcode("LASER_ON")
results = []

with tempfile.TemporaryDirectory("pa_videos") as dir:
        video_files = record_pattern(normal_pattern, 4, dir)

        for video_file in video_files:
            results.append(
                generate_height_data_from_video(video_file)
            )
print(results)
from synthetic import plot_height_map
plot_height_map(results[0])