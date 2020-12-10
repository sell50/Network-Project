import os

#This program answers the first one-to-one job
class IPOnlineDetection(object):

    def detectIPStatus(self, targetIP):

        rep = os.system('ping ' + targetIP)

        if rep == 0:
            return "Target IP: "+targetIP + " Online"
        else:
            return "Target IP: "+targetIP + " Offline"