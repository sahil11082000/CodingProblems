'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description


Complete the swap_case function in the editor below.

swap_case has the following parameters:z
    string s: the string to modify

Returns
    string: the modified string
'''
def swap_case(s):
    result = ''
    for i in s:
        if i.isalpha():
            if i.isupper():
                result += i.lower()
            else:
                result += i.upper()
        else:
            result += i
    
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)