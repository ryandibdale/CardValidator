def card_number():
    while True:
        try:
            cn = int(input("Please enter your 16 digit card number "))
        except:
            print("This is not a valid format")
        else:
            if len(str(cn)) == 16:
                return cn
            else:
                continue

def validate_card(n=0):
    n = card_number()
    numbers = [int(x) for x in str(n)]
    final_num = numbers[-1]
    numbers.pop()
    doubles = [x * 2 for x in numbers[::2]]
    final_doubles = []

    for num in doubles:
        if num < 9:
            final_doubles.append(num)
        elif num > 9:
            final_doubles.append(int(str(num)[0]) + int(str(num)[1]))

    for index, num in enumerate(numbers):
        if index % 2 == 0:
            numbers[index] = final_doubles[0]
            final_doubles.pop(0)

    first_15_total = 0

    for num in numbers:
        first_15_total = first_15_total + num

    final_total = first_15_total + final_num

    if (final_total) % 10 == 0:
        print("True")
        return True
    else:
        print("False")
        return False

if __name__ == '__main__':
    validate_card()
