from collections import defaultdict, Counter
import random
import time


document = """Now is the time for all good men to come to the aid of their country and
the quick red fox jumped over the lazy brown cow
"""

wordc = defaultdict(int)
for word in document:
    wordc[word] += 1
c = Counter(wordc)

print(c)
s = sorted(c.items(), key=lambda (w, cnt): cnt, reverse=True)
print(s)
letters, counts = zip(*s)
print(letters)
print(len(counts))


def f(n):
    trials = [random.choice([0, 1]) for _ in range(n)]
    return sum(trials) / float(n), trials

start = time.time()
# flips = 1000000000
# 16 minutes 943791 flips/sec
# [(33, 1), (32, 1), (31, 1), (30, 2), (29, 3), (28, 3), (27, 3), (26, 2), (25, 14), (24, 27), (23, 69),
#  (22, 107), (21, 220), (20, 474), (19, 925), (18, 1947), (17, 3990), (16, 7639), (15, 15194), (14, 30519),
#  (13, 61166), (12, 122044), (11, 243548), (10, 489346), (9, 976700), (8, 1952872), (7, 3906282),
#  (6, 7811525), (5, 15624609), (4, 31248164), (3, 62499355)]
flips = 10
p, t = f(flips)
print("Probability of heads: {}".format(p))
seconds = time.time() - start
print("Seconds: {:.2f}, Flips per second: {:.0f}".format(seconds, flips/seconds))
headsInARow = 0
currentRun = 0
runs = []
for i in t:
    if i == 1:
        currentRun += 1
    else:
        if currentRun > 2:
            runs.append(currentRun)
            headsInARow = max(headsInARow, currentRun)
            currentRun = 0
headsInARow = max(headsInARow, currentRun)
print("Longest run of heads: {}".format(headsInARow))
print(sorted(Counter(runs).items(), key=lambda(l, lrc): l, reverse=True))

