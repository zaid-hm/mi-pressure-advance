# %%
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
import os

# %%
patterns: list[PatternInfo] = []
for x in range(20, 186, 31):
    for y in range(80, 190, 45):
        patterns.append(
            PatternInfo(
                0, 0.06,
                x, y,
                10,
                30, 4
        ))

# %%
# send_gcode(PRINT_START)
# send_gcode("PURGE_LINE")
# send_gcode("M109 S255")
# send_gcode("CLEAN_NOZZLE")
# home()
# for pattern in patterns:
#     send_gcode(generate_pa_tune_gcode(pattern, False))
# send_gcode("G90;")
# send_gcode(f"G1 X{FINISHED_X} Y{FINISHED_Y} F30000")
# wait_until_printer_at_location(FINISHED_X, FINISHED_Y)
# send_gcode("M104 S0; let the hotend cool")

# %%
pa_scans= []
send_gcode("G28")
for pattern in patterns:
    results=generate_pa_results_for_pattern(pattern)
    sorted_results = list(sorted(zip(results, pattern.pa_values), key=lambda x: x[0].score))
    # sorted_results = list([(x.score, y) for x, y in sorted_results])
    scored_results=[]
    score=1
    for result,value in sorted_results:
        scored_results.append([score,sorted_results])
        score-=0.1
    pa_scans.extend(scored_results)
    

# %%
output_dir="scanned_maps"

for i,score,hm,value in enumerate(pa_scans):
    filename = f"map_{i:02d}_score_{score:.4f}.csv"
    filepath = os.path.join(output_dir, filename)
    np.savetxt(filepath, hm, delimiter=",")


