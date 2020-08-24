
word_set = set()
filepath = 'word-list.txt'

print("Reading words from word list...")
with open("word-list.txt") as fp:
    for cnt, line in enumerate(fp):
        if cnt % 100000 == 0:
            print("Read " + str(cnt) + " lines")
        word_set.add(line)


print("Reading from word list is complete!")
print("Writing to word set file...")
with open("word-set.txt", "w") as output:
    output.write('\n'.join(word_set))

print("Writing to word set is complete!")