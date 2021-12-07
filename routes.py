import sys

class Routes:
 

    def __init__(self, routesTable={}):
        # the routesTable is our hash map DT
        self.routesTable = routesTable
    
    def dB(self, cities=[]):
      
        
        """
        We need to Calculates distance of the route
        The Arguments cities=[]: the array of cities
        which Return the calculated distance
       
        """

        distance = 0 
        '''
        For every town, we are able to have a look at the adjoining direction and 
        via way of means of including the burden of the direction to the full distance
        '''
        for i in range(len(cities)):
            root_node = cities[i]
            if i + 1 < len(cities):
                next_node = cities[i+1]
                if next_node in self.routesTable[root_node]:
                    distance = distance + self.routesTable[root_node][next_node]
                else: 
                    return "No Route found : !"
        return distance
    
    def ns(self, start, end, maxStops):
      
        """
        Wrapper function to calculate the number of stops
        The Arguments:
        
        Start : City Starting as- ->(String) 
        end: the Destination City as- ->(String)
        maxStops: maximum stops that are allowed->(int)
        It Return:the calclated No.of routes->(int)
        
        
        
        """
        return self.fR(start, end, 0, maxStops)
    
    def fR(self, start, end, depth, maxStops):
    
        """
        Recursive function to calculate the number of stops
       
        The Arguments:
         
        Start       : City Starting as                       ->(String) 
        end         : the Destination City as                ->(String)
        maxStops    : quantity of most stops allows          ->(int)
        depth       : The present day intensity of recursion ->(int)
        
        It Return:
                the calclated No.of routes                     ->(int)
        """

        visited =[]
        routes = 0
        # Check if start and end nodes exists in route table
        if start in self.routesTable and end in self.routesTable:
            depth +=  1
            if depth > maxStops:  
                return 0
            visited.append(start) 

            for adj in self.routesTable[start]:
                '''
               
                If vacation spot matches, we increment route
    count, then preserve to subsequent node at equal depth
				'''
                if adj == end:
                    routes+=1 
                    
                
                '''
                
                If vacation spot does now no longer match, and
    vacation spot node has now no longer but been visited,
    we recursively traverse vacation spot node
				'''
                if adj not in visited and adj != end:
                    depth -= 1
                    routes += self.fR(adj, end, depth, maxStops)
        else:
            return "No Such route"
        
        # unmark the start node before leaving recursive func
        if start in visited:
            visited.remove(start)
        return routes
    

    def sR(self, start, end):
       
        """
        Wrapper function to calculate the shortest route
        Arguments:
            start    :    Starting city             -->(String)
            end      :    Destination city          -->(String)

        It Returns:
             Which calculates the  weight of the shortest route ->(int)
        """
        return self.fSR(start, end, 0, 0)

    def fSR(self, start, end , weight, sR, visited=[]):
        
        """
      Recursive characteristic to calculate the shortest route
        Arguments:
            start           :      Starting city            ->(String)
            end             :      Destination city         ->(String)
            weight          :   weight of the route         ->(Weight)
            sR              :      shortest route so far    ->(int)
            visited         :    array of visited nodes     ->(String[])

        It Returns:
            int: calculated weight of the shortest route    ->(int)
        """

        # Check if start and end nodes exists in route table
        if start in self.routesTable and end in self.routesTable:
            visited.append(start) 

            for adj in self.routesTable[start]:
                if(adj == end or adj not in visited):
                    weight += self.routesTable[start][adj]
                    
                '''
                
                
                If vacation spot matches, we compare
                weight of this path to shortest path
                so far, and make a suitable switch
                '''

                if adj == end:
                    if sR == 0 or weight < sR:
                        sR = weight
                    visited.remove(start)
                    return sR
                '''
                If vacation spot does now no longer match, and
    vacation spot node has now no longer but been visited,
    we recursively traverse vacation spot node
                '''
                if adj not in visited:
                    sR = self.fSR(adj, end, weight, sR, visited)
                    weight -= self.routesTable[start][adj]
        
        else:
            return "No such route exists"

        if start in visited:
            visited.remove(start)
        
        return sR

    def numberOfRWithin(self, start, end, maxDistance):
       
        """
        Wrapper function to calculate the number of routes within a given limit
        Arguments:
            start           :      Starting city            ->(String)
            end             :      Destination city         ->(String)
            maxDistance     :      Maximum distance/limit   ->(int)

        It Returns:
             number of routes ->(int)
        """
        return self.findnumberOfRWithin(start, end, 0, maxDistance)
    
    def findnumberOfRWithin(self, start, end , weight, maxDistance, routes=0):
        """
        Recursive function to calculate the number of routes within a given limit
        Arguments:
            start           :      Starting city            ->(String)
            end             :      Destination city         ->(String)
            weight:         :      Weight of the route      ->(int)
            maxDistance     :      Maximum distance/limit   ->(int)
            routes:         :      Current routes in the recursion ->(int)

        It Returns:
             number of routes ->(int)
        """
        # check if start and end node exists in the graph
        if start in self.routesTable and end in self.routesTable:
            '''
            
   If begin node exists then traverse all possible
   routes and for each, test if it's far destination
            '''
            for adj in self.routesTable[start]:
                weight += self.routesTable[start][adj]
                '''
                
    If the distance is below max, maintain traversing
    even though the fit is discovered till the distance is > max
                '''
                if weight <= maxDistance:
                    if adj == end:
                        routes +=1
                        routes += self.findnumberOfRWithin(adj, end, weight, maxDistance)
                    else:
                        routes += self.findnumberOfRWithin(adj, end, weight, maxDistance)
                        weight -= self.routesTable[start][adj] 
                else:
                    weight -= self.routesTable[start][adj]
        else:
            print("No Route Found")
        
        return routes

    def fpwES(self, start, finish, exact):
        
        """
        Wrapper function to calculate the path with exact number of stops
        Arguments:
            start           :      Starting city            ->(String)
            end             :      Destination city         ->(String)
            maxDistance     :      exact number of stops    ->(int)

        It Returns:
             number of routes ->(int)
        """
        count = 0
        visited = []
        path = []

        path.append(start)
        visited.append(start)

        for adjacent_node in self.routesTable[start]:
            if adjacent_node not in visited:
                count = self.pAPUtil(adjacent_node, finish, visited, path, exact, count)
        
        return count

    
    # util methods for cycle detection
    def pAPUtil(self, start, finish, visited, path, exact, count):
    
        """
        Recursive function to calculate the number of routes within a given limit
        Arguments:
            start           :        Starting city          ->(String)
            end             :        Destination city       ->(String)
            visited         :      Maximum distance/limit   ->(String[])
            path            :      path so far              ->(String[])
            exact           :        limit                  ->(int)
            count           :        number of paths found so far ->(int)

        It Returns:
             count ->(int)
        """
        visited.append(start)
        path.append(start)

        if start == finish:
            if len(path) < exact:
                count = self.findCycle(finish, path, exact, count)
            
            if len(path) == exact + 1:
                
                count+=1
        else:
            for adjacent_node in self.routesTable[start]:
                if adjacent_node not in visited:
                    count = self.pAPUtil(adjacent_node, finish, visited, path, exact, count)
        
        path.pop()
        visited.remove(start)

        return count


    def findCycle(self, start, path, exact, count):
        """
        Wrapper function to detect cycle in the graph
        Arguments:
            start           :        Starting city          ->(String)
            end             :        Destination city       ->(String)
            path            :      path so far              ->(String[])
            exact           :        limit                   ->(int)
            count           :        number of paths found so far ->(int)

        It Returns:
           count ->(int) 
        """
        visited = []

        for adj_node in self.routesTable[start]:
            if adj_node not in visited:
                count = self.fCUtil(adj_node, start, path, visited, exact, count)
        return count
    

    def fCUtil(self, start, end, path, visited, exact, count):
       
        """
        recursive function to detect circular path in the graph
        Arguments:
            start           :        Starting city          ->->(String)
            end             :        Destination city       ->->(String)
            path            :        path so far ->
            visited         :        visited nodes so far   ->(String[]) 
            exact           :        limit                  ->(int)
            count           :        number of paths found so far ->(int)

        It Returns:
             count  ->(int)
        """
        visited.append(start)
        path.append(start)

        if start == end:
            if len(path) == exact + 1:
                count+=1
             
        else:
            for adj_node in self.routesTable[start]:
                if adj_node not in visited:
                   count = self.fCUtil(adj_node, end, path, visited, exact, count)

        path.pop()
        visited.remove(start) 

        return count
    
      #dB->distanceBetween
      #ns->numStops
      #fR->findRoutes
      #sR->shortestRoute
      #fSR->findShortestRoute
      #numberOfRWithin->numberOfRoutesWithin
      #fpwES->findPathWithExactStops
      #pAPUtil->printAllPathsUtil
      #fCUtil->findCycleUtil
    