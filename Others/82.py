def WeightGraph():
    def findPath(start, end, cost=0):
        if start == end:
            # If the start and end are the same, print the cost
            print(str(cost) + ' ')
        else:
            # Check each edge in the weighted list
            for (s, e, w) in weightedList:
                if s == start:
                    # If the edge starts at the current start point,
                    # call findPath() recursively with the end point of the edge
                    # and the updated cost
                    findPath(e, end, cost + w)

    # Here I have defined the edges as a list of tuples
    # Each tuple contains the start and end points, and the weight of the edge
    weightedList = [('A', 'B', 10), ('A', 'C', 5),
                    ('B', 'D', 20), ('C', 'D', 15),]
    start_point = str(input('Enter Starting point: '))
    end_point = str(input('Enter Ending point: '))
    print('The length of findPath is: ')
    findPath(start_point, end_point)


WeightGraph()