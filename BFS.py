import numpy

def BFS(a, b, c, d, size):
    var = 0
    ima = True
    que_search = False

    brojac_koraka = 1

    while ima:
        for i in range(int(size)):
            if(a[var][i] != -1 and i != var):
                size_q = numpy.size(b)

                for j in range(size_q):
                    if(a[var][i] == b[j]):
                        que_search = True
                
                if(que_search == False and d[i] != 1):
                    b = numpy.append(b, numpy.array([a[var][i]]))
                
                que_search = False

        #print("Korak " + str(brojac_koraka) + ":")
        #print("Red: " + str(b))

        c = numpy.append(c, numpy.array([var]))
        d[var] = 1
        if(numpy.size(b) > 0):
            var = b[0]  
        if(numpy.size(b) < 1):
            ima = False
        if(numpy.size(b) > 0):
            b = numpy.delete(b, 0)

        #print("Odgovor: " + str(c))
        #print("\n\n")
        brojac_koraka += 1

    return c