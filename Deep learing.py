import torch

lista = [[1,2,3],
        [4,5,6]]

tns = torch.FloatTensor(lista)
print(tns.dtype)
print(tns)

tns = torch.DoubleTensor(lista)
print(tns.dtype)
print(tns)


tns = torch.LongTensor(lista)
print(tns.dtype)
print(tns)


arr = np.random.rand(3,4)
tns = torch.from_numpy(arr)

print(arr)
print(arr.dtype)

print(tns)
print(tns.dtype)


tns1 = torch.ones(2,3)
tns0 = torch.zeros(4,5)
tnsr = torch.randn(3,3)

print(type(tnsr ))
arr = tnsr.data.numpy()
print(arr)

print(tnsr)
tns[0,2] = -10
print('')
print(tnsr)

print('')
print(tnsr[0,2])

print(tnsr[0,2])


tns= tnsr
print(tns)
print(tns1)

print(torch.mm(tns1,tns.T))


