def conflict(state, nextX):
    """
    Given the positions of the queens(in the form of a state of tuple)
    and determines if position for the next queen generate any conflicts
    """
    nextY = len(state)
    
    for i in range(nextY):
        """
        It is true if the horizontal distance between the next queen and
        the previous one under consideration is either zero(same column)
        or equal to the vitical distance(on a diagonal)
        """
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
            
    return False

def quee(num=8, state=()):
    print("in queue")
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def pretty_print(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
        
    for pos in solution:
        print(line(pos))

quee({(2, 4), (7, 1), (3, 7), (1, 1), (6, 8), (0, 6), (4, 5), (5, 3)})