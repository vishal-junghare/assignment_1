from datetime import date
from typing import List

# Given a sorted array of positive and negative numbers. You have to Square it and sort it. Constraint : Time complexity O(n) 
# Example: 
# Input: [-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
# Output : [4, 16, 25, 25, 49, 56, 121, 144, 225] 



def sorted_squares(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    position = n - 1

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[position] = arr[left] * arr[left]
            left += 1
        else:
            result[position] = arr[right] * arr[right]
            right -= 1
        position -= 1

    return result

# Example usage
input_array = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
output_array = sorted_squares(input_array)
print(output_array)

class Address:
    def __init__(self, street: str, city: str, zip_code: str):
        self.street = street
        self.city = city
        self.zip_code = zip_code


# Design an immutable class with following attributes 
# String name; 
# String Id, 
# Date dateOfJoining 
# List<Address> addresses; 

class ImmutableEmployee:
    def __init__(self, name: str, emp_id: str, date_of_joining: date, addresses: List[Address]):
        self._name = name
        self._id = emp_id
        self._date_of_joining = date_of_joining
        self._addresses = addresses

    @property
    def name(self):
        return self._name

    @property
    def emp_id(self):
        return self._id

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @property
    def addresses(self):
        return self._addresses.copy()
        

# Given an array of Red Green Blue balls.You have to sort it. 
# Constraint : Time complexity O(n) 
# Constraint : Space complexity O(1) 
# Example: 
# Input: [R, G, B, G, G, R, B, B, G] 
# Output : [B,B,B,G,G,G,G,R, R] 

def sort_rgb(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:  # arr[mid] == 'B'
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage
input_balls = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
output_balls = sort_rgb(input_balls)
print(output_balls[::-1])

# Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}, dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
# Output: 3 
# Explanation: There are at-most three trains at a time (time between 9:40 to 12:00) 
# Input: arr[] = {9:00, 9:40}, dep[] = {9:10, 12:00} 
# Output: 1 


def find_minimum_platforms(arr, dep):
    arr.sort()
    dep.sort()
    n = len(arr)
    
    platform_needed = 1
    result = 1
    i = 1
    j = 0
    
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platform_needed += 1
            i += 1
        elif arr[i] > dep[j]:
            platform_needed -= 1
            j += 1
        
        if platform_needed > result:
            result = platform_needed
    
    return result

# Example usage
arrival_times = [900, 940, 950, 1100, 1500, 1800]
departure_times = [910, 1200, 1120, 1130, 1900, 2000]
print(find_minimum_platforms(arrival_times, departure_times))

arrival_times = [900, 940]
departure_times = [910, 1200]
print(find_minimum_platforms(arrival_times, departure_times))