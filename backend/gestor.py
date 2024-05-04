from satellite import Satellite
import json


class Gestor:
    def __init__(self):
        self.satlist = []

    def encontrarSateliteConId(lista, id_buscado):
        for sat in lista:
            if sat.getId() == id_buscado:
                return sat
        return None

    #Update the sat correspondent to that data
    def actualizar(self, data):
        id = (data["svid"],data["constellationType"])
        sat = self.encontrarSateliteConId(self.satlist,id)

        if sat is None: #El satelite está
            sat = Satellite(id)
            self.satlist.append(sat)

        sat.setStats(data["cn0DbHz"],data["agcDb"],data["azimuthDegrees"],data["elevationDegrees"])

        return 0
    
    #Delete all the sats updated > timeMargin seconds ago
    def deleteOldSats(self, timeMargin):
        for sat in self.satlist:
            if sat.wasUpdatedMoreThanAgo(timeMargin):
                self.satlist.pop(sat)
    
    
    def getSats(self):
        satellite_dicts = [sat.computeAndCompress() for sat in self.satlist]
        s = ""
        json.dump(satellite_dicts, s, indent=4)
        return s


