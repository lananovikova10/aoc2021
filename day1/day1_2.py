#Your goal now is to count the
#number of times the sum of measurements in this sliding window increases from the previous sum.
# So, compare A with B, then compare B with C, then C with
# D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.
with open('input_2.txt') as f:
        lines = f.readlines()
        data = []
        for item in lines:
            data.append(int(item))
f.close()

step = 3
summs_of_three = []
summs_of_three = [sum(data[0:step])]
print(summs_of_three)

counter = []
for element in range(1, len(data)):
    summs_of_three.append(sum(data[element:element + step]))
    if summs_of_three[-1] > summs_of_three[-2]:
        counter.append(1)
print(sum(counter))