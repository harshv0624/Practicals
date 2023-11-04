INF=9999999
N=5
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 1, 6, 1, 0]]


selected_node=[0,0,0,0,0]
no_of_edges=0
selected_node[0]=True

while(no_of_edges<N-1):
    min=INF
    a=0
    b=0
    for m in range(N):
        if selected_node[m]:
            for i in range(N):
                if ((not selected_node[i]) and G[m][i]):
                    if min>G[m][i]:
                        min=G[m][i]
                        a=m
                        b=i
    print(str(a) + " - " + str(b) + "  :" + "  " + str(G[a][b]))
    selected_node[b]=True
    no_of_edges+=1
