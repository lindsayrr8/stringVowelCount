
# This program returns a count of all vowels in a string.


# Declare vowel counting function.
def countVowels(string):
    vowels = "aeiouAEIOU" # Specify values for vowels.
    count = 0

    for char in string: # Evaluate vowels in the given string.
        if char in vowels:
            count += 1

    return count

# Declare main function; prompts user to input a word for evaluation.
def main():
    userWord = input("Please enter a word. ")
    # Assign data from countVowels() function to vowelCount variable.
    vowelCount = countVowels(userWord)
    print(" ")
    print("The vowel count is: ", vowelCount) # Output

# Call main function.
main()
