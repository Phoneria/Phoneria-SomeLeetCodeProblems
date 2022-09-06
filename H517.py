#Super Washing Machines
"""
It is enough to increase number which is smaller than average
"""

machines = [0,3,0]



def moves(machines):

    if sum(machines)%3 != 0:
        return -1

    average = sum(machines)/len(machines)

    step= 0

    for i in range(len(machines)):
        if machines[i] < average:
            diff = average-machines[i]
            machines[i] += diff
            step+= diff


    return int(step)

answer = moves(machines)


