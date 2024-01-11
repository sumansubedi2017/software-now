def Check_seprate_convert(s):
    #Divide substrings into letter and number categories.
    number = ''.join(c for c in s if c.isdigit())
    letter= ''.join(c for c in s if c.isalpha())

    #Generating ASCII code decimal values of Even numebr
    even_numberstoascii = [str(ord(c)) for c in number if int(c) % 2 == 0]

    #Generating ASCII code decimal values of upper-case letters
    upper_caseletterstoascii = [str(ord(c)) for c in letter if c.isupper()]

    return ','.join(even_numberstoascii), ','.join(upper_caseletterstoascii)

#Get input from the user
user_input = input("Enter a string with numbers and letters at least length 16: ")

#Checking length of the string 
if len(user_input) < 16:
    print("Please enter a string with at least length 16.")
else:
    #Call the function with the user input
    number_result, letter_result = Check_seprate_convert(user_input)

    #Dispaly thesubstrings
    print("Number Substring:", number_result)
    print("Letter Substring:", letter_result)

#GitHub repository https://github.com/sumansubedi2017/software-now.git
