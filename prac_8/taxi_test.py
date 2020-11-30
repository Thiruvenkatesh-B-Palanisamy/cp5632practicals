from taxi import Taxi


def main():

    prius_taxi = Taxi("Prius 1", 100)
    prius_taxi.drive(40)
    print(prius_taxi)
    prius_taxi.start_fare()
    prius_taxi.drive(100)
    print(prius_taxi)


main()

