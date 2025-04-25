from Exscript.protocols import Telnet
from Exscript.util import start
from time import sleep
from subprocess import Popen

finalVideoPath = "/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Media/Snowplough_video.mp4"
testVideoPath = "/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Media/test_video.mp4"

class Display_Driver():
    """
    This class drives the Vestel display which plays the video for the exhibition
    Default values for parameters ip, username, pword, port, videoPath should be okay as long as nothing is changed.
    The display is set to go into standby mode after 10 seconds if no input signal is detected. Therefore it
    should pretty much always be in standby mode when this class is instantiated once the exhibition is installed
    and therefore the method 'toggle_display_standby' should always switch the display on when called once from idle.
    """
    
    def __init__(self, ip="10.166.76.10", username='', pword='', port=1986,
                 videoPath=finalVideoPath):
        self.ip = ip
        self.username = username
        self.pword = pword
        self.port = port
        self.videoPath = videoPath
        self.conn = None
        self.responses = ["video is on", "video is off"]
        
        # These commands are from the Vestel display user manual and are in a format that the software
        # on the display will accept over a valid Telnet connection"
        self.cmdStandbyToggle = "KEY standby\n"
        self.cmdGetVidState = "GETVIDSTATE\n"
        

    def toggle_standby(self):
        """
        Sends a Telnet command over Ethernet local area network to the display to toggle standby mode.
        If this does not work check that the display is powered on by the switch and that the Ethernet
        cable is actually plugged in to both the Raspberry Pi and the display
        """
        
        with open('log.txt', 'w') as file:
            try:
                self.conn = Telnet(stdout=file)
                print("Attempting to connect to display via Telnet...")
                self.conn.connect(hostname=self.ip, port=self.port)
                
                print("Sending standby command.")
                self.conn.send(self.cmdStandbyToggle)
                (idx, _) = self.conn.expect(responses)  # Wait for response from the display
                                
            except Exception as exc:
                print("Connection attempt failed. ", exc)
                
            finally:
                #print(conn.response)
                #print("Command executed successfully.")
                print("Connection closed.")
        
    
    def _get_video_state(self):
        print("Sending getVidState command.")
        self.conn.send(self.cmdGetVidState)
        (idx, _) = self.conn.expect(self.responses)
        print(f"Response: {self.responses[idx]}")
        if (idx == 0):
            return True
        elif (idx == 1):
            return False
    
    
    def switch_on(self):
        try:
            self.conn = Telnet()
            print(self.conn.get_host())
            
            print("Attempting to connect to display via Telnet...")
            self.conn.connect(hostname=self.ip, port=self.port)
            
            displayOn = self._get_video_state()

            if (displayOn):
                print("Display is already on.")  # Don't need to do anything here as display is already on
            else:
                print("Switching display on.")
                print("Sending standby toggle command.")
                self.conn.send(self.cmdStandbyToggle)
                            
        except Exception as exc:
            print("Connection attempt failed. ", exc)
            
        finally:
            self.conn.close(force=True)
            print("Connection closed.")
        
        
    def switch_off(self):
        try:
            self.conn = Telnet()
            print(self.conn.get_host())
            
            print("Attempting to connect to display via Telnet...")
            self.conn.connect(hostname=self.ip, port=self.port)
            
            displayOff = not(self._get_video_state())

            if (displayOff):
                print("Display is already off.")  # Don't need to do anything here as display is already on
            else:
                print("Switching display off.")
                print("Sending standby toggle command.")
                self.conn.send(self.cmdStandbyToggle)
                            
        except Exception as exc:
            print("Connection attempt failed. ", exc)
            
        finally:
            self.conn.close(force=True)
            print("Connection closed.")
    
        
    def play_video(self):
        """
        Spawns a new process which opens VLC media player and plays the video located at the
        specified file path on the Raspberry Pi. If the video is ever changed it is **imperative**
        that it is placed in the same file location and given the same name, or that the video path
        in this file is updated to reflect any change.
        """
        vlcp = Popen(["cvlc", "--play-and-exit", "--no-qt-video-autoresize", self.videoPath, "--fullscreen"])
        
        # Uncomment this if you want file logging for debug purposes
        #vlcp = Popen(["cvlc", "--play-and-exit", "--file-logging", "--logfile=/home/glenfinnan/snowplough/Glenfinnan-Snowplough/logs/vlc.log","--no-qt-video-autoresize", self.videoPath, "--fullscreen"])
    
        # Use the return value if you need to wait for the process to execute
        return vlcp        

    def run_display(self):
        self.switch_on()
        
        vlcp = self.play_video()
        vlcp.wait()
        
        self.switch_off()

if __name__ == '__main__':
    display = Display_Driver(videoPath=testVideoPath)
    display.run_display()