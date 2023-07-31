# list comprehensions

salaries = [2000,3000,4000,5000]

x = [salary * 2 if salary < 3000 else salary * 0 for salary in salaries] #eğer sadece if kullanıyorsak for'un sağına, if else kullanıyorsak for'un soluna yazmamız gerekir
# list comprehensions yapısı içine fonksiyon da çağırabilirsin

print(x)

# dict comprehensions

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
print({k: v ** 2 for (k, v) in dictionary.items()}, {k.upper(): v ** 2 for (k, v) in dictionary.items()})

