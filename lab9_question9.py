"""n=int(input())
if(n%2==0):
    if(6<n<20):
        print("weird")
    else:
        print("Not weird")
else:
    print("Weird")
    
if __name__ == '__main__':
    n = int(input().strip())
    if ((n > 20) and (n % 2 == 0)) or n == 4:
        print('Not Weird')
    elif 1 < n < 100:
        print('Weird')"""
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**i)

