"""
    You are provided with a list of names. Write a program to  rearrange them so that persons with the same surname are adjacent. Each item in the list will contain first name, middle name(optional), and surname, separated by space, the last word will be the surname.

    Example:
    "input": ["Pratik Thapa", "Hari Kumar Karki", "Shyam Govind Sharma", "Wilson Karki", "Baladev Thapa"]
    "output": ["Pratik Thapa", "Baladev Thapa", "Hari kumar Karki", "Gopal Karki", "Shyam Govind Sharma"]

"""

import unittest

"""
    The given list
"""
list = ["Pratik Thapa", "Hari Kumar Karki", "Shyam Govind Sharma", "Wilson Karki", "Baladev Thapa"]

print("The given list is:\n",list)

"""
    Divide the string names into list names and sort the array
"""
def divide_sort(list):
    value_list = []
    def sort_key(name):
        return name[len(name)-1]
    for i in list:
        value = i.lower().split()
        value_list.append(value)

    value_list.sort(key=sort_key,reverse=True)   
    return value_list
"""
    Combine the array names into string after sorting
"""
def combine_name(value_list):
    return [' '.join(i).title() for i in value_list]

sorted_list = combine_name(divide_sort(list))
print("The output is:\n",sorted_list)

"""
    Testing
"""
class LearnTest(unittest.TestCase):
    def test_main_function(self):
        list = ["Pratik Thapa", "Hari Kumar Karki", "Shyam Govind Sharma", "Wilson Karki", "Baladev Thapa"]     
        self.assertEqual(combine_name(divide_sort(list)),['Pratik Thapa', 'Baladev Thapa', 'Shyam Govind Sharma', 'Hari Kumar Karki', 'Wilson Karki'])
if __name__ == "__main__":
    unittest.main()