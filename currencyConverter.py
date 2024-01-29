import requests
def currecyconverter():
    fromcurrency = input('Enter currency you want to convert from:').upper()
    tocurrency = input('Enter currency  you want to convert to:').upper()
    amountoconvert = int(input('Enter the amount you want to convert'))

    params = {'from': fromcurrency, 'to': tocurrency, 'apikey': 'fca_live_TDO7ZRKdYqedxrK7oRWmAylsD85i2Box1hCCgO12'}
    url= 'https://api.freecurrencyapi.com/v1/latest?'
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code == 200:
            convectionrates = data['data'][tocurrency]
            newamount = amountoconvert * convectionrates
            print(f"{amountoconvert} {fromcurrency} is {newamount} {tocurrency}")
        else:
            print(f'Error: {response.status_code} - {data["error"]}')
    except requests.exceptions.RequestException as e:
        print(f"the Error : {e}")

if __name__ == "__main__":
    currecyconverter()
        
