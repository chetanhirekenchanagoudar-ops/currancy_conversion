
# Currency Conversion: INR to USD

exchange_rate = 98

def inr_to_usd(inr):
    usd = inr / exchange_rate
    return round(usd, 2)


amount = float(input("Enter amount in INR: "))

result = inr_to_usd(amount)

print("Indian Rupees:", amount)
print("US Dollars:", result)
