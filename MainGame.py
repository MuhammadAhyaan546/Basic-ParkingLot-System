import datetime
#baseclass
class vehicle:
    def __init__(self,licenseplate,sizelevel):
        self.licenseplate=licenseplate
        self.sizelevel=sizelevel

#classmotorcycle
class motorcycle:
    def __init__(licenseplate):
        super.__init__(licenseplate,1)

#classcar
class car:
    def __init__(licenseplate):
        super.__init__(licenseplate,2)

#classparkingspot
class parkingspot:
    def __init__(self,spotid,spotsize):
        self.spotid=spotid
        self.spotsize=spotsize
        self.vehicle_=None

    def isavailable(self):
        if self.vehicle_==None:
            return True
        else:
            return False

    def canfit(self,vehicle):
        if self.spotsize >= vehicle.sizelevel and self.isavailable():
            return True
        else:
            return False

    def assignvehicle(self, vehicle):
        if self.canfit(vehicle):
            self.vehicle_=vehicle
            return True
        else:
            return False

    def removevehicle(self):
        vehicle=self.vehicle_
        self.vehicle_=None
        return vehicle

#classparkingticket
class parkingticket:
    def init(self, ticketid, licenseplate, spotid):
        self.ticketid = ticketid
        self.licenseplate = licenseplate
        self.spotid = spotid
        self.entrytime = datetime.datetime.now()

#classparkinglot
class parkinglot:
    def init(self, numsmallspots,nummediumspots):
        self._spots=[]
        self.activetickets=dict()
        self.ticketcounter=1000