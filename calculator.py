sum = 0

class calculator():


    def Addition(self,number_a):

        global sum

        sum += number_a
        return sum


    def Subtraction(self,number_s):

        global sum

        sum -= number_s
        return sum


    def Multiply(self,number_m):

        global sum

        if sum == 0:
            sum = number_m
            return sum

        else:
            sum = sum * number_m
            return sum



    def Division(self,number_d):

        global sum

        if sum == 0:
            sum = number_d
            return sum

        else:
            sum = sum / number_d
            return sum



    def Exponential(self,number_1,number_e):

        global sum

        sum = number_1 ** number_e
        return sum



    def Factoriel(self,number_f):

        global sum

        if number_f == 0:
            sum = 1
            return sum

        else:
            sum = 1
            for i in range(1,number_f+1):
                sum = sum * i
            return sum


calculator = calculator()

#Screen that shows process
print("""
 ____________________
|_____CALCULATOR_____|
|                    |
|                    |
|   Addition(+)      |
|   Subtration(-)    |
|   Multiply(*)      |
|   Division(/)      |
|   Exponential(^)   |
|   Factoriel(!)     |
|                    |
|   Clear(C)         |
|   Quit(q)          |
|                    |
|____________________|
""")

print(sum)

while True:


    progress = input("Progress:")

    if progress == "q":
        break


    elif progress == "C":
        sum = 0
        print(sum)


    elif progress == "+":

        try:
            number = float(input("Number:"))

        except ValueError:
            print("Enter a number...")

        else:
            print(calculator.Addition(number))



    elif progress == "-":

        try:
            number = float(input("Number:"))

        except ValueError:
            print("Enter a number...")

        else:
            print(calculator.Subtraction(number))



    elif progress == "*":

        try:
            number = float(input("Number:"))

        except ValueError:
            print("Enter a number...")

        else:
            print(calculator.Multiply(number))


    elif progress == "/":

        try:
            number = float(input("Number:"))

        except ValueError:
            print("Enter a number...")

        else:
            print(calculator.Division(number))


    elif progress == "^":

        try:
            number_e = float(input("Exponential number:"))

        except ValueError:
            print("Enter a number...")

        else:
            print(calculator.Exponential(sum,number_e))


    elif progress == "!":

        number = int(sum)       #to get factoriel number must be integer
        print(calculator.Factoriel(number))
