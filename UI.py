import Encryption

# get the user input and ensure it is formatted correctly
def getUserInput():
    try:
        path = input("Enter 'E' to encode and 'D' to decode\n").upper()
        if len(path) > 0:
            if path == 'E':
                userInput = input("Enter a string: ")
                if len(userInput) == 0:
                    print("Invalid string\n")
                    getUserInput()
                
            elif path == 'D':
                userInput = input("Enter a list of integers: ")   
                try:        
                    userInput = eval(userInput)
                except:
                    raise Exception('invadid list')
            else:
                raise Exception('must enter "E" or "D"')
        else:
            raise Exception('No input')
  
        return userInput
    except Exception as error:
        print("Input Error: " + str(error) + '\n')        
        return getUserInput()             

def main(): 
    while True:
        userInput = getUserInput()
        if isinstance(userInput, str):
            result = Encryption.encode(userInput)
        else:
            result = Encryption.decode(userInput)
        print(result)
        print()    

main()
