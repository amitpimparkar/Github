#Horoscope Calculator

def zodiac_sign():
    
    try:
        



        user=input('Provide your Name: ')
        print('\n'*1)
        day=int(input('Provide your Day of Birth: [1-31]'))
        print('\n'*1)
        month=input('Provide your Month of Birth: [January-December]')
        print('\n'*1)

        if month.capitalize() == 'December':
            if (day < 22):
                astro_sign = 'Sagittarius'
                num==9
            else:
                astro_sign = 'capricorn'
                num==10

        elif month.capitalize() == 'January':
            if (day < 20):
                astro_sign = 'Capricorn'
                num=10
            else:
                astro_sign='aquarius'
                num=11

        elif month.capitalize() == 'February':
            if (day < 19):
                astro_sign = 'Aquarius'
                num=11
            elif (day <=29):
                astro_sign='pisces'
                num=12


        elif month.capitalize() == 'March':
            if (day < 21):
                astro_sign = 'Pisces'
                num=12
            else:
                astro_sign='aries'
                num=1

        elif month.capitalize() == 'April':
            if (day < 20):
                astro_sign = 'Aries'
                num=1
            else:
                astro_sign='taurus'
                num=2

        elif month.capitalize() == 'May':
            if (day < 21):
                astro_sign = 'Taurus'
                num=2
            else:
                astro_sign='gemini'
                num=3

        elif month.capitalize() == 'June':
            if (day < 21):
                astro_sign = 'Gemini'
                num=3
            else:
                astro_sign='cancer'
                num=4

        elif month.capitalize() == 'July':
            if (day < 23):
                astro_sign = 'Cancer'
                num=4
            else:
                astro_sign='leo'
                num=5

        elif month.capitalize() == 'August':
            if (day < 23):
                astro_sign = 'Leo'
                num=5
            else:
                astro_sign='virgo'
                num=6

        elif month.capitalize() == 'September':
            if (day < 23):
                astro_sign = 'Virgo'
                num=6
            else:
                astro_sign='libra'
                num=7

        elif month.capitalize() == 'October':
            if (day < 23):
                astro_sign = 'Libra'
                num=7
            else:
                astro_sign='scorpio'
                num=8

        elif month.capitalize() == 'November':
            if (day < 22):
                astro_sign = 'scorpio'
                num=8
            else:
                astro_sign='sagittarius'
                num=9

        astro_sign=astro_sign.upper()
        user=user.upper()
        print(f'{user} : Your Zodiac sign is: {astro_sign}')

        print('\n'*1)

        print('Your Horoscope is as below: ')




        print(astro_sign.capitalize())


        url=f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={num}'
        import webbrowser
        webbrowser.open(url, new=0, autoraise=True)


        import requests
        page=requests.get(url)
        #print(page.status_code)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')
        x=soup.find(class_="horoscope-content").get_text()
        newlines=x.split('\n')
        newlines=newlines[:3]
        print(''.join(newlines))
        
    except:
        print('Please Provide Correct Parameters!')
        
    else:
        print('\n'*1)
        
        


    #print(x)
    