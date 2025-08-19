import requests

class CurrencyConverter:
    
    #A simple Currency Converter using live exchange rates.
    

    def __init__(self, base_currency="USD"):
        self.base_currency = base_currency
        self.api_url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        self.rates = self.get_exchange_rates()

    def get_exchange_rates(self):

        #Fetch exchange rates from API.

        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return data["rates"]
        except Exception as e:
            print("Error fetching data:", e)
            return {}

    def convert(self, amount, target_currency):

        #Convert amount from base_currency to target_currency.
        
        if target_currency not in self.rates:
            raise ValueError(f"Currency {target_currency} not available.")

        rate = self.rates[target_currency]
        return round(amount * rate, 2)


if __name__ == "__main__":
    print("🌍 Currency Converter 🌍")

    base = ""
    converter = None
    while converter is None or not converter.rates:
        base = input("Enter base currency (e.g., USD, EUR, INR): ").upper()
        converter = CurrencyConverter(base)
        if not converter.rates:
            print(f"Invalid base currency code '{base}' or unable to fetch rates. Please try again.")

    amount = None
    while amount is None:
        try:
            amount_str = input(f"Enter amount in {base}: ")
            amount = float(amount_str)
        except ValueError:
            print("Invalid amount. Please enter a number.")

    target = input("Enter target currency: ").upper()

    try:
        converted = converter.convert(amount, target)
        print(f"{amount} {base} = {converted} {target}")
    except ValueError as e:
        print(e)
