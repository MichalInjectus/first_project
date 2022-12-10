path = 'C:\\Users\\vdi-student\\Desktop\\first_project\\rozliczenie.csv'
mode = 'r'
with open(path, mode) as plik:
    content = plik.readlines()

print(content)
for i in range (len(content)):
    content[i] = content[i].split(',')
print(content)