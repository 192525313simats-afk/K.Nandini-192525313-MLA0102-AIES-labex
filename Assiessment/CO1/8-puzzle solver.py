import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

print("Heuristic Value:", heuristic(start))
