class UndergroundSystem(object):

    def __init__(self):
        
        self.travels = []
        self.destinations = {}        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.travels.append([id, stationName, t, "checkIn"])

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        checkedIn = False
        startTime = 0
        startStation = ""
        endStation = stationName
        endTime = t
        for travel in self.travels:
            if travel[0] == id:
                if travel[3] == "checkIn":
                    checkedIn = True
                    startTime = travel[2]
                    startStation = travel[1]
                
                elif travel[3] == "checkOut":
                    checkedIn = False
            
        if checkedIn:
            stationStr = startStation + "," + endStation
            try:
                if type(self.destinations[stationStr]) == list:
                    self.destinations[stationStr].append(endTime - startTime)
                else:    
                    self.destinations[stationStr] = [endTime - startTime]
            except:
                self.destinations[stationStr] = [endTime - startTime]

        self.travels.append([id, stationName, t, "checkOut"])
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        times = self.destinations[startStation + ","  + endStation]
        avgTime = sum(times)/float(len(times))
        
        print(round(avgTime,1))
        return round(avgTime, 1)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)