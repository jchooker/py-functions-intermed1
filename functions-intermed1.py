import random
#input function with min as first value, max as second
def inputMinMax():
    a = {}
    #input receives two values max from user
    prompt_txt = "Please provide min value: "
    try:
        user_input = int(input(prompt_txt))
        a["min"] = user_input
    except:
        print("Invalid entry, using default 0 value for min")
        a["min"] = None
    prompt_txt = "Please provide max value: "
    try:
        user_input = int(input(prompt_txt))
        a["max"] = user_input
    except:
        print("Invalid entry")
        a["max"] = None
    return a

def randInt(min=0, max=100):
    if min < 0 and max < 0:
    #edge case: min > max - both numbers provided by user
        if min > max:
            minTemp = 0
            minTemp = min
            min = max
            max = minTemp
            print("Max and min reversed!")
        num = (random.random()*(min*-1)+(max*-1))*-1
            
    elif min > max:
        minTemp = 0
        minTemp = min
        min = max
        max = minTemp
        print("Max and min reversed!")
    else:
        num = random.random()*max+min
    return round(num)
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
minMax = inputMinMax()
if (minMax["min"] != None) and (minMax["max"] != None):
    print(randInt(min=minMax["min"],max=minMax["max"]))
elif (minMax["min"] == None) and (minMax["max"] != None): 
    print(randInt(max=minMax["max"]))
elif (minMax["min"] != None) and (minMax["max"] == None): 
    print(randInt(min=minMax["min"]))
else:
    print(randInt())
