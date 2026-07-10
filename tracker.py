swim_times = [28.5, 27.9, 29.1, 27.4]
def average_time(times):
    return sum(times) / len(times)

print(average_time(swim_times))
rank_points = [1200, 1350, 1290, 1400]
print(average_time(rank_points))
def fastest_time(times):
    return min(times)


def slowest_time(times):
    return max(times)

def count_time(times):
    return len(times)
def difference(times):
    return max(times) - min(times)
print(fastest_time(swim_times))
print(slowest_time(swim_times))
print("The amount of times you recorded your races was")
print (count_time(swim_times))
print(difference(swim_times))
swim_log = {"Mon": 28.5, "Wed": 27.9, "Fri": 27.4, "Sat":26.8}
print(swim_log)
best_day = min(swim_log, key=swim_log.get)
print(best_day)