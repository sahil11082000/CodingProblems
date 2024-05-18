def stringValidator(s: str):
    """
    This function will print out boolean values if the input string contains:
    alphanumeric characters, 
    alphabetical characters, 
    digits, 
    lowercase and 
    uppercase characters.

    INPUT: s : string type
    OUTPUT: for each of the validation condition : True/False
    """
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))


if __name__ == '__main__':
    s = input("Enter a string: ")
    
    # Calling function to validate string
    stringValidator(s)