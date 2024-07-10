# Variables
left_number = float(input("Saisir le nombre de gauche"))
right_number = float(input("Saisir le nombre de droite"))
operation = (input("Saisir l'operation, si addition +, si soustraction -, si multiplication *, si division / "))

match operation:
    case '+':
        print('Addition')
    case '-':
        print('Soustraction')
    case '*':
        print('Multiplication')
    case '/':
        print('Division')
result = 0
# Check if numbers are int or float
if not isinstance(left_number, (int, float)) or not isinstance(right_number, (int, float)):
    print("Erreur: les deux nombres doivent être des nombres entiers ou flottants.")
else:
# Check if symbols are valids
    if operation not in ["+", "-", "*", "/"]:
        print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    else:
# Make the operation
        if operation == "+":
            result = left_number + right_number
        elif operation == "-":
            result = left_number - right_number
        elif operation == "*":
            result = left_number * right_number
# Specific
        if operation == '/' and right_number == 0:
            print('Impossible de diviser par 0')
        elif operation == "/":
           result = left_number / right_number
# Print result
        print(f"L’écriture de l'opération est: {left_number} {operation} {right_number} = ")
        print(f"Le résultat de l'opération est: {result}")
