from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            finished = False
            while finished is False:
                try:
                    taxi_choice = int(input("Choose taxi: "))
                    finished = True
                except ValueError:
                    print("please enter number")
                    finished = False
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis, 1):
        print("{} - {}".format(i, taxi))


def run_tests():
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    distance = int(input("Drive how far? "))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("Drive how far? "))

    taxi = Taxi("Prius 1", 100)
    print(taxi)
    taxi.drive(25)
    print(taxi, taxi.get_fare())
    taxi.start_fare()
    taxi.drive(40)
    print(taxi, taxi.get_fare())

    silver_service_taxi = SilverServiceTaxi("Limo", 100, 2)
    print(silver_service_taxi, silver_service_taxi.get_fare())
    silver_service_taxi.drive(10)
    print(silver_service_taxi, silver_service_taxi.get_fare())


main()
