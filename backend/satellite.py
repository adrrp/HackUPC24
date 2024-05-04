import datetime

"""
Input json (nombre)
-time
-timeError
-svid
-constellationType
-cn0DbHz
-agcDb
-deviceLongitude
-deviceLatitude
-azimuthDegrees
-elevationDegrees

"""

class Satellite():

    def __init__(self):
        self.id = None
        self.cn0 = None
        self.agcDb = None
        self.azimuth = None
        self.elevation = None
        self.lastUpdate = datetime.datetime.now()

    def setId(self, svid, const):
        self.id = (svid, const)
        self.lastUpdate = datetime.datetime.now()

#    def setCn0(self, cn0):
#        self.cn0 = cn0
#
#    def setAgcDb(self, agc):
#        self.agcDb = agc
#
#    def setAzimuth(self, az):
#        self.azimuth = az
#
#    def setElevation(self, el):
#        self.elevation = el
        
    def setStats(self, cn0, agc, az, el):
        self.cn0 = cn0
        self.agcDb = agc
        self.azimuth = az
        self.elevation = el
        self.lastUpdate = datetime.datetime.now()

    #Getters
    def getId(self):
        return self.id

    def getCn0(self):
        return self.cn0

    def getAgcDb(self):
        return self.agcDb

    def getAzimuth(self):
        return self.azimuth

    def getElevation(self):
        return self.elevation
    
    def wasUpdatedMoreThanAgo(self, sec):
        return datetime.datetime.now() - self.lastUpdate > datetime.timedelta(seconds=sec)


    def computeAndCompress(self):
        return {
            'id': self.id,
            'cn0': self.cn0,
            'agcDb': self.agcDb,
            'azimuth': self.azimuth,
            'elevation': self.elevation
        }