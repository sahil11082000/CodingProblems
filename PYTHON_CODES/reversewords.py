'''
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples:
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''
def reverse_words(text):
  res = ""
  for i in text.split(" "):
        if i == '':
            res = res + " "
        else:
            res += i[::-1] + " "
  return res.strip()


def optimized_reverse_words(text):
    return ' '.join(s[::-1] for s in str.split(' '))

if __name__ == "__main__":
    in_string = input("Enter the string:")
    print(reverse_words(in_string))
    