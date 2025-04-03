from Exscript.protocols import Telnet
from Exscript.util import start
from time import sleep
from subprocess import Popen

videoPath = "/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Media/test_video.mp4"

ip = "10.166.76.10"
username = ''
pword = ''
port = 1986

#def execute_command(command, host, conn):

cmd_standby_toggle = "KEY standby\n"
cmd_get_video_state = "GETVIDSTATE\n"

with open('log.txt', 'w') as file:
    conn = Telnet(stdout=file)
    conn.connect(hostname=ip, port=port)
    #conn.autoinit()
    
    Popen(["wlr-randr", "--output", "HDMI-A-1", "--off"])
    #sleep(1)
    #Popen(["wlr-randr", "--output", "HDMI-A-2", "--on"])
    #sleep(1)
    conn.send(cmd_standby_toggle)

    vlcp = Popen(["vlc", "--play-and-exit", videoPath, "--fullscreen"])
    vlcp.wait()
    
    Popen(["wlr-randr", "--output", "HDMI-A-1", "--on"])
    #sleep(1)
    #Popen(["wlr-randr", "--output", "HDMI-A-1", "--on"])
    #sleep(1)
    conn.send(cmd_standby_toggle)
    

    
    print(conn.response)
    print("Command executed successfully.")


#conn.expect_prompt()