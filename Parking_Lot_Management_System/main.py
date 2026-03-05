from services.parking_lot import ParkingLot

parking = ParkingLot()

parking.add_slot(1,"CAR")
parking.add_slot(2,"BIKE")
parking.add_slot(3,"TRUCK")

while True:

    print("\n1 Park Vehicle")
    print("2 Exit Vehicle")
    print("3 Exit")

    choice=input("Enter choice: ")

    if choice=="1":

        number=input("Vehicle Number: ")
        vtype=input("Vehicle Type (CAR/BIKE/TRUCK): ")

        parking.park_vehicle(number,vtype)

    elif choice=="2":

        ticket=int(input("Enter Ticket ID: "))
        parking.exit_vehicle(ticket)

    elif choice=="3":
        break