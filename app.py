from sys import getrecursionlimit, setrecursionlimit
from routes import Routes

# Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
graph = {
          'A': {'B': 5, 'D': 5, 'E': 7 },
          'B': {'C': 4},
          'C': {'D': 8, 'E': 2},
          'D': {'C': 8, 'E':  6},
          'E': {'B': 3}
        }

r = Routes(graph)
i=1
print("OUTPUT #"+str(i),":",r.dB(['A','B','C'],))
i+=1
print("OUTPUT #"+str(i),":",r.dB(['A','D']))
i+=1
print("OUTPUT #"+str(i),":",r.dB(['A','D','C']))
i+=1
print("OUTPUT #"+str(i),":",r.dB(['A','E','B', 'C', 'D']))
i+=1
print("OUTPUT #"+str(i),":",r.dB(['A','E','D']))
i+=1
print("OUTPUT #"+str(i),":",r.ns('C', 'C', 3))
i+=1
print("OUTPUT #"+str(i),":",r.fpwES('A', 'C', 4))
i+=1
print("OUTPUT #"+str(i),":",r.sR('A', 'C' ))
i+=1
print("OUTPUT #"+str(i),":",r.sR('B', 'B' ))
i+=1
print("OUTPUT #"+str(i),":",r.numberOfRWithin('C', 'C', 30))
i+=1



