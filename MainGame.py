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