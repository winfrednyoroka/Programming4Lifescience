#function to obtain reverse complimentary strand from parent strand input
def reverse_strand(seq):
    complementary_strand =""
    for base in seq:
        if base == "A":
            complementary_strand += "T"
        elif base == "T":
            complementary_strand += "A"
        elif base == "G":
            complementary_strand += "C"
        else:
            complementary_strand += "G"
    print(complementary_strand)
seq1 = "ATCGATCGATCAGATTTAAACGGCATATCATAGCACGTACATGACG"
reverse_strand(seq1)

#for loop 4-10
for numbers in range(4, 11):
    print(numbers)
x=0
print("")
#while loop
while x < 6:
    print(x)
    x = x+1

#opening sequence and analysis
myfile = open("C:/Users/playe/Google Drive/SeqfromfileQ4.fasta")
myfile_content = myfile.read()
print(myfile_content)

#4 (c)
for data in myfile_content:
    atg_count = myfile_content.count("ATG")
print(atg_count, "is the ATG count")
print('')
print('')

#4 (b)
myfile_2 = open("C:/Users/playe/Google Drive/SeqfromfileQ4.fasta")
high_base = ""
current_length = 0
max_length = 0
current_base = ""
myfile2 = myfile_2.readlines()
myfile2 = myfile2[1:]
sequence = "".join(myfile2)
for base in sequence:
    if current_base == base:
        current_length += 1
    else:
        current_length = 1
    if current_length > max_length:
        max_length = current_length
        high_base = current_base
    current_base = base
print(high_base, "is the highest repeating base", max_length, "is the times it repeats")
print('')
print('')
    


##bash script for Q5
## ./hello.sh
## echo hello
## read varname
## echo $varname how are you?

#Q6
import re
fasta_file1 = open("C:/Users/playe/Google Drive/sequence1.fasta")
fasta_file2 = open("C:/Users/playe/Google Drive/sequence_2.fasta")
fasta_file3 = open("C:/Users/playe/Google Drive/sequence_3.fasta")
count_seq = 0
for line in fasta_file1.readlines():
    if line.startswith(">"):
        count_seq += 1
print("sequence1.fasta:",count_seq)
print("")
count_seq1 = 0
for line in fasta_file2.readlines():
    if line.startswith(">"):
        count_seq1 += 1
print("sequence_2.fasta:",count_seq1)
print("")
count_seq2 = 0
for line in fasta_file3.readlines():
    if line.startswith(">"):
        count_seq2 += 1
print("sequence_3.fasta:",count_seq2)

#q7

myfile_header = open("all_sequence_headers.txt", "w")
line_header = []
with open("C:/Users/playe/Google Drive/sequence1.fasta") as myfile_h1:
    for line in myfile_h1.readlines():
        if line.startswith(">"):
            line.strip
            line_header.append(str(line))
        continue
str_h = ""
for item in line_header:
    str_h += item
print(str_h)
myfile_header.write(str_h)

myfile_header1 = open("all_sequence_headers.txt", "w")
line_header1 = []
with open("C:/Users/playe/Google Drive/sequence_2.fasta") as myfile_h2:
    for line in myfile_h2.readlines():
        if line.startswith(">"):
            line.strip
            line_header1.append(str(line))
        continue
str_h1 = ""
for item in line_header1:
    str_h1 += item
myfile_header.write(str_h1)

myfile_header2 = open("all_sequence_headers.txt", "w")
line_header2 = []
with open("C:/Users/playe/Google Drive/sequence_3.fasta") as myfile_h3:
    for line in myfile_h3.readlines():
        if line.startswith(">"):
            line.strip
            line_header2.append(str(line))
        continue
str_h2 = ""
for item in line_header2:
    str_h2 += item
myfile_header.write(str_h2)
myfile_header.close()
    



 


    





