#Code to retrieve googlesearch entries for the keyword entered.
def googlesearch():
        try:
            import googlesearch
        except:
            print("No Such module named 'googlesearch' found")
            
        keyword = input('Enter the Keyword for search: ')

        noe=int(input('Please enter number of entries to retrieve: '))
        print('\n')
        print(f'For the Keyword "{keyword}" below are the {noe} entries:-')

        for j in googlesearch.search(keyword, tld="co.in", num=noe, stop=1, pause=2):

            print(j)