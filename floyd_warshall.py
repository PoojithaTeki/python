#Floyd-warshall alogrithm
nv=4
INF=9999
def floyd_warshall(G):
	dist=list(map(lambda i:list(map(lambda j:j,i)),G))
	for k in range(nv):
		for i in range(nv):
			for j in range(nv):
				dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
	print_sol(dist)
def print_sol(dist):
	for i in range(nv):
		for j in range(nv):
			if dist[i][j]==INF:
				print("INF",end=" ")
			else:
				print(dist[i][j],end=" ")
		print(" ")
G=[[0,3,INF,5],[2,0,INF,4],[INF,1,0,INF],[INF,INF,2,0]]
floyd_warshall(G)
