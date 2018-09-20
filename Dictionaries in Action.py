import random
import time

final_home = {

    }
locations = {
    'louiville':'ky',
    'california':'sanfran',
    'new york': 'timesquare'
    }

def house_color(color):
    colors = {
    'c1': 'blue',
    'c2': 'black',
    'c3': 'white',
    'c4': 'red'
    }
    for key,value in colors.items():
        color = input ("Here are a list of colors, pick one(type c than number to pick one) %s %s"%(key,value))
        if color == 'c2':
            return "black paint"
        elif color == 'c1':
            return "blue paint"
        elif color == 'c3':
            return "white paint"
        elif color == 'c4':
            return "red paint"
final_home.update({'final_color':"color"})
            
def house_style(style):
    version = {
    'v1': 'manison',
    'v2': 'apartment',
    'v3': 'hotel'
    }
    for key,value in version.item():
        style = input ("also choose a style for you house (type t than number to pick one)%s"%(key,value))
        if style == 'v1':
            return "mansion home"
        elif style == 'v2':
            return "apartment home"
        elif style == 'v3':
            return "hotel home"
final_home.update({'final_style':"style"})

            

print( "welcome to make a new home")
while True:
    user_name = input("please type your name or press x to exit")
    if user_name == "x":
            break
    else:
            print (" Hi %s you will be given a random location"%(user_name))
    time.sleep(3)
    print("%s is the location for your house" %(random.choice(locations.keys))
          
print("Here is you new home it is"(final_home['final_style']) "also it has"(final_home['final_color']))






