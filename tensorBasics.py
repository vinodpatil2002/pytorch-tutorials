import torch


def empty_tensor():
    # create empty tensors
    x = torch.empty(3,3)
    print(x)

def random_tensors():
    # create tensors with random values:
    x = torch.rand(2,2)
    print(x)




def zero_tensor():
    # can create tensors with zeroes
    x = torch.zeros(2,2)



def ones_tensor():
    # can create tensors with ones
    x= torch.ones(2,2)

def try_dtype():
    # give specific data types;

    # print(x.dtype)  # default will be torch.float32

    y = torch.ones(2,2, dtype=torch.int)

    # simlarly double
    # y = torch.ones(2,2, dtype=torch.double)

    # float16
    # y = torch.ones(2,2, dtype=torch.float16)

    print(y.dtype)
    print(y.size())



def tensor_data():
    # create tensor from data 
    z = torch.tensor([[2.5,0.1,0.3],[1.5,7.5,1.6]])
    print(z)

# basic operations:


def add_tensors():
    a = torch.rand(2,2)
    b = torch.rand(2,2)
    # print(a,b)
    c = torch.add(a,b) #inbuilt function to add tensors
    # print(a + b);
    # modify b and add a 
    b.add_(a)
    print(c)


def subtract_tensors():
    a = torch.rand(2,2)
    b = torch.rand(2,2);
    print(a)
    print(b)
    print(a-b)
    # inbuilt: c = torch.sub(a,b)
    b.sub_(a)
    print(b)


def mutliply_tensors():
    a = torch.rand(2,2)
    b = torch.rand(2,2);
    print(a)
    print(b)
    print(a*b)
    print(torch.mul(a,b))
    b.mul_(a)
    print(b)

def main():
    mutliply_tensors()

if __name__ == "__main__":
    main()

