
    # FIX 2: Fixed the variable names and added 'f' to string interpolation
    print(f"Taxi {taxi.licenseplate} has been parked!") 
    print(f"Ticket ID: {ticket1.ticketid} | Spot ID: {ticket1.spotid}") 
else: 
    print("Parking Failed")

print("Remaining spots:", LotNRoll.totalavailablespots())
