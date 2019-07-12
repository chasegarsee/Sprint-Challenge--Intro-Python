# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # Parent
    pass


class FlightVehicle(Vehicle):  # Child
    pass


class Starship(FlightVehicle):  # Grandchild of Vehicle // Child of FlightVehicle
    pass


class Airplane(FlightVehicle):  # Grandchild of Vehicle // Child of FlightVehicle
    pass


class GroundVehicle(Vehicle):  # Child of Vehicle
    pass


class Car(GroundVehicle):  # Grandchild of Vehicle // Child of GroundVehicle
    pass


class Motorcycle(GroundVehicle):  # Grandchild of Vehicle // Child of GroundVehicle
    pass
