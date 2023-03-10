#!/usr/bin/python
"""Retime SRT files."""
# Jak Crow
# Created: 2018/01/14

import datetime
import os
import subs

# root_path = r'C:\Users\jak\ALL\Japanese\SUBS2SRS\Movies and Shows\FLCL\JP Subs'
# match_pattern = 'FLCL'
# os.chdir(root_path)
# filenames = os.listdir()
# filenames = [filename for filename in filenames if match_pattern in filename]

# first_sub_timings_jp = []
# for filename in filenames:
#     with open(filename, 'r', encoding='utf-8') as file:
#         subs = file.read()
#     subs = list(srt.parse(subs))

#     first_sub_timing = subs[0].start
#     first_sub_timings_jp.append(first_sub_timing)

# root_path = r'C:\Users\jak\ALL\Japanese\SUBS2SRS\Movies and Shows\FLCL\EN Subs'
# match_pattern = 'FLCL'
# os.chdir(root_path)
# filenames = os.listdir()
# filenames = [filename for filename in filenames if match_pattern in filename]

# first_sub_timings_en = []
# for filename in filenames:
#     with open(filename, 'r', encoding='utf-8') as file:
#         subs = file.read()
#     subs = list(srt.parse(subs))

#     first_sub_timing = subs[0].start
#     first_sub_timings_en.append(first_sub_timing)

# timing_diffs = [en_timing - jp_timing for (en_timing, jp_timing) in
#                 zip(first_sub_timings_en, first_sub_timings_jp)]

# for filename, timing_diff in zip(filenames, timing_diffs):
#     with open(filename, 'r', encoding='utf-8') as file:
#         subs = file.read()
#     subs = list(srt.parse(subs))

#     for sub in subs:
#         sub.start = sub.start - timing_diff
#         sub.end = sub.end - timing_diff

#     output_path = root_path + '\\' + 'retimed\\' + filename
#     with open(output_path, 'w+', encoding='utf-8') as file:
#         file.write(srt.compose(subs))

with open(r'C:\Users\jak\Downloads\REC.4.Apocalypse.2014.720p.BluRay.x264-SPLiTSViLLE.srt', 'r', encoding='utf-8') as file:
    subs = file.read()
    subs = list(subs.parse(subs))

    for sub in subs:
        sub.start = sub.start - datetime.timedelta(0, 4, 300)
        sub.end = sub.end - datetime.timedelta(0, 4, 300)

output_path = r'C:\Users\jak\Downloads\REC.4.Apocalypse.2014.720p.BluRay.x264-SPLiTSViLLE_retimed4.srt'
with open(output_path, 'w+', encoding='utf-8') as file:
    file.write(subs.compose(subs))
