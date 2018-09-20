import random

final_home = [ ]
locations = {
    'louiville':'ky',
    'california':'sanfran',
    'new york': 'timesquare'
    }
colors = {
    'c1': 'blue',
    'c2': 'black',
    'c3': 'white',
    'c4': 'red'
    }

version = {
    'v1': 'manison',
    'v2': 'apartment',
    'v3': 'hotel'
    }

print ( "welcome to make a new home")
while True:
    user_name = input("please type your name or press x to exit")
    if user_name == "x":
            break
    else:
            print (" Hi %s you will be given a random location"%(user_name))
print ("%s is the location for your house"%(random.choice(locations.keys))
               
def build_house(color,style):
    build_house.split(",")
    for key,value in colors.items():
        color = input ("Here are a list of colors, pick one(type c than number to pick one) %s %s"%(key,value))
            if color == 'black':
                return "c2"
            elif color == 'blue':
                return "c1"
            elif color == 'white':
                return ""
            elif color == 'red':
                return "red paint"
    for key,value in version.item():
        style = input ("also choose a style for you house (t %s"%(version))
            if style == 'mansion':
                return "mansion home"
            elif style == 'apartment':
                return "apartment home"
            elif style == 'hotel':
                return "hotel home"
final_home.append( "%s,%s"%(color,style))
                                            
print ("Here is you new home %s"%(final_home))   
                                    
