def temperaturConverter():
    print('I can convert tempratures between Fahrenheit and Celsius.\n')
    degreefrom = input('what temperature do you want to convert from?:').lower()
    if degreefrom not in ["fahrenheit","celsius"]:
        degreefrom = input('Your input is not correct try again?').lower()
    degreeto = input('what temperature do you want to convert to?:').lower()
    if degreeto not in ["fahrenheit","celsius"]:
        degreeto = input('Your input is not correct try again?').lower()
    try:
        tempnum = float(input('Enter the temperature number:'))
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return
    holder = tempnum
    
    if degreeto == degreefrom:
        print(f"{holder} {degreefrom} is converted to {tempnum} {degreeto}.")

    if degreeto == 'fahrenheit' and degreefrom == 'celsius':
       tempnum = tempnum *9/5 + 32
    elif degreeto == 'celsius' and degreefrom == 'fahrenheit':
       tempnum = (tempnum - 32) * 5/9

    print(f"{holder} {degreefrom} is converted to {tempnum} {degreeto}.")

temperaturConverter()




