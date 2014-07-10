class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        
points = [Point(1,2), Point(2,3), Point(3,4), Point(3,5)] 

size = len(points)
slop = {"inf":0}
for i in range(size):
    p1 = points[i]
    for j in range(i+1, size):
        p2 = points[j]
        if p2.x - p1.x != 0:
            if (p2.y - p1.y)/float(p2.x - p1.x) in slop:
                slop[(p2.y - p1.y)/float(p2.x - p1.x)] += 1
            else:
                slop[(p2.y - p1.y)/float(p2.x - p1.x)] = 1
        else:
            slop['inf'] += 1
            
print sorted(slop.values(), reverse = True)[0]