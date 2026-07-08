swim_times = [28.5, 27.9, 29.1, 27.4]
def average_time(times):
    return sum(times) / len(times)

print(average_time(swim_times))
rank_points = [1200, 1350, 1290, 1400]
print(average_time(rank_points))
def fastest_time(times):
    return min(times)

print(fastest_time(swim_times))
def slowest_time(times):
    return max(times)
print(slowest_time(swim_times))
def count_time(times):
    return len(times)
print("The amount of times you recorded your races was")
print (count_time(swim_times))