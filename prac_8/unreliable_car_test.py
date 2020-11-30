from unreliable_car import UnreliableCar


def main():
    nice_car = UnreliableCar("Mostly Good", 100, 80)
    not_nice_car = UnreliableCar("bad", 100, 8)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(nice_car.name, nice_car.drive(i)))
        print("{:12} drove {:2}km".format(not_nice_car.name, not_nice_car.drive(i)))

    print(nice_car)
    print(not_nice_car)


main()

