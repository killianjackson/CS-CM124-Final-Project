import sys
from datetime import datetime

genotypes = []
undetermined = []
haplotypes = []
possibles = []

def initialHaplotypes():
    for gt in genotypes:
        undet = False
        tempList = []
        for a in gt:
            if a == '0':
                tempList.append('0')
            elif a == '1':
                tempList.append('x')
                undet = True
            elif a == '2':
                tempList.append('1')
        if undet:
            undetermined.append(tempList)
        else:
            exists = False
            for h in haplotypes:
                if h == tempList:
                    exists = True
            if not exists:
                haplotypes.append(tempList)


def generatePossibleHaplo(undet):
    buffer = [[]]
    for i in range(0,len(undet)):
        if undet[i] == '0' or undet[i] == '1':
            for p in buffer:
                p.append(undet[i])
        elif undet[i] == 'x':
            buffer2 = []
            for z in range(0,len(buffer)):
                buffer2.append([])
            for x in range(0,len(buffer)):
                for y in range(0,len(buffer[x])):
                    buffer2[x].append(buffer[x][y])
            for j in range(0,len(buffer)):
                buffer[j].append('0')
                buffer2[j].append('1')
            buffer = list(buffer + buffer2)
    return buffer


def haplotypePhaser():
    initialHaplotypes()
    for i in undetermined:
        buffer = generatePossibleHaplo(i)
        for k in buffer:
            for j in haplotypes:
                if k == j:
                    flip = []
                    for a,b in zip(i,k):
                        if a == '0' or a == '1':
                            flip.append(a)
                        elif a == 'x':
                            if b == '0':
                                flip.append('1')
                            elif b == '1':
                                flip.append('0')
                    exists = False
                    for z in haplotypes:
                        if z == flip:
                            exists = True
                    if not exists:
                        haplotypes.append(flip)

def generateOutputFile(haplos):
    outputFile = open('very_easy_training_output.txt', 'w+')
    for h in haplos:
        outputFile.write(''.join(h) + '\n')
    outputFile.close()

if __name__ == '__main__':
    startTime = datetime.now()
    if len(sys.argv) != 2:
        print('Error: this program requires three arguments')
        exit()
    f = open(sys.argv[1], 'r')
    for line in f:
        line = line.rstrip('\n')
        genotypes.append(line)
    f.close()
    haplotypePhaser()
    generateOutputFile(haplotypes)
    print "Run time: "
    print datetime.now() - startTime

