path = ('C:\\Users\\vdi-student\\Desktop\\first_project\\rozliczenie.csv):
mode = 'r'
with open(path, mode) as plik:
    content = plik.redlines()

print(dontent)
for i in range (len(content)):
    content[1] = content[i].split','