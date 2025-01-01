
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