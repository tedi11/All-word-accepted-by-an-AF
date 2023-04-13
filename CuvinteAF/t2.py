sol = []
lista_pasi = []
def bkt(nod):
    global sol, lista_pasi, lm
    #print("!")
    if len(lista_pasi) > lm:
        return
    if destinations[nod] == 1:
        #print("!")
        #sol.append(lista_pasi)
        print(*lista_pasi)
        sol.append(lista_pasi)
    for i in range(n):
        #if i != nod:
        try:
            for element in m[nod][i]:
                #print(lista_pasi)
                lista_pasi.append(element)
                #print(lista_pasi)
                bkt(i)
                lista_pasi.pop(len(lista_pasi)-1)  
        except:
            pass   
    


f = open("automat.txt")
n = int(f.readline())
lm = int(f.readline())
destinations = [0 for x in range(n)]
m = [[-1 for x in range(n)] for k in range(n)]

for i in range(n):
    fin = int(f.readline())
    destinations[i] = fin
    v = int(f.readline())
    for j in range(v):
        line = f.readline()
        dest = int(line.split()[0])
        pas = (line.split()[1])
        try:
            m[i][dest].append(pas)
        except:
            m[i][dest] = [pas]

bkt(0)
#print(sol)       
#print(m)

