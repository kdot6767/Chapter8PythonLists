filename = input("Enter file name: ")
file = open(filename)

word_list = []

for line in file:
    words = line.split()

    for word in words:
        if word not in word_list:
            word_list.append(word)

word_list.sort()

print(word_list)