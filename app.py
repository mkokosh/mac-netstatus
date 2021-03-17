import rumps
import os
import threading

class netStatus(rumps.App):

    def __init__(self):
        super(netStatus, self).__init__(name="Ping")
        self.title = "❔"
    
    @rumps.clicked("Wyczyść")
    def clearIcon(self, sender):
        self.title = "❔"

    def getPingStatus(self):
        online = os.system("ping -c 1 -W 1 1.1.1.1")
        if online==0:
            self.title = "😀"
        else:
            self.title = "🚫"

    @rumps.timer(5)
    def updatePingStatus(self,sender):
        thread = threading.Thread(target=self.getPingStatus)
        thread.start()

if __name__ == '__main__':
    netStatus().run()


