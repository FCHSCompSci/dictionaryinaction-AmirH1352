import random

locations = {
    'louiville':ky,
    'california':sanfran,
    'new york': timesquare
    }
colors = {
    c1: 'blue',
    c2: 'black',
    c3: 'white',
    c4: 'red'
    }

version = {
    v1: 'manison',
    v2: 'apartment',
    v3: 'hotel'
    }

print ( "welcome to make a new home")
while True:
    user_name = input("please type your name or press x to exit")
    if user_name == "x":
        break
    else:
        print (" Hi %s you will be given a random location"%(user_name))

print ("%s is your homes location"%(random.choice(locations.keys())
def build_house(color,style):
        color = input ("here are a list of colors, pick one %s"%(colors))
            if color == 'black':
                return "c2"
            elif color == 'blue':
                return "c1"
            elif color == 'white':
                return "c3"
            elif color == 'red':
                return "c4"
                                    
