from math import pi

def calculateAreaCircle(radius):
    area = pi * (radius ** 2)
    return round(area, 2)

def calculateTaxes(money, taxRate):
    totalDue = money + (money * (taxRate/100))
    return round(totalDue, 2)

def fahrenheitToCelsius(temperature):
    celsius = (temperature - 32) * (5/9)
    if celsius == 0:
        return int(celsius)
    else:
        return round(celsius, 4)

def main():
    radius = float(input("Enter the radius of the circle: "))
    print("The area of the circle is:", calculateAreaCircle(radius))
    print()

    money = float(input("Enter the amount of money: "))
    taxRate = float(input("Enter the tax rate: "))
    print("The total due is: %.2f " % calculateTaxes(money, taxRate))
    print()

    temperature = float(input("Enter the temperature in Fahrenheit: "))
    print("The temperature in celsius is: ", fahrenheitToCelsius(temperature))
    print()

main()

