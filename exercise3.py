word = input("Enter any word: ")

def reverseString(s):
    newWord = s[::-1]
    if newWord == s:
        return "The word is a palindrome."    
    else:        
        return "The word is not a palindrome."




print(reverseString(word))