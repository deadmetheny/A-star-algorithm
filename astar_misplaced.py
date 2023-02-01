def formato(matrix):
    for i in range(16):
        if i%4==0 and i>0:
            print("")
        print(str(matrix[i])+" ", end = "")

def read_file(Datos):
    lines = []
    with open(Datos, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines
print(read_file('datos.txt'))

def contar(x):
    n = 0
    meta = [1, 2, 3, 4,
          5, 6, 7, 8,
          9, 10, 11, 12,
          13, 14, 15, 0]
    for i in range(16):
        if x[i] != 0 and x[i] != meta[i]:
            n += 1
    return n

def move(ar, p, st):
    rh = 9999
    store_st = st.copy()
    
    for i in range(len(ar)):
        
        dupl_st = st.copy()
        
        tmp = dupl_st[p]
        dupl_st[p] = dupl_st[arr[i]]
        dupl_st[arr[i]] = tmp
        
        trh = contar(dupl_st)
        
        if trh<rh:
            rh = trh
            store_st = dupl_st.copy()
    
    #print(rh, store_st)
    
    return store_st, rh
 

estado = [1, 2, 4, 5,
          3, 6, 7, 8,
          9, 10, 11, 12,
          13, 14, 15, 0]

h = contar(estado)

Nivel = 1

print("\n------ Nivel "+str(Nivel)+" ------")
formato(estado)
print("\nFichas mal colocadas: "+str(h))


while h>0:
    pos = int(estado.index(0))
    
    Nivel += 1
    
    if pos==0:
        arr = [1, 4]
        estado, h = move(arr, pos, estado)
    elif pos==1:
        arr = [0, 2, 5]
        estado, h = move(arr, pos, estado)
    elif pos==2:
        arr = [1, 3, 6]
        estado, h = move(arr, pos, estado)
    elif pos==3:
        arr = [2, 7]
        estado, h = move(arr, pos, estado)
    elif pos==4:
        arr = [0, 5, 8]
        estado, h = move(arr, pos, estado)
    elif pos==5:
        arr = [1, 4, 6, 9]
        estado, h = move(arr, pos, estado)
    elif pos==6:
        arr = [2, 5, 7, 10]
        estado, h = move(arr, pos, estado)
    elif pos==7:
        arr = [3, 6, 11]
        estado, h = move(arr, pos, estado)
    elif pos==8:
        arr = [4, 9, 12]
        estado, h = move(arr, pos, estado)
    elif pos==9:
        arr = [5, 8, 10, 13]
        estado, h = move(arr, pos, estado)
    elif pos==10:
        arr = [6, 9, 11, 14]
        estado, h = move(arr, pos, estado)
    elif pos==11:
        arr = [7, 10, 15]
        estado, h = move(arr, pos, estado)
    elif pos==12:
        arr = [8, 13]
        estado, h = move(arr, pos, estado)
    elif pos==13:
        arr = [9, 12, 14]
        estado, h = move(arr, pos, estado)
    elif pos==14:
        arr = [10, 13, 15]
        estado, h = move(arr, pos, estado)
    elif pos==15:
        arr = [11, 14]
        estado, h = move(arr, pos, estado)
    print("\n------ Nivel "+str(Nivel)+" ------")
    formato(estado)
    print("\nFichas mal colocadas: "+str(h))

