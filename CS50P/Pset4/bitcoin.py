import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not a number")

    try:
        url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=45bc7777f0c56bd354a55a333d9f46ab9b657203e7e6fd764bc8d1c88b5510e5"

        response = requests.get(url)
        data = response.json()

        price = float(data["data"]["priceUsd"])
        cost = n * price

        print(f"${cost:,.4f}")

    except requests.RequestException:
        sys.exit(1)

if __name__ == "__main__":
     main()












