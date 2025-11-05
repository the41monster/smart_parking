# Smart Parking Lot System

## Overview

This is a backend system for managing a **smart parking lot**. It handles:

* Vehicle **entry and exit**
* **Automatic parking spot allocation** based on vehicle size
* **Parking fee calculation** using a strategy pattern
* **Real-time availability updates** for parking spots

The system is designed using **object-oriented principles** with a focus on **SRP**, **OCP**, and modularity.

---

## Features

* **Parking Spot Allocation:** Assigns the first available spot on a floor based on vehicle size.
* **Check-In / Check-Out:** Tracks vehicle entry and exit times via tickets.
* **Fee Calculation:** Cost is calculated based on duration and vehicle type.
* **Concurrency Handling:** Supports multiple gates using locks to prevent race conditions.
* **Extensible:** Easily add new vehicle types or pricing rules using factories and cost calculators.

---

## Project Structure

```
smart_parking/
│
├── constants/          # Vehicle and Spot type enums
├── models/             # Vehicle, ParkingSpot, ParkingFloor, ParkingTicket
├── services/           # CostCalculator, ParkingLot, EntryGate, ExitGate
├── factories/          # Vehicle factories for each type
└── main.py             # Demo script
```

---

## Design Patterns Used

* **Factory Pattern:** Creates vehicles of different types (`SmallVehicle`, `MediumVehicle`, `LargeVehicle`).
* **Strategy Pattern:** Vehicle has a `CostCalculator` to compute parking fees.
* **Singleton / Locking:** Ensures safe spot allocation with multiple entry/exit gates.
* **Polymorphism & OCP:** Adding a new vehicle type does not require changes to existing classes.

---

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/the41monster/smart_parking
cd smart_parking
```

2. Run the demo:

```bash
python main.py
```

3. Output will show:

* Tickets generated for vehicles
* Parking costs based on duration
* Current availability of parking spots

---

## Example Output

```
Tickets issued: 1eef3c98-a41b-4f86-bef4-0d2f8fde0276, 5a4a11c9-f4d6-4e28-8dd8-982da4440cce, 048a2c7a-ed21-4c63-bc2c-ca536f77922a
Current Parking Availability: {'F1': {'SMALL': 5, 'MEDIUM': 4, 'LARGE': 2}}
KA-01-HH-1234 parking cost: 10
KA-01-HH-9999 parking cost: 15
KA-01-HH-0001 parking cost: 20
Current Parking Availability: {'F1': {'SMALL': 6, 'MEDIUM': 5, 'LARGE': 3}}
```

---

## Extending the System

* Add new **Vehicle types** by creating a subclass and a factory.
* Add new **CostCalculator** strategies for pricing changes.
* Add multiple floors or entry/exit gates with minimal changes.

---
