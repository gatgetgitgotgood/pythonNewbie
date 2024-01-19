# a=['1','2','3']
# b=list(map(int,a))
# print(b)
# a,b,c=map(int,input('공백으로 구분해서 값을 3개 넣어라').split())
# print('a=',a)
# print('b=',b)
# print('c=',c)

# def abc(n):
#     return n*3

# a=[1,2,3]
# b=list(map(abc,a))
# print(b)

# a=[1,2,3]
# b=[i*3 for i in a]
# print(b)

# def abc(n):
#     return n*3

# a=[1,2,3]
# print(list(map(abc,a)))

# a=[1,2,3]
# print(list(map(lambda x:x*3,a)))

# def chk_str(n):
#     return type(n)==int

# a=[1,2,3,'a','b',3,'abc']
# b=list(filter(lambda x: type(x)==int,a))
# print(b)

# a=[4,3,2,1]
# b=sorted(a,reverse=True)
# print(b)

# a=[('김',30,70),
#    ('이',50,10),
#    ('박',10,30)]

# # b=sorted(a,key=lambda x:x[1],reverse=True)
# b=sorted(a,key=lambda x:x[-1])
# print(b)

# a={
#     '영어':30,
#     '국어':10,
#     '일어':50
#     }
# print(a.items())
# b=dict(sorted(a.items, key=lambda x:x[1]))
# print(b) > 문제있는 코드

# a=['a.jpg','b.txt','c.jpg']
# b=[i for i in a if '.jpg' not in i]
# print(b)

# def decorator(func):
#     def wrapper():
#         return func()
#     return wrapper

import time

# def abc()
#     print('안녕하세요')

# s=time.time()
# abc()
# e=time.time()
# print(f'프로그램 실행시간: {e-s}입니다')

def time_chk(func):
    def wrapper():
        s=time.time()
        result=func()
        e=time.time()
        print(f'실행시간: {e-s}')
        return result
    return wrapper

@time_chk
def abc():
    print('안녕하세요')

# abc()

@time_chk
def kkk():
    print(3+5*10000/50)

kkk()
