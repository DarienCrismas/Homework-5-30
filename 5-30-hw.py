#Exercise 1
#Accept two user ages as inputs and give us the difference between them. (The Answer should always be a positive output)
def exercise_1():
    age1 = int(input("Please give me an age. "))
    age2 = int(input("Please give me a second age."))
    print("Calculating difference.")
    print (abs(age1 - age2))

exercise_1()
print()


#Exercise 2
#Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.
def exercise_2():
    noun = input("Please type a noun. ")
    verb = input("Now a verb. ")
    adjective = input("Finally, an adjective. ")
    print(f"The {adjective.lower()} {noun.lower()} screamed and {verb.lower()} up the tree.")


exercise_2()
print()


#Exercise 3 
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print senior 
def exercise_3():
    age = int(input("How old are you? Please enter a number, not text. "))
    if age < 18:
        print("Hey kiddo")
    elif age < 65:
        print("You are an adult")
    else:
        print("'Sup fossil")


exercise_3()
print()


#Exercise 4 
#Take in a number from a user input, output the number squared.
def exercise_4():
    number = int(input("Type a number. "))
    print (number**2)

exercise_4()
print()


#Exercise 5 
#Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False
def exercise_5():
    print (len(word1) > 5)
    print (len(word2) > 5)
    print (len(word3) > 5)
    print (len(word4) > 5)
    print (len(word5) > 5)


word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

exercise_5()

