def main(): # Main procedure starts here
    print('Please enter 3 different numbers below... ') 
    First = int(input('First number: '))
    Second = int(input('Second number: ')) # User sets variables here
    Third = int(input('Third number:  '))
    Mean = (First+Second+Third)/3 # Uses user input to calculate mean
                                  # before the main series of statements
                                  # begins.
############################################################           
    if (First==Second)or(First==Third)or(Second==Third):
        print('Please enter 3 different numbers: ')
    else:
        if (First>Second) and (First>Third): # Compound statement
            Largest=First                    # checks for largest,
            if (Second>Third):               # middle, and smallest.
                Middle= Second  
                Smallest= Third 
            else:                            # If the conditions are
                Middle= Third                # not the above, run this: 
                Smallest= Second 
        elif (Second>First) and (Second>Third):
            Largest=Second 
            if (First>Third):                # Checks third number against
                Middle=First                 # first number.
                Smallest=Third 
            else:                            # Second else checks for
                Middle= Third                # conformations that certain 
                Smallest= First              # variables are not third and
        elif (Third>Second) and (Third>First): # first. 
            Largest=Third 
            if (First>Second):              # Second if compound statement is checked
                Middle = First              # again, instead however is checked under
                Smallest= Second            # a single if statement in this instance.
            else:
                Middle= Second 
                Smallest= First
        else: 
            print('Error')
###########################################################
    print ('Mean average is: ' + str(Mean))
    print ('Ascending order... ' + str(Smallest) + ', ' + str(Middle) + ', ' + str(Largest)) # These lines print the new smallest
    print ('Descending order... ' + str(Largest) + ', ' + str(Middle) + ', ' + str(Smallest))# middle and largest variables that
                                                                                             # have just been set.

    playAgain = input ("Do you want to sort more numbers? Y/N ").lower() # Makes input lwrcase
    
    if playAgain not in {"y","n"}:                # If input is not y or n, then print error.
        print("Please enter a valid option: ")
    
    elif playAgain == "y": # Else if the input is "y", set invalid_input to true and run main()
        invalid_input  = True 
        main()
        
    elif playAgain == "n": # Else if the input is "n", set invalid_input to true and run main()
        invalid_input = False 
        print ("Exiting program...")
        exit()
main()


