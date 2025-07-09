#!/usr/bin/python3
from processing import *
from analysis import pa_score_from_video_file
from pattern_info import PatternInfo
from record import record_pattern
from pa_result import PaResult
from pa import *
from constants import *



import tempfile


def generate_pa_results_for_pattern(pattern_info: PatternInfo)-> list[PaResult]:
    results = []

    # Hardcoding a buffer distance of 3mm here for now.  Adjust if needed.
    with tempfile.TemporaryDirectory("pa_videos") as dir:
        video_files = record_pattern(pattern_info, 4, dir)

        for video_file in video_files:
            s=pa_score_from_video_file(video_file)
            results.append(s)
            print(s)
    return results


