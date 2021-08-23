# 1.

name = input("what is your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.

in_file = open("name.txt", 'r')
name = in_file.read()
print("your name is: ", name)

# 3.

in_file = open("numbers.txt", 'r')
sum = 0
lines_to_read = [0, 2]
for line in in_file:
    line = int(line)
    while line != 400:
        sum += line
print(sum)
