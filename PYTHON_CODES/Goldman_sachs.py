# This problem was asked by Goldman Sachs.
# Given a list of numbers _inputList, implement a method _sum(i, j) which returns the sum 
# from the sublist _inputList[i:j] (including i, excluding j).
# For example, given _inputList = [1, 2, 3, 4, 5], _sum(1, 3) should return _sum([2, 3]), which is 5.

# taking input from user
def _input():
    global _inputList # Declaring input variable as global variable to access it outside the function w/o passing as param

    #taking input
    _inputList = list(map(int, input("Enter list element(space separated): ").strip().split(" ")))
    
    #printing the input list
    print(_inputList)


# function to calculate the sum within the indexes of _inputlist
def _sum(i: int, j: int):
    global _inputList #using global variable
    sum = 0 #declaring sum variable to store the result

    for item in range(i,j):
        sum += _inputList[item]
    
    #returning the sum as result
    return sum



#driver code
if __name__ == "__main__":
    
    #Calling the _input() function for user input
    _input()

    #calling _sum() function
    res = _sum(1,3)

    #printing out the result of operation done in _sum()
    print("Output: ", res)