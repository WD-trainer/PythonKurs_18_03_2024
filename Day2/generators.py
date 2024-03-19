import time


def elementy():
    yield 'element numer 1'
    yield 'element numer 2'
    yield 'element numer 3'
    print("Cos w generatorze")
    yield 'element numer 4'


gen = elementy()

for e in elementy():
    print(e)


def potegi2(n:int):
    for x in range(1, n + 1):
        yield pow(2, x)


for p in potegi2(50):
    print(p)


def dziesieci():
    i = 1
    while True:
        yield i * 10
        i += 1


dz = dziesieci()
print(dz.__next__())
print(dz.__next__())
print(dz.__next__())

potegi22 = [2 ** i for i in range(100)]
generator_potegi = (2 ** i for i in range(1000000))
print(generator_potegi)
next(generator_potegi)
generator_potegi.__next__()

# print(generator_potegi[5])

for i in generator_potegi:
    print(i)
    if i > 2048:
        break


# for i in dziesieci():
#     print(i)

################################### f-string resources ####################################################
#http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf

#  Stworz generator ktory bedzie przyjmowal przez parametr ilosc elementow a nastepnie zwracal elementy o tresci
#  'element o indeksie x'( gdzie x bedzie numerem podawanego elementu) czekajac 1 sekunde przed zwrotem kazdego elementu.
def generator_elementow(ilosc: int):
    for i in range(ilosc):
        time.sleep(1)
        yield f'element o indeksie {i}'
        # yield print(f'element o indeksie {i}')


genrator = generator_elementow(3)
print(next(genrator))
next(genrator)
print(next(genrator))


#     Stwórz generator który będzie podawał nieskończenie wiele liczb parzystych.
#     Przetestuj go pobierając z niego kolejne wartości i wyświetlając je na konsoli.




for i in generator_parzysty():
    print(i)
    if i > 20:
        break