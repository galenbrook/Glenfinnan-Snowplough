from Exscript.protocols import Telnet
from Exscript.util import start
from time import sleep
from subprocess import Popen


class Display_Driver():
    """
    This class drives the Vestel display which plays the video for the exhibition
    Default values for parameters ip, username, pword, port, videoPath should be okay as long as nothing is changed.
    The display is set to go into standby mode after 10 seconds if no input signal is detected. Therefore it
    should pretty much always be in standby mode when this class is instantiated once the exhibition is installed
    and therefore the method 'toggle_display_standby' should always switch the display on when called once from idle.
    """
    
    def __init__(self, ip="10.166.76.10", username='', pword='', port=1986,
                 videoPath="/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Media/test_video.mp4"):
        self.ip = ip
        self.username = username
        self.pword = pword
        self.port = port
        self.videoPath = videoPath
        
        # These commands are from the Vestel display user manual and are in a format that the software
        # on the display will accept over a valid Telnet connection"
        self.cmdStandbyToggle = "KEY standby\n"
        self.cmdGetVidState = "GETVIDSTATE\n"
        

    def toggle_display_standby(self):
        """
        Sends a Telnet command over Ethernet local area network to the display to toggle standby mode.
        If this does not work check that the display is powered on by the switch and that the Ethernet
        cable is actually plugged in to both the Raspberry Pi and the display
        """
        
        with open('log.txt', 'w') as file:
            try:
                conn = Telnet(stdout=file)
                conn.connect(hostname=self.ip, port=self.port)
                
                # Ideally would use conn.execute() to actually get feedback from the display
                # Could not get this to work in time though
                conn.send(cmd_standby_toggle)
                                
            except:
                print("Connection attempt failed.")
                
            finally:
                print(conn.response)
                print("Command executed successfully.")
                conn.close()
        

    def play_video(self):
        """
        Spawns a new process which opens VLC media player and plays the video located at the
        specified file path on the Raspberry Pi. If the video is ever changed it is **imperative**
        that it is placed in the same file location and given the same name, or that the video path
        in this file is updated to reflect any change.
        """
        vlcp = Popen(["vlc", "--play-and-exit", self.videoPath, "--fullscreen"])
        
        # Could add a timer here to make the process exit and the display switch off just before
        # the video finishes in order to avoid the slight moment where the desktop is visible
        # before the display switches off again
        vlcp.wait()

