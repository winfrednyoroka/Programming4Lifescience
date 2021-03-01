from path import Path

files = Path('../Files')
for file_name in files.walk('*.fasta'):
    with open(file_name) as f_in:
        data = f_in.read()
    count = 0
    for line in data:
        if line == '>':
            count += 1
    print('%s + has %d sequences' %(file_name, count))
            