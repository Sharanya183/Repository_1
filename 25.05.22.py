#Price of a house is $1M. If buyer has good credit, they need to put down 10% Otherwise, they need to put down 20%. Print the down payment.#

House_Price = 1000000
credit = input(str("credit(good/bad): "))
if credit == "good":
    downpayment = 0.1*House_Price
else:
    downpayment = 0.2*House_Price
print(f"Down Payment: ${downpayment}")

