class Node:
    def __init__(self,k):
        self.value = k
        self.next = None

class Graphnode:
    def __init__(self,k):
        self.value= k
        self.next = None
        self.color = 'ZZZZZ'
        self.previous_numbers = []

class Adjascency_list:
    def __init__(self,n):
        self.adjlst = [None] * n
        for i in range(n):
            self.adjlst[i] = Graphnode(i)

    def insert(self,a,b):
        temp = self.adjlst[a]
        while temp.next != None:
            temp = temp.next
        temp.next = Node(b)

def color_the_graph(G,Vertex_array,colours,temp_array):
    final_output = []
    i = 0
    flag = 0
    while (i < len(temp_array)):
        if flag == 1:
            j = colour_till_now + 1
        else:
            j = 0
        temp = G.adjlst[temp_array[i]]
        while temp.next != None:
            if((G.adjlst[temp.next.value].color == colours[j])): 
                j+=1
                temp = G.adjlst[temp_array[i]]
            else:
                temp = temp.next
        if j<9:
            G.adjlst[temp_array[i]].color = colours[j]
            flag = 0
        else:
            i -= 2
            flag = 1
            colour_till_now = colours.index(G.adjlst[temp_array[i+1]].color)
            G.adjlst[temp_array[i+1]].color = 'ZZZZZ'
           # print("COLOR", colour_till_now)
        i += 1
    '''for i in range(len(Vertex_array)):
        print("Vertex : ", i, end = ' ' )
        print(",", G.adjlst[i].color)
    '''
    for i in range(len(Vertex_array)):
        z = colours.index(G.adjlst[i].color)
        final_output.append(z+1)


    print("\nANS OF THE GIVEN SUDOKU IS : ")
    for i in range(len(Vertex_array)):
        if i%9 != 8:
            print(final_output[i], " ", end = ' ')
        else:
            print(final_output[i])

def Display_Question(G,Vertex_array,colours,Entries_Given):
    final_output = []

    for i in range(len(Vertex_array)):
        if(G.adjlst[i].color == 'ZZZZZ'):
            final_output.append('-')
        else:
            z = colours.index(G.adjlst[i].color)
            final_output.append(z+1)


    print("\nGIVEN SUDOKU IS : ")
    for i in range(len(Vertex_array)):
        if i%9 != 8:
            print(final_output[i], " ", end = ' ')
        else:
            print(final_output[i])


def main():
    v = 81
    #e = 56
    colours = ['red','blue','green','pink','orange','purple','yellow','majenta','grey','neon','violet','a','b','c','d','e','f','g','h','i']
    Vertex_array = []
    temp_array = []
    for i in range(v):
        Vertex_array.append(i)
        temp_array.append(i)

    G = Adjascency_list(v)
    with open('8_input.txt') as f:
        for line in f:
            s=line.strip()
            x,y = s.split()
            x,y = int(x),int(y)
            G.insert(x,y)
            G.insert(y,x)

    entry_number = int(input("How many entries are given in the table : "))
    print("Enter row number , column number and value at that index ")
    Entries_Given = []
    for i in range(entry_number):
        a,b,c = input().split()
        a,b,c = int(a),int(b),int(c)
        vertexnumber = (a-1)*9 + (b - 1)
        Entries_Given.append(vertexnumber)
        G.adjlst[vertexnumber].color = colours[c-1]


    for i in range(entry_number):
        t = temp_array.index(Entries_Given[i])
        temp_array.pop(t)

    #print(temp_array)
    Display_Question(G,Vertex_array,colours,Entries_Given)

    color_the_graph(G,Vertex_array,colours,temp_array)

if __name__ == '__main__':
    main()



