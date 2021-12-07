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


def tDB_ABC():
	assert r.dB(['A','B','C']) == 9
	
def tDB_AD():
	assert r.dB(['A','D']) == 5
	
def tDB_ADC():
	assert r.dB(['A','D','C']) == 13
	
def tDB_AEBCD():
	assert r.dB(['A','E','B', 'C', 'D']) == 22
	
def tDB_AED():
	assert r.dB(['A','E','D']) == 'No Route Found'

def tNS_CC3():
    assert r.ns('C', 'C', 3) == 3

def tNS_AC4():
    assert r.fpwES('A', 'C', 4) == 3
	
def tSR_AC():
    assert r.sR('A', 'C' ) == 9

def tSR_BB():
    assert r.sR('B', 'B' ) == 9

def tNRWithin_CC():
    assert r.numberOfRWithin('C', 'C', 30) == 7
    
    
     #dB->distanceBetween
      #ns->numStops
      #fR->findRoutes
      #sR->shortestRoute
      #fSR->findShortestRoute
      #numberOfRWithin->numberOfRoutesWithin
      #fpwES->findPathWithExactStops
      #pAPUtil->printAllPathsUtil
      #fCUtil->findCycleUtil