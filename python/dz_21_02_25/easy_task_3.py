def Judge(n, trust):
    if len(trust) == 0: return -1
    if len(trust) == 1: return trust[0][1]
    else:
        judge = trust[0][1]
        graph = {}
        for i in range(len(trust)):
            if(trust[i][1] != judge): return -1
            graph[trust[i][0]] = trust[i][1]
        if graph.get(judge) == None: 
            return judge
        else: return -1
        
n = 2
trust = [[1,2]]
print(Judge(n, trust))
n = 3
trust = [[1,3],[2,3]]
print(Judge(n, trust))
n = 3
trust = [[1,3], [2,3], [3,1]]
print(Judge(n, trust))

n = 6
trust = [[1,5],[2,5],[3,5],[4,5],[6,5]]
print(Judge(n, trust))