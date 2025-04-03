import os
import sys
from time import sleep

from subprocess import Popen

videoPath = "/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Media/test_video.mp4"

# Popen(["wlr-randr", "--output", "HDMI-A-2", "--off"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-2", "--on"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-2", "--mode", "4096x2160"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-2", "--pos", "1920,0"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-1", "--off"])

vlcp = Popen(["vlc", "--play-and-exit", videoPath, "--fullscreen"])
vlcp.wait()

# Popen(["wlr-randr", "--output", "HDMI-A-2", "--off"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-1", "--on"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-2", "--on"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-2", "--mode", "4096x2160"])
# sleep(0.5)
# Popen(["wlr-randr", "--output", "HDMI-A-2", "--pos", "1920,0"])