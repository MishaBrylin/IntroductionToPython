# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
f = open('file1.txt', 'r')
data = f.read()
f.close()
print(data)


data_RLE = ''
z = 1
prev_i = ''

for i in data:
    if prev_i != i:
        if prev_i != '':
            data_RLE += str(z) + prev_i
            z = 1
            prev_i = i
        else:
            prev_i = i
    else:
        if prev_i != '':
            z += 1
        else:
            prev_i = i
data_RLE += str(z) + prev_i


f = open('file2.txt', 'w')
f.write(data_RLE)
f.close()

f = open('file2.txt', 'r')
data = f.read()
f.close()
print(data)

decode = ''
z = ''
for i in data:
    if i.isdigit():
        z += i
    else:
        decode += i * int(z)
        z = ''


print(decode)
