def Only_shapes():
for _ in range(int(input())):
    n,r=map(int,input().split())
    if n>r:
        print((r*(r+1))//2)
    else:
        print(((n*(n-1))//2)+1)


if __name__ == "__main__":
    Only_shapes()
