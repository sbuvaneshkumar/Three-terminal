import subprocess
import threading
 
class CountThread(threading.Thread):
    def run(self):
        subprocess.call('/bin/gnome-terminal') % (x)
 
a = CountThread()
a.start()
b = CountThread()
b.start()
c = CountThread()
c.start()
