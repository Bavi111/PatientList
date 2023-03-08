import pandas as pd


pdx = pd.read_excel("") # copy the path of the excel file and enter in quotes add double slashes
wx = pdx['weight'].values.tolist()  # extracts 'weight' column to a list
rx = pdx['name'].values.tolist()    # extracts 'names' column to a list
hx = pdx['height'].values.tolist()   # extracts 'height' column to a list

pass

def new_funct(rx, wx):
    oldlist = []
    wtdict = {}
    htdict = {}
    newdict = {}

    for r, h, w in zip(rx, hx, wx):
        wtdict[r] = w
        htdict[r] = h
        newdict[r] = w,h

    
    weight = 0
    for x in wx:
        weight += x

    average1 = weight/len(wtdict)

    height = 0
    for z in hx:
        height += x

    average2 = height/len(htdict)

    oldlist.append(newdict)

    oldlist.append(f'Average weight: {average1} in lbs, Average height: {average2} in inches') 

    print('\n',oldlist)

    def bMI(wtdict, htdict):

        name = input('\nEnter name: ')

        if name in rx:

            heit = htdict[name]
            weit = wtdict[name]

            calc = (weit/(heit ** 2))*703

            if calc <= 16:
                print("\nYou are severely underweight")

            elif calc <= 18:
                print("\nYou are underweight")

            elif calc <= 25:
                print("\nYou are Healthy")

            elif calc <= 30:
                print("\nYou are overweight")

            else:
                print("\nYou are severely overweight")

        else:
            print('\nno info found under: ', name)
    bMI(wtdict, htdict)

new_funct(rx, wx)

#the function uses for loops to respectively add the height and weight per name to the dict
#made seperate dicts for height and weight so it's easier to call for BMI, then use equation to calculate BMI
#used loops to add and also find the respective averages