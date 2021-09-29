import rumps
import os
import threading
import requests

class netStatus(rumps.App):

    _isp = "?"

    def __init__(self):
        super(netStatus, self).__init__(name="Ping")
        self.title = "❔"
    
    @rumps.clicked("Wyczyść")
    def clearIcon(self, sender):
        self.title = "❔"

    def getPingStatus(self):
        online = os.system("ping -c 1 -W 1 1.1.1.1")
        if online==0:
            self.title = "😀 " + self._isp
        else:
            self.title = "🚫"

    def getIspStatus(self):
        response = requests.get("http://ifconfig.co/asn")
        if '6830' in response.text:
            self._isp = "Fiber"
        else:
            self._isp = "LTE"

    @rumps.timer(5)
    def updatePingStatus(self,sender):
        thread = threading.Thread(target=self.getPingStatus)
        thread.start()

    @rumps.timer(10)
    def updateIspStatus(self,sender):
        thread = threading.Thread(target=self.getIspStatus)
        thread.start()

if __name__ == '__main__':
    netStatus().run()


