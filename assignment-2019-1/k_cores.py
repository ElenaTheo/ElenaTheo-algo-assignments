import sys
import pprint

input_filename = sys.argv[1]

g = {}

with open(input_filename) as graph_input:
    for line in graph_input:
        # Split line and convert line parts to integers.
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        # If a node is not already in the graph
        # we must create a new empty list.
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        # We need to append the "to" node
        # to the existing list for the "from" node.
        g[nodes[0]].append(nodes[1])
        # And also the other way round.
        g[nodes[1]].append(nodes[0])

d = []
p = []
core = []
pn = []
opn = []
npn = []
a = []


for i in g.keys():
    d.insert(i,len(g[i]))
    p.insert(i,len(g[i]))
    core.insert(i,0)

for i in g.keys():
    pn.insert(i,[p[i], i])
    #insert sthn pq


def create_pq():
    return []

def add_last(pq, c):
    pq.append(c)

def root(pq):
    return 0

def set_root(pq, c):
    if len(pq) != 0:
        pq[0] = c

def get_data(pq, p):
    return pq[p]

def children(pq, p):
    if 2*p + 2 < len(pq):
        return [2*p + 1, 2*p + 2]
    else:
        return [2*p + 1]

def parent(p):
    return (p - 1) // 2

def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]

def insert_in_pq(pq, c):
    add_last(pq, c)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i) < get_data(pq, parent(i)):
        p = parent(i)
        exchange(pq, i, p)
        i = p


pq = create_pq()
for i in range(len(pn)):
    insert_in_pq(pq,pn[i])

def extract_last_from_pq(pq):
    return pq.pop()

def has_children(pq, p):
    return 2*p + 1 < len(pq)

def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        # Use the data stored at each child as the comparison key
        # for finding the minimum.
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c
        exchange(pq, i, j)
        i = j
    return c
#βγαζω τον συγκεκριμενο γειτονα απο τη Pq
def extract_specific_from_pq(pq,opn,neighbour):
    index = -1
    for i in range(len(opn)):
        if opn[i] == neighbour:
            index = i

    return pq.pop(index)

#με παρομοιο τροπο με την extract_min_from_pq βαζω το συγκεκριμενο γειτονα που εβγαλα
#με την extract extract_specific_from_pq και φτιαχνω απο την αρχη την ουρα προτεραιοτητας
#ετσι καθε γονιος να εχει μικροτερη τιμη απο το παιδι

def remove_from_PQ(pq,opn,i):
    c = pq[root(pq)]
    set_root(pq, extract_specific_from_pq(pq,opn,1))
    i = root(pq)
    while has_children(pq, i):
        # Use the data stored at each child as the comparison key
        # for finding the minimum.
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c
        exchange(pq, i, j)
        i = j
    return c


while len(pq)>0:
    t = extract_min_from_pq(pq)
    core[t[1]] = t[0]
    if len(pq) != 0:
        neighbours = g[t[1]]
        for i in neighbours:
            d[i] = d[i]-1
            opn.insert(i,[p[i], i])
            change = max(t[0],d[i])
            p.insert(i,change)
            npn.insert(i,[p[i], i])
            remove_from_PQ(pq,opn,i)

#ο κωδικας δε βγαζει το αποτελεσμα που πρεπει, στο τελος η διαδικασια του updatepq 
#που επρεπε να κανω συμφωνα με τον αλγοριθμο μου εβγαζε λαθη που δεν ειχα χρονο να διορθωσω.
#προσπαθησα μεχρι ενα σημειο να συνεχισω
print(core)
