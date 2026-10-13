number = int(input("Enter the number of items: "))
price = float(input("Enter the price of the item: "))
total_price = number * price
print("The total cost is:" , total_price)

if total_price > 10:
    print("She is spending too much!!")
elif number >= 5:
    print("Gertrude is drinking an unhealthy amount of soda...")