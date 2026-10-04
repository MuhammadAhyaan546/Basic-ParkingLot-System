import datetime
#baseclass
class vehicle:
    def __init__(self,licenseplate,sizelevel):
        self.licenseplate=licenseplate
        self.sizelevel=sizelevel

#classmotorcycle
class motorcycle(vehicle):
    def __init__(self,licenseplate):
        super().__init__(licenseplate,1)

#classcar
class car(vehicle):
    def __init__(self,licenseplate):
        super().__init__(licenseplate,2)

#classparkingspot
class parkingspot:
    def __init__(self,spotid,spotsize):
        self.spotid=spotid
        self.spotsize=spotsize
        self.vehicle_=None

    #isavailablefunction
    def isavailable(self):
        if self.vehicle_==None:
            return True
        else:
            return False

    #canfit function
    def canfit(self,vehicle):
        if self.spotsize >= vehicle.sizelevel and self.isavailable():
            return True
        else:
            return False
    #assignvehicle function
    def assignvehicle(self, vehicle):
        if self.canfit(vehicle):
            self.vehicle_=vehicle
            return True
        else:
            return False

    #removevehicle function
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
        #initializingsmallspots
        for i in range(numsmallspots):
            self._spots.append(parkingspot(f"s-{i+1}",1))
        for i in range(nummediumspots):
            self._spots.append(parkingspot(f"m-{i+1}",2))

    #parkvehicle function
    def parkvehicle(self,vehicle):
        for m in self._spots:
            if m.canfit(vehicle):
                if m.assignvehicle(vehicle):
                    self.ticketcounter+=1
                    ticketid=f"T-{self.ticketcounter}"
                    ticket=parkingticket(ticketid, vehicle.licenseplate, m.spotid)
                    self.activetickets[ticketid]=(ticket,m)
                    return ticket
            else:
                return None
    #unparkvehicle function
    def unparkvehicle(self, ticketid):
        if ticketid in self.activetickets:
            ticket,spot=self.activetickets.pop(ticketid)
            spot.removevehicle()
            return True
        else:
            return False
        #totalavailablespots function
    def totalavailablespots(self):
        smallspots=0
        mediumspots=0
        for i in self._spots:
            if i.isavailable():
                if i.spotsize==1:
                    smallspots+=1
                else:
                    mediumspots+=1
        return {
            "smallspots":smallspots,
            "mediumspots":mediumspots,
            "totalspots":smallspots+mediumspots
            
        }
#adding the objects...
#main code:
#carobjects
policecar=car(licenseplate="A1OB8H")
van=car("4GUJS6")
taxi=car("JFI6L8")
truck=car("HYUR7J")
racecar=car("RTY65O")
taxi2=car("QWC65R")
#motorcycleobjects
motorbike=motorcycle("YHSDA6")
bike=motorcycle("RFEY27")
deliverybike=motorcycle("EDYD6I")
cycle=motorcycle("HDSF84")
motorbike2=motorcycle("NDSJ56")