


class InputReader:

        def __call__(self):
                pass
        def __init__(self):
                self.plik = open('dane.txt','r')
                self.lines= self.plik.readlines()
                self.matrix = []
                for wiersz in self.lines:
                        self.matrix.append(wiersz.split(' '))
                self.matrix[0][2] = self.matrix[0][2][:-1]

class InputValidator(InputReader):
        def __call__(self):
                pass
        def __init__(self,IR):
                self.flag=0
                self.flag3=0
                for wiersz in IR.matrix:
                        for kolumna in wiersz:
                                if not (kolumna.lstrip('-').replace(".", "", 1).isdigit()):
                                        self.flag = 1
                if (self.flag):
                        print ("Dane nie sa liczbami")
                else:
                        self.matrix2 = []
                        for i in xrange(len(IR.matrix)):
                                self.matrix2.append([])
                                for j in xrange(len(IR.matrix[i])):
                                        self.matrix2[i].append(0)
                        self.flag2=0                
                        for i in xrange(len(IR.matrix)):
                                for j in xrange(len(IR.matrix[i])):
                                        self.matrix2[i][j] = float(IR.matrix[i][j])
                                        if not(self.matrix2[i][j]==0):
                                                self.flag2=1
                        if(self.flag2):
                                if not(self.matrix2[0][0]*self.matrix2[1][1]-self.matrix2[0][1]*self.matrix2[1][0]==0):
                                        self.flag3=1
                                        print("uklad oznaczony")
                                
                                elif  ((self.matrix2[0][0]*self.matrix2[1][1]-self.matrix2[0][1]*self.matrix2[1][0]==0) and (self.matrix2[0][2]*self.matrix2[1][1]-self.matrix2[0][1]*self.matrix2[1][2]!=0) and (self.matrix2[0][0]*self.matrix2[1][2]-self.matrix2[0][2]*self.matrix2[1][0]!=0)):
                                        print("uklad sprzeczny")
                                else:
                                        print("uklad nieoznaczony")
                                        
                        else:
                                print("Wszystkie parametry sa zerami, uklad nieoznaczony")
                                        
                        

class Solver(InputValidator):
        def __call__(self):
                pass
        def __init__(self,IV):
                if (IV.flag3):
                        self.X=(IV.matrix2[0][2]*IV.matrix2[1][1]-IV.matrix2[0][1]*IV.matrix2[1][2])/(IV.matrix2[0][0]*IV.matrix2[1][1]-IV.matrix2[0][1]*IV.matrix2[1][0])
                        self.Y= (IV.matrix2[0][0]*IV.matrix2[1][2]-IV.matrix2[0][2]*IV.matrix2[1][0])/(IV.matrix2[0][0]*IV.matrix2[1][1]-IV.matrix2[0][1]*IV.matrix2[1][0])
                        print "Rozwiazanie ukladu X="+str(self.X)+" Y="+str(self.Y)
a = InputReader()       
b = InputValidator(a)
b()
c = Solver(b)
c()
