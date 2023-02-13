# 4.1 create a file and call it lyrics.txt

open('lyrics.txt', 'w')

# 4.2
file = open('songs.docx', 'w')
file.writelines(['Hello\n', 'hello2\n', 'hello3'])

# 4.3
file = open('songs.docx', 'r')
print(file.readlines())


file.seek(0)
print(file.read())


# virker ikke så godt
file.seek(0)
lines = file.readlines()
file.seek(0)
for line in lines:
    print(file.readline())

