final_home = {

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
    final_home['final_color'] = "color"
            
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
    final_home['final_style'] = "style"

def house_location(place):
    locations = {
    'louiville':'ky',
    'california':'sanfran',
    'new york': 'timesquare'
    }
    for key, value in location.item():
        place = input ("Finally pick a spot for your house we are limited for areas so pick carefully %s"%(key, value))
        if place == 'ky':
            return "louisville"
        elif place == 'sanfran':
            return "california"
        elif place == 'timesquare':
            return "new york"
        final_home['final_location'] = "place"

            

print( "welcome to make a new home")
print("lets begin making your new home")

while True:
    user_name = input("please type your name or press x to exit")
    if user_name == "x":
            break
    else:
        print("alright %s lets build a house"%(user_name))
    def house_location(place):
        def house_color(color):
            def house_style(style):
            

print("Here is your new home it is final_home['final_style']:",final_home['final_style'])
    print("it is colored with final_home['final_color']:",final_home['final_color'])
    print("it is located at final_home[final_location]:",final_home['final_location'])






