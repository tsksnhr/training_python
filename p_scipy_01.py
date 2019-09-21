from scipy import sparse
import numpy  as np

a = sparse.lil_matrix((4, 5))
a[0, 1] = 1
a[0, 3] = 2
a[2, 2] = 3
a[3, 4] = 4
print(a.toarray())

b = sparse.lil_matrix((5, 4))
b[0, 2] = 1
b[1, 2] = 2
b[2, 3] = 3
b[3, 3] = 4
print(b.toarray())

#c1 = np.dot(a, b)
c2 = a.dot(b)

#print(c1)
#print(c1.toarray())

print(c2)
print(c2.toarray())

# csr form
ar = a.tocsr()
br = b.tocsr()
cr = ar.dot(br)
print(cr.toarray())

# csc form
ac = a.tocsc()
bc = b.tocsc()
cc = ac.dot(bc)
print(cc.toarray())
