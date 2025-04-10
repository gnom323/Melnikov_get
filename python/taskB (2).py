n, m = map(int, input().split())

clients = list(map(int, input().split()))

kassy = [0]*m

for i in range(len(clients)):
    malo = min(kassy)
    for j in range(len(kassy)):
        if(kassy[j] == malo): 
            kassy[j] += clients[i]
            #print(f'client {i} v kasse {j}')
            #print(kassy)
            break
print(max(kassy))