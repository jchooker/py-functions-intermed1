import random
#input function with min as first value, max as second
def inputMinMax():
    a = []
    #input receives two values max from user
    prompt_txt = "Please provide min value: "
    try:
        user_input = int(input(prompt_txt))
        a.append(user_input)
    except:
        print("Invalid entry")
    prompt_txt = "Please provide max value: "
    try:
        user_input = int(input(prompt_txt))
        a.append(user_input)
    except:
        print("Invalid entry")
    return a

def randInt(min=0, max=100):
    #edge case: min > max
    if min > max:
        minTemp = 0
        minTemp = min
        min = max
        max = minTemp
        print("Max and min reversed!")
    num = random.random()*max+min
    # print(f"randInt Min Check: {min}, randInt Max Check: {max}")
    return round(num)
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
minMax = inputMinMax()
if len(minMax) == 2:
    print(randInt(min=minMax[0],max=minMax[1]))
elif len(minMax) == 1: #Accounts for edge case of only one valid entry being provided, which gets used as min if < default max of 100, max if > 100
    print(randInt(min=minMax[0]))
else:
    print(randInt())
