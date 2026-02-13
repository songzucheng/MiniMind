import torch 

# v1 = torch.tensor([1, 2, 3])
# v2 = torch.tensor([4, 5, 6])
# result = torch.outer(v1, v2)
# print(result)

# t1 = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[13, 14, 15], [16, 17, 18]]])
# t2 = torch.tensor([[[7, 8, 9], [10, 11, 12]], [[19, 20, 21], [22, 23, 24]]])
# result = torch.cat((t1, t2), dim=2)
# print(result)

x = torch.tensor([1, 2, 3])
x2 = x.unsqueeze(1)
print(x2.shape)