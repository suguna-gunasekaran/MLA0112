import heapq

h = {'A':7,'B':6,'C':5,'D':2,'G':0}
graph = {'A':[('B',1),('C',4)], 'B':[('D',2)], 'D':[('G',3)], 'C':[], 'G':[]}

pq = [(h['A'], 0, 'A')]
visited = set()

while pq:
    f, g, n = heapq.heappop(pq)
    if n in visited: continue
    print(n)
    visited.add(n)
    if n == 'G':
        print("Cost =", g)
        break
    for nxt,c in graph[n]:
        heapq.heappush(pq, (g+c+h[nxt], g+c, nxt))
