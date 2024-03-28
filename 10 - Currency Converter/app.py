def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another based on given exchange rates.
    """
    if from_currency == to_currency:
        return amount

    if from_currency not in rates or to_currency not in rates:
        print(f"Error: Exchange rates not available for {from_currency} or {to_currency}")
        return None

    from_rate = rates[from_currency]
    to_rate = rates[to_currency]

    # Convert to USD first
    usd_amount = amount / from_rate

    # Convert USD to target currency
    converted_amount = usd_amount * to_rate

    return converted_amount

def main():
    # Example exchange rates (1 USD = ?)
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.81,
        "JPY": 133.85,
        "AUD": 1.49,
        "CAD": 1.36,
        "CHF": 0.92,
        "CNY": 6.96,
        "HKD": 7.85,
        "NZD": 1.60
    }

    while True:
        amount = input("Enter the amount to convert: ")
        if not amount:
            break

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        from_currency = input("From (currency code): ").upper()
        to_currency = input("To (currency code): ").upper()

        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        if converted_amount is not None:
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()