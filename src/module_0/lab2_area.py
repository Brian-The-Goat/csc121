# Refer to this module's readme
def area(legnth, width):
    print(str(legnth * width) + "square feet")
    return legnth * width


def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + " square feet")


main()