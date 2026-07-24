import logo 

print(logo)

firstnumber = int(input("What is your first number? "))
op_symbol = input("What operation do you want to do ('+', '-', '*', '/'): ")
secondnumber = int(input("What is your second number? "))


def calculate(n1, n2, operation_symbol):
    if operation_symbol == "+":
        return n1 + n2
    elif operation_symbol == "-":
        return n1 - n2
    elif operation_symbol == "*":
        return n1 * n2 
    elif operation_symbol == "/":
        return n1 / n2
    else:
        return "Invalid operation!"


output = calculate(firstnumber, secondnumber, op_symbol)
print(f"Result: {output}")