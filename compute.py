import sys

def display_output(threshold,actualLimit,userInput):
    remainingLimit=actualLimit
    if actualLimit==0.0 or sum(userInput)==0.0 or max(userInput)<=threshold:
        for item in userInput:
            print(0.0)
        print(0.0)
    else:
        for item in userInput:
            if item == 0.0 or item <= threshold or remainingLimit==0.0:
                print(0.0)
            elif remainingLimit>(item-threshold):
                print(item-threshold)
                remainingLimit = remainingLimit-(item-threshold)
            else:
                print(remainingLimit)
                remainingLimit=0.0
        print(actualLimit-remainingLimit)


try:
    #taking command line inputs
    threshold=float(sys.argv[1])
    actualLimit=float(sys.argv[2])
    remainingLimit=actualLimit
except ValueError:
     #checking for type error
    print(f"Invalid input of arguments")
    exit(1)
userInput = []
for line in sys.stdin:
    try:
        #checking if the usser input has reached the max count
        if(len(userInput)>99):
            print(f'maximum number of inputs reached')
            break
        value = float(line.strip())
        #checking if the number is within range
        if 0.0 <= value <= 1000000000.0:
                userInput.append(value)
        else:
             print(f"Value {value} out of range. Skipping.")
    except ValueError:
        #checking for type error
        print(f"Invalid input '{line.strip()}'. Skipping.")
    
display_output(threshold,actualLimit,userInput)
