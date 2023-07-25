def func(a):
    if a==a[::-1]:  
        return True
    else:
        return False
    # выполняем проверку на палиндром через обратный перебор
print(func('топот'))
