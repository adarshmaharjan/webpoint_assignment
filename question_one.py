"""
    Write a program which takes array of integers, keep a total score based on the following:
        Add 1 point for every even number in the array
        Add 3 points for every odd number in the array, expect for the number "5"
        Add 5 points every time the number "5" appears in the array
        Note that 0 is considered even.

    Example:
    Input [1,2,3,4,5]
    Output: 13

    Input: [17, 19, 21]
    Output: 9
"""

import array 
import unittest
"""
    Takes input
"""
def take_input():
    integerArr = array.array('i',[])
    
    n = int(input("Enter no of numbers you want in a array:"))
    for _ in range(n):
        try:
            integerArr.append(int(input('Enter a an integer:')))
        except:
            raise Exception("Please input integer only")
    print("Given Array:",integerArr)
    return integerArr
"""
    Execution of main function
"""
def main_function(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum+=1
        if i % 2 != 0 and i != 5:
            sum+=3
        if i==5:
            sum+=5
    return sum


res = main_function(take_input())
print("The output of this program is:",res) 

"""
    Testing
"""
class LearnTest(unittest.TestCase):
    def test_main_function(self):
       self.assertEqual(main_function([1,2,3,4,5]),13)
if __name__ == "__main__":
    unittest.main()




