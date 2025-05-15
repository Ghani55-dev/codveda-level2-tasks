# Import the requests module to make HTTP calls
import requests

# Function to fetch and display the current price of a cryptocurrency
def fetch_price(coin):
    # Format the API endpoint URL with the user's input coin
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr"
    
    try:
        # Send the GET request to the CoinGecko API
        response = requests.get(url)
        
        # If the response is an error (e.g., 404 or 500), raise an exception
        response.raise_for_status()

        # Parse the JSON response from the API
        data = response.json()

        # IF statement: Check if the entered coin exists in the response
        if coin in data:
            price = data[coin]["inr"]  # Get the inr price from the data
            print(f"💰 Current price of {coin.capitalize()}: ₹{price}")
            

        else:
            # Coin name is not found in the response
            print("❌ Invalid coin name or data not found.")

    # EXCEPT block catches errors like connection issues or invalid responses
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching data: {e}")

# Main function to run the program
def main():
    # Ask the user to input the coin name (e.g., bitcoin)
    coin = input("Enter cryptocurrency (e.g., bitcoin, ethereum): ").lower()
    fetch_price(coin)  # Call the function to fetch and display the price

# Run the program if this script is the main entry point
if __name__ == "__main__":
    main()
