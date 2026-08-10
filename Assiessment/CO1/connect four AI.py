import math

def minimax(depth, isMax):
    if depth == 0:
        return 0

    if isMax:
        best = -math.inf
        for i in range(2):
            value = minimax(depth - 1, False)
            best = max(best, value)
        return best
    else:
        best = math.inf
        for i in range(2):
            value = minimax(depth - 1, True)
            best = min(best, value)
        return best

print("Minimax Value =", minimax(3, True))
