num1 = int(input("Enter your frist number: "))
operator = input("Enter in any math operator: ")
num2 = int(input("Enter in  your second number: "))

if operator == "+":
	total = num1 + num2
	print(f"{num1} + {num2} = {total}")
elif operator == "-":
	total = num1 - num2
	print(f"{num1} - {num2} = {total}")
elif operator == "*":
	total = num1 * num2
	print(f"{num1} * {num2} = {total}")
elif operator == ("/"):
	total = num1 / num2
	print(f"{num1} / {num2} = {total}")
elif operator == "//":
	total = num1 // num2
	print(f"{num1} // {num2} = {total}")
elif operator == "/+":
	total = num1 /+ num2
	print(f"{num1} /+ {num2} = {total}")
elif operator == "/-":
	total = num1 /- num2
	print(f"{num1} /- {num2} = {total}")
elif operator == "**":
	total = num1 ** num2
	print(f"{num1} ** {num2} = {total}")
elif operator == "%":
	total = num1 % num2
	print(f"{num1} % {num2} = {total}")
else:
	print("Try again")