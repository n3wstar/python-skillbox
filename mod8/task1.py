class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if isinstance(coordinates, tuple) and len(coordinates) == 2 and all(
                isinstance(coord, (int, float)) for coord in coordinates):
            self._coordinates = coordinates
        else:
            raise ValueError("Coordinates should be a tuple of two numeric values.")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if isinstance(speed, (int, float)):
            self._speed = speed
        else:
            raise ValueError("Speed should be a numeric value.")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError("Brand should be a string.")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self._year = year
        else:
            raise ValueError("Year should be an integer.")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if isinstance(number, str):
            self._number = number
        else:
            raise ValueError("Number should be a string.")

    def __str__(self):
        return f"Transport Info:\n" \
               f"Coordinates: {self._coordinates}\n" \
               f"Speed: {self._speed}\n" \
               f"Brand: {self._brand}\n" \
               f"Year: {self._year} \n" \
               f"Number: {self._number}"

    def is_in_area(self, pos_x, pos_y, length, width) -> bool:
        x, y = self._coordinates
        if pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width:
            return True
        return False


class Passenger:
    def __init__(self):
        self._passengers_capacity = 0
        self._number_of_passengers = 0

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self):
        self._carrying = 0

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    def __str__(self):
        return super().__str__() + f"\nHeight: {self._height}"

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, (int, float)):
            self._height = height
        else:
            raise ValueError("Height should be a numeric value.")


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number, body_type):
        super().__init__(coordinates, speed, brand, year, number)
        self._body_type = body_type

    @property
    def body_type(self):
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        if isinstance(body_type, str):
            self._body_type = body_type
        else:
            raise ValueError("Body type should be a string.")

    def __str__(self):
        return super().__str__() + f"\nBody Type: {self._body_type}"


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port

    def __str__(self):
        return super().__str__() + f"\nPort: {self._port}"

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            self._port = port
        else:
            raise ValueError("Port should be a string.")


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)


class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)

    def __str__(self):
        return Transport().__str__() + f"\nHeight: {self._height}" + f"\nPort: {self._port}"









