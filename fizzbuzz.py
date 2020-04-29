g = 1
i = 1
h = input("First Number: ")

while h.isdigit() != 1:
    h = input("First Number: ")
    if h.isdigit():
        break
c = input("Second Number: ")
while c.isdigit() != 1:
    c = input("First Number: ")
    if c.isdigit():
        break
hn = input("FizzBuzz times: ")
while hn.isdigit() != 1:
    hn = input("FizzBuzz times: ")
    if hn.isdigit():
        break
c = int(c)
h = int(h)
set = str(h)
hn = int(hn)
array = []
array2 = []
for x in range(hn):
    m = h*x
    if m < hn:
        array.append(str(m))
    else:
        print(x)
        break
for f in range(hn):
    k = c*f
    if k < hn:
        array2.append(str(k))
    else:
        print(f)
        break
while i != hn:
    istr = str(i)
    n = istr.find(set)
    if n != 1:
        if istr in array:
            if istr in array2:
                print("FizzBuzz")
                i = i + 1
            else:
                print("Fizz")
                i = i + 1
        else:
            if istr in array2:
                print("Buzz")
                i = i + 1
            else:
                print(i)
                i = i + 1
    else:
        if istr in array2:
            print("FizzBuzz")
            i = i + 1
        else:
            print("Fizz")
            i = i + 1
