import re
from functools import reduce

def decompressv1(line):
    marker_re = re.compile(r"\((\d+)x(\d+)\)")
    output = ""
    while True:
        marker = marker_re.search(line)
        if marker is None:
            break
        mark_begin, mark_end = marker.span()
        rep_len, rep_count = int(marker.group(1)), int(marker.group(2))
        output += line[:mark_begin] + line[mark_end:mark_end + rep_len] * rep_count
        line = line[mark_end + rep_len:]
    return output + line

def decompressv2_size(line):
    marker_re = re.compile(r"\((\d+)x(\d+)\)")
    output_size = 0
    while True:
        marker = marker_re.search(line)
        if marker is None:
            break
        mark_begin, mark_end = marker.span()
        rep_len, rep_count = int(marker.group(1)), int(marker.group(2))
        # If we move the "*rep_count" out of the argument to the end, I get the "correct" result instantly, but that
        # would nontheless be wrongly computed because repetition can invent new markers. Example: "(5x2))(2x1.".
        # Correct size: 6. Incorrect size: 11
        output_size += mark_begin + decompressv2_size(line[mark_end:mark_end + rep_len] * rep_count)
        line = line[mark_end + rep_len:]
    return output_size + len(line)

outputv1 = decompressv1(open("input").read())
print ("outputv1 is", outputv1)
print ("outputv1 length is", len(outputv1))

outputv2_size = decompressv2_size(open("input").read())
print ("outputv2 length is", outputv2_size)
