def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def octal_to_decimal(octal):
    decimal = 0
    for digit in octal:
        decimal = decimal * 8 + int(digit)
    return decimal

def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    for digit in hexadecimal:
        decimal = decimal * 16 + int(digit, 16)
    return decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def decimal_to_octal(decimal):
    if decimal == 0:
        return "0"
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal > 0:
        hexadecimal = hex_digits[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal

def is_valid_binary(binary):
    return all(d in '01' for d in binary)

def is_valid_octal(octal):
    return all(d in '01234567' for d in octal)

def is_valid_decimal(decimal):
    return decimal.isdigit()

def is_valid_hexadecimal(hexadecimal):
    return all(c in '0123456789ABCDEF' for c in hexadecimal.upper())

def perform_operation(num1, num2, base, operator):
    if base == "binary":
        decimal1 = binary_to_decimal(num1)
        decimal2 = binary_to_decimal(num2)
    elif base == "octal":
        decimal1 = octal_to_decimal(num1)
        decimal2 = octal_to_decimal(num2)
    elif base == "decimal":
        decimal1 = int(num1)
        decimal2 = int(num2)
    elif base == "hexadecimal":
        decimal1 = hexadecimal_to_decimal(num1)
        decimal2 = hexadecimal_to_decimal(num2)
    else:
        print("Invalid number system.")
        return

    if operator == '+':
        result = decimal1 + decimal2
    elif operator == '-':
        result = decimal1 - decimal2
    elif operator == '*':
        result = decimal1 * decimal2
    elif operator == '/':
        if decimal2 == 0:
            print("Error: Division by zero.")
            return
        result = decimal1 // decimal2
    else:
        print("Invalid operator.")
        return

    print(f"Result in decimal: {result}")
    print(f"Result in binary: {decimal_to_binary(result)}")
    print(f"Result in octal: {decimal_to_octal(result)}")
    print(f"Result in hexadecimal: {decimal_to_hexadecimal(result)}")

def main():
    while True:
        print("What do you want to do?")
        print("[1] +")
        print("[2] -")
        print("[3] ×")
        print("[4] ÷")
        print("[5] Convert numbering system from one to another")
        choice = input("Your choice (1-5): ")

        if choice in {'1', '2', '3', '4'}:
            operator = '+' if choice == '1' else '-' if choice == '2' else '*' if choice == '3' else '/'
            print("What number system's operation do you want?")
            print("[1] Binary")
            print("[2] Octal")
            print("[3] Decimal")
            print("[4] Hexadecimal")
            num_system_choice = input("Your choice (1-4): ")

            if num_system_choice == '1':
                base = "binary"
                num1 = input("Enter the first binary number: ")
                num2 = input("Enter the second binary number: ")
                if not is_valid_binary(num1) or not is_valid_binary(num2):
                    print("Invalid binary number.")
                    continue
            elif num_system_choice == '2':
                base = "octal"
                num1 = input("Enter the first octal number: ")
                num2 = input("Enter the second octal number: ")
                if not is_valid_octal(num1) or not is_valid_octal(num2):
                    print("Invalid octal number.")
                    continue
            elif num_system_choice == '3':
                base = "decimal"
                num1 = input("Enter the first decimal number: ")
                num2 = input("Enter the second decimal number: ")
                if not is_valid_decimal(num1) or not is_valid_decimal(num2):
                    print("Invalid decimal number.")
                    continue
            elif num_system_choice == '4':
                base = "hexadecimal"
                num1 = input("Enter the first hexadecimal number: ")
                num2 = input("Enter the second hexadecimal number: ")
                if not is_valid_hexadecimal(num1) or not is_valid_hexadecimal(num2):
                    print("Invalid hexadecimal number.")
                    continue
            else:
                print("Invalid choice.")
                continue

            perform_operation(num1, num2, base, operator)

        elif choice == '5':
            print("What type of number do you want to convert?")
            print("[1] Binary")
            print("[2] Octal")
            print("[3] Decimal")
            print("[4] Hexadecimal")
            num_type_choice = input("Your choice (1-4): ")

            if num_type_choice == '1':
                binary = input("What is the binary number? ")
                if is_valid_binary(binary):
                    decimal = binary_to_decimal(binary)
                    print(f"Decimal: {decimal}")
                    print(f"Octal: {decimal_to_octal(decimal)}")
                    print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
                else:
                    print("Invalid binary number.")
            elif num_type_choice == '2':
                octal = input("What is the octal number? ")
                if is_valid_octal(octal):
                    decimal = octal_to_decimal(octal)
                    print(f"Decimal: {decimal}")
                    print(f"Binary: {decimal_to_binary(decimal)}")
                    print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
                else:
                    print("Invalid octal number.")
            elif num_type_choice == '3':
                decimal = input("What is the decimal number? ")
                if is_valid_decimal(decimal):
                    decimal = int(decimal)
                    print(f"Binary: {decimal_to_binary(decimal)}")
                    print(f"Octal: {decimal_to_octal(decimal)}")
                    print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
                else:
                    print("Invalid decimal number.")
            elif num_type_choice == '4':
                hexadecimal = input("What is the hexadecimal number? ")
                if is_valid_hexadecimal(hexadecimal):
                    decimal = hexadecimal_to_decimal(hexadecimal)
                    print(f"Decimal: {decimal}")
                    print(f"Binary: {decimal_to_binary(decimal)}")
                    print(f"Octal: {decimal_to_octal(decimal)}")
                else:
                    print("Invalid hexadecimal number.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid operation choice.")

        print("\n=== Press Enter to continue ===\n")
        input()

if __name__ == "__main__":
    main()
