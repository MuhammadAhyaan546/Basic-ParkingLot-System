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
#motorcycleobjects
motorbike=motorcycle("YHSDA6")
bike = motorcycle("RFEY27")
deliverybike = motorcycle("EDYD6I")
cycle = motorcycle("HDSF84")
motorbike2=motorcycle("NDSJ56")
garbagetruck=car('JGH564')
tractor=car("HDSF6S")
limousine=car('GSA5SD')
minivan=car("HGA5SF")
forklift=motorcycle("HAS6DA")
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

ticket2 = LotNRoll.parkvehicle(racecar)
if ticket2:
    print(f"Racecar {racecar.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket2.ticketid} | Spot ID: {ticket2.spotid}")
else:
    print("parking failed")

ticket3 = LotNRoll.parkvehicle(policecar)
if ticket3:
    print(f"Policecar {policecar.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket3.ticketid} | Spot ID: {ticket3.spotid}")
else:
    print("parking failed")

ticket4 = LotNRoll.parkvehicle(taxi2)
if ticket4:
    print(f"Taxi2 {taxi2.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket4.ticketid} | Spot ID: {ticket4.spotid}")
else:
    print("parking failed")

ticket5 = LotNRoll.parkvehicle(van)
if ticket5:
    print(f"Van {van.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket5.ticketid} | Spot ID: {ticket5.spotid}")
else:
    print("parking failed")

ticket6 = LotNRoll.parkvehicle(truck)
if ticket6:
    print(f"Truck {truck.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket6.ticketid} | Spot ID: {ticket6.spotid}")
else:
    print("parking failed")

ticket7 = LotNRoll.parkvehicle(motorbike)
if ticket7:
    print(f"Motorbike {motorbike.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket7.ticketid} | Spot ID: {ticket7.spotid}")
else:
    print("parking failed")

ticket8 = LotNRoll.parkvehicle(bike)
if ticket8:
    print(f"Bike {bike.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket8.ticketid} | Spot ID: {ticket8.spotid}")
else:
    print("parking failed")

ticket9 = LotNRoll.parkvehicle(deliverybike)
if ticket9:
    print(f"DeliveryBike {deliverybike.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket9.ticketid} | Spot ID: {ticket9.spotid}")
else:
    print("parking failed")

ticket10 = LotNRoll.parkvehicle(cycle)
if ticket10:
    print(f"cycle {cycle.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket10.ticketid} | Spot ID: {ticket10.spotid}")
else:
    print("parking failed")

ticket11 = LotNRoll.parkvehicle(motorbike2)
if ticket11:
    print(f"MotorBike2 {motorbike2.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket11.ticketid} | Spot ID: {ticket11.spotid}")
else:
    print("parking failed")
print(LotNRoll.totalavailablespots())

ticket12 = LotNRoll.parkvehicle(garbagetruck)
if ticket12:
    print(f"GarbageTruck {garbagetruck.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket12.ticketid} | Spot ID: {ticket12.spotid}")
else:
    print("parking failed")
if ticket10:
    if LotNRoll.unparkvehicle(ticket10.ticketid):
        print(f"Succesfully Unparked {ticket10.ticketid} ")
print(LotNRoll.totalavailablespots())

if ticket12:
    print(f"GarbageTruck {garbagetruck.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket12.ticketid} | Spot ID: {ticket12.spotid}")
else:
    print("parking failed")

if LotNRoll.unparkvehicle(ticket1.ticketid):
    print(f"succesfully unparked {ticket1.ticketid}")
print(LotNRoll.totalavailablespots())

if ticket12:
    print(f"GarbageTruck {garbagetruck.licenseplate} has been parked!")
    print(f"Ticket ID: {ticket12.ticketid} | Spot ID: {ticket12.spotid}")
else:
    print("parking failed")
print(LotNRoll.totalavailablespots())