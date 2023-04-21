#!/bin/python3

num_hairstyles = int(input("Enter the number of hairstyles: "))

hairstyles = []
prices = []
last_week = []

for i in range(num_hairstyles):
    name = input(f"Enter the name of haircut #{i+1}: ")
    hairstyles.append(name)
    
    price = float(input(f"Enter the price of {name}: "))
    prices.append(price)

    last_week.append(int(input(f"How many people got {name} last week? ")))

print("Hairstyles:", hairstyles)
print("Prices:", prices)

total_price = sum(prices)
num_prices = len(prices)
average_price = total_price / num_prices
print("Average Haircut Price:", average_price)

new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: {}".format(total_revenue))
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: {}".format(average_daily_revenue))