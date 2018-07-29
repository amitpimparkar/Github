#Currency Converter
@interact(from_currency=['USD','GBP','INR','EUR','JPY'],to_currency=['USD','GBP','INR','EUR','JPY'],rate=(1,100,0.1),amount=(1,100,1))
def currency_converter(from_currency,to_currency,rate,amount):
    fin_amt=amount*rate
    print(fin_amt)
    return ( from_currency,to_currency,rate,amount)