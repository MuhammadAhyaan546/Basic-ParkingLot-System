import datetime

# Baseclass 
class vehicle: 
    def __init__(self, licenseplate, sizelevel): 
        self.licenseplate = licenseplate 
        self.sizelevel = sizelevel 

# Class Motorcycle
class motorcycle(vehicle): 
    def __init__(self, licenseplate): 
        super().__init__(licenseplate, 1) 

# Class Car
class car(vehicle): 
    def __init__(self, licenseplate): 
        super().__init__(licenseplate, 2) 

# Class ParkingSpot
class parkingspot: 
    def __init__(self, spotid, spotsize): 
        self.spotid = spotid 
        self.spotsize = spotsize 
        self.vehicle_ = None 

    def isavailable(self): 
        return self.vehicle_ is None 

    def canfit(self, vehicle): 
        return self.spotsize >= vehicle.sizelevel and self.isavailable() 

    def assignvehicle(self, vehicle): 
        if self.canfit(vehicle): 
            self.vehicle_ = vehicle 
            return True 
        return False 

    def removevehicle(self): 
        vehicle = self.vehicle_ 
        self.vehicle_ = None 
        return vehicle 

# Class ParkingTicket
class parkingticket: 
    def __init__(self, ticketid, licenseplate, spotid): 
        self.ticketid = ticketid 
        self.licenseplate = licenseplate 
        self.spotid = spotid 
        self.entrytime = datetime.datetime.now() 

# Class ParkingLot
class parkinglot: 
    def __init__(self, numsmallspots, nummediumspots): 
        self._spots = [] 
        self.activetickets = dict() 
        self.ticketcounter = 1000 

        # Initializing spots
        for i in range(numsmallspots): 
            self._spots.append(parkingspot(f"s-{i+1}", 1)) 
        for i in range(nummediumspots): 
            self._spots.append(parkingspot(f"m-{i+1}", 2)) 

    def parkvehicle(self, vehicle): 
        for m in self._spots: 
            if m.canfit(vehicle): 
                # FIX 1: Changed self.vehicle to vehicle
                if m.assignvehicle(vehicle): 
                    self.ticketcounter += 1 
                    ticketid = f"T-{self.ticketcounter}" 
                    ticket = parkingticket(ticketid, vehicle.licenseplate, m.spotid) 
                    self.activetickets[ticketid] = (ticket, m) 
                    return ticket 
        return None 

    def unparkvehicle(self, ticketid): 
        if ticketid in self.activetickets: 
            ticket, spot = self.activetickets.pop(ticketid) 
            spot.removevehicle() 
            return True 
        return False 

    def totalavailablespots(self): 
        smallspots = 0 
        mediumspots = 0 
        for i in self._spots: 
            if i.isavailable(): 
                if i.spotsize == 1: 
                    smallspots += 1 
                else: 
                    mediumspots += 1 
        return { 
            "smallspots": smallspots, 
            "mediumspots": mediumspots, 
            "totalspots": smallspots + mediumspots 
        } 

# --- Main Code Execution ---
policecar = car(licenseplate="A1OB8H") 
van = car("4GUJS6") 
taxi = car("JFI6L8") 
truck = car("HYUR7J") 
racecar = car("RTY65O") 
taxi2 = car("QWC65R") 

LotNRoll = parkinglot(5, 6) 
print("Initial spots:", LotNRoll.totalavailablespots()) 

ticket1 = LotNRoll.parkvehicle(taxi) 
if ticket1: 
    # FIX 2: Fixed the variable names and added 'f' to string interpolation
    print(f"Taxi {taxi.licenseplate} has been parked!") 
    print(f"Ticket ID: {ticket1.ticketid} | Spot ID: {ticket1.spotid}") 
else: 
    print("Parking Failed")

print("Remaining spots:", LotNRoll.totalavailablespots())
