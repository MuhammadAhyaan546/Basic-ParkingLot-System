# Parking Lot System

A lightweight, Object-Oriented Parking Lot Management System implemented in Python. This project demonstrates dynamic resource allocation, object-oriented design principles (Inheritance, Polymorphism, and Encapsulation), and physical space compatibility tracking without relying on external dependencies or complex data structures like `Enum`.

---

## Features

* **Dynamic Spot Allocation:** Automatically evaluates incoming vehicles against available physical spots based on vehicle size hierarchy.
* **Flexible Fitting Matrix:** Small vehicles (e.g., Motorcycles) can fit into both Small and Medium spots, while larger vehicles (e.g., Cars) require Medium or larger spots.
* **Automated Ticket Issuance:** Generates unique tracking tickets (`TICK-1001`, `TICK-1002`, etc.) containing entry metadata upon successful parking.
* **Vehicle Unparking & State Release:** Safely releases occupied spots and updates active ticket registries when a vehicle exits.
* **Real-Time Capacity Monitoring:** Tracks available spots segmented by size (`Small`, `Medium`, `Total Available`).

---

## OOP Concepts Demonstrated

### 1. Inheritance
* `Vehicle` serves as the parent class containing baseline properties (`license_plate`, `size_level`).
* `Motorcycle` and `Car` inherit from `Vehicle` and set their size requirements upon instantiation (`1` for Small, `2` for Medium).

### 2. Polymorphism
* The `ParkingSpot.can_fit(vehicle)` method evaluates compatibility dynamically using numerical size levels (`spot_size_level >= vehicle.size_level`).
* The spot accepts any subclass instance derived from `Vehicle` without needing separate methods like `can_fit_car()` or `can_fit_motorcycle()`.

### 3. Encapsulation
* `ParkingSpot` encapsulates the vehicle object reference (`_vehicle`), preventing external code from directly modifying spot occupancy without going through `assign_vehicle()` or `remove_vehicle()`.
* `ParkingLot` hides its internal tracking collections (`_spots`, `_active_tickets`, `_ticket_counter`) behind clean public methods (`park_vehicle`, `unpark_vehicle`, `get_available_spots_count`).

---

## Class Architecture (UML Diagram)

```mermaid
classDiagram
    class Vehicle {
        +String license_plate
        +int size_level
        +Vehicle(license_plate: str, size_level: int)
    }

    class Motorcycle {
        +Motorcycle(license_plate: str)
    }

    class Car {
        +Car(license_plate: str)
    }

    class ParkingSpot {
        +String spot_id
        +int spot_size_level
        -Vehicle _vehicle
        +ParkingSpot(spot_id: str, spot_size_level: int)
        +is_available() bool
        +can_fit(vehicle: Vehicle) bool
        +assign_vehicle(vehicle: Vehicle) bool
        +remove_vehicle() Vehicle
    }

    class ParkingTicket {
        +String ticket_id
        +String spot_id
        +String license_plate
        +DateTime entry_time
        +ParkingTicket(ticket_id: str, spot_id: str, license_plate: str)
    }

    class ParkingLot {
        -List~ParkingSpot~ _spots
        -Dict _active_tickets
        -int _ticket_counter
        +ParkingLot(num_small_spots: int, num_medium_spots: int)
        +park_vehicle(vehicle: Vehicle) ParkingTicket
        +unpark_vehicle(ticket_id: str) bool
        +get_available_spots_count() dict
    }

    Vehicle <|-- Motorcycle : Inherits
    Vehicle <|-- Car : Inherits
    ParkingSpot "1" o-- "0..1" Vehicle : Holds
    ParkingLot "1" *-- "1..*" ParkingSpot : Composes
    ParkingLot "1" o-- "0..*" ParkingTicket : Tracks
