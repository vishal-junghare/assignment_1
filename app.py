def min_platforms(arrivals, departures):
    """
    Calculate minimum number of platforms needed at a railway station.
    
    Args:
        arrivals: List of arrival times in HH:MM format
        departures: List of departure times in HH:MM format
        
    Returns:
        int: Minimum number of platforms required
    """
    # Convert times to minutes for easier comparison
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    # Convert all times to minutes
    arr_times = [time_to_minutes(t) for t in arrivals]
    dep_times = [time_to_minutes(t) for t in departures]
    
    # Sort both arrays
    arr_times.sort()
    dep_times.sort()
    
    platforms_needed = 1  # At least one platform is needed
    result = 1
    i = 1  # Start from second arrival
    j = 0  # Start from first departure
    
    # Similar to merge process of merge sort
    while i < len(arr_times) and j < len(dep_times):
        # If next arrival is before current departure
        if arr_times[i] <= dep_times[j]:
            platforms_needed += 1
            i += 1
        # If a train has departed, we can reduce the platform count
        elif arr_times[i] > dep_times[j]:
            platforms_needed -= 1
            j += 1
            
        result = max(result, platforms_needed)
    
    return result

# Test cases
test_cases = [
    {
        'arrivals': ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00'],
        'departures': ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']
    },
    {
        'arrivals': ['9:00', '9:40'],
        'departures': ['9:10', '12:00']
    }
]

# Run test cases
for i, test in enumerate(test_cases, 1):
    result = min_platforms(test['arrivals'], test['departures'])
    print(f"Test case {i}: {result} platforms needed")