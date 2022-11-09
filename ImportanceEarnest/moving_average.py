days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
values = [10,12,9,11,14,20,12,14,16,21,17,24,21,18,16]
moving_average_values = []
n = 3
for i in range(len(values)):
    moving_average = None
    if(i >= n-1):
        moving_average = 0
        selector = i - n
        while(selector < i):
            selector += 1
            moving_average += values[selector]/n

    moving_average_values.append(moving_average)

print("stop")