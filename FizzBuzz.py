# Nama: Muhammad Hasan Ghani
# NIM: 251011700638

start = 1
end = 100

for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        hasil = "FizzBuzz"
    elif i % 3 == 0:
        hasil = "Fizz"
    elif i % 5 == 0:
        hasil = "Buzz"
    else:
        hasil = i

    print(hasil)