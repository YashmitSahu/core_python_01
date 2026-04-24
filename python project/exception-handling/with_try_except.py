print('before')

print('mid')

try:
    a= 10
    b= 0
    c= a/b
    print('division',c)
except ZeroDivisionError as e:
    print('exception',e)
except Exception as e:
    print('exception',e)
    print('after')

