from scipy import sparse

a = sparse.lil_matrix((4, 4))
a[0, 1] = 1
a[1, 2] = 2
a[2, 3] = 3
a[3, 3] = 4

ar = a.tocsr()
ac = a.tocsc()

print(type(ar))
print(type(ar))

br = ar.getrow(1)
print(br.toarray())

bc = ac.getcol(3)
print(bc.toarray())

print(type(ar.T))
print(type(ac.T))
