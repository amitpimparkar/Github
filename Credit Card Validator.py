#Credit Card Validator
def val_cc():
    total=0
    cc = str(input("Enter a credit card number to validate (Mastercard, Visa,Rupay,Amex only): "))
    cc_rev = cc[::-1]
    rev=cc_rev[1::2]
    #print(cc_rev)
    #print(rev)
    for i in rev:
        x=int(i)*2 #18
        if len(str(x))==2:
            for a in str(x):
                total+=int(a)
        else:
            total+=int(x)
            
    #print(total)
            
    for i in cc_rev[::2]:
        total+=int(i)
        
        
    #print(total)
    
    if total%10==0:
        print('Credit Card is Valid!')
    else:
        print('Credit Card is Not Valid!')
        
    #Account Number 
    #Taking away the 6 identifier digits and the last digits, remaining digits are the person’s account number 
    #(7th and following excluding last digits)
    
    Account_Number=cc[6:-1]
    
    print(f'Account Number: {Account_Number}')
        
    #Major Industry Identifier (MII).
    #The first digit of the credit card number is the Major Industry Identifier (MII). 
    #It designates the category of the entry which issued the card.
    
    if cc[0]=='1' or cc[0]=='2':
        print('Industry : Airlines')
    elif cc[0]=='3':
        print('Industry : Travel')
    elif (cc[0]=='4' or cc[0]=='5'):
        print('Industry : Banking & Financials')
    elif cc[0]=='6':
        print('Industry : Merchandising')
    elif cc[0]=='7':
        print('Industry : Petroleum')
    elif cc[0]=='8':
        print('Industry : Healthcare')
    else:
        print('Industry : National Assignment')
        
    #Issuer Identification Number
    #The first 6 digits are the Issuer Identification Number. 
    #It will identify the institution that issued the card. 
    
    if cc[:2]=='34' or cc[:2]=='37':
        print('Issuer : Amex')
    elif cc[:1]=='4':
        print('Issuer : Visa')
    elif cc[:2]=='51' or cc[:2]=='55':
        print('Issuer : MasterCard')
    else:
        print('Issuer : RuPay')