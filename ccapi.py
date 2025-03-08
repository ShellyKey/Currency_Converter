def convert_currency(amount, from_currency, to_currency, conversion_rates):
    if from_currency == to_currency:
        return amount  # No conversion needed
    
    # Direct conversion available
    if (from_currency, to_currency) in conversion_rates:
        return amount * conversion_rates[(from_currency, to_currency)]
    
    # Convert via USD if direct rate is missing
    if (from_currency, 'USD') in conversion_rates and ('USD', to_currency) in conversion_rates:
        amount_in_usd = amount * conversion_rates[(from_currency, 'USD')]
        return amount_in_usd * conversion_rates[('USD', to_currency)]
    
    return "Conversion rate not available."

# Define conversion rates with USD as the bridge
conversion_rates = {
    ('INR', 'USD'): 0.012, ('USD', 'INR'): 83.20,
    ('JPY', 'USD'): 0.0091, ('USD', 'JPY'): 110.55,
    ('KRW', 'USD'): 0.00076, ('USD', 'KRW'): 1321.50,
    ('AUD', 'USD'): 0.74, ('USD', 'AUD'): 1.36,
    ('NPR', 'USD'): 0.0075, ('USD', 'NPR'): 133.25,
    ('AED', 'USD'): 0.27, ('USD', 'AED'): 3.67,
    ('EUR', 'USD'): 1.18, ('USD', 'EUR'): 0.85,
    ('GBP', 'USD'): 1.33, ('USD', 'GBP'): 0.75,
    ('MXN', 'USD'): 0.055, ('USD', 'MXN'): 18.20
}

# List of available currencies
currencies = {
    "INR": "Indian Rupee",
    "USD": "United States Dollar",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won",
    "AUD": "Australian Dollar",
    "NPR": "Nepalese Rupee",
    "AED": "UAE Dirham",
    "EUR": "Euro",
    "GBP": "British Pound",
    "MXN": "Mexican Peso"
}

# Display available currencies
print("Available currencies:")
for code, name in currencies.items():
    print(f"{code} - {name}")

# Get user input
from_currency = input("\nEnter the currency code you have: ").upper()
to_currency = input("Enter the currency code you want to convert to: ").upper()
amount = float(input("Enter the amount: "))

# Perform conversion
converted_amount = convert_currency(amount, from_currency, to_currency, conversion_rates)

if converted_amount == "Conversion rate not available.":
    print(f"\n❌ Conversion failed: {converted_amount}")
else:
    print(f"\n✅ {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
