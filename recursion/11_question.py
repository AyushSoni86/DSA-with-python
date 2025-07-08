# josephus problem

def play(n, k):
    if n == 1: return 1
    return (play(n - 1, k) + k - 1) % n + 1
    

print(play(3, 2))