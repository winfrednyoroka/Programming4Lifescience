def compliment(DNA="ATCGATCGATCAGATTTAAACGGCATATCATAGCACGTACATGACG"):
    d = {'A':'T', "T": "A",'C':'G', 'G': "C"}
    complement = ''
    for i in DNA:
        complement += d.get(i)
    reverse_compliment = complement[::-1]
    return reverse_compliment 

print("reverse complement of the DNA is: " + compliment())


#Write a for loop that prints values 4-10 (2.5mks)

for i in range(4,10):
    print(i)

#Create a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console. (2.5mks)

x = 0

while x <= 5:
    print(x)
    x += 1



#Using a DNA sequence read from file, answer the following questions: (20mks)

# import os
# os.setwd()
# from path import Path
#  f = Path(’os.getcwd()+'/Files')

#get the file
with open('../Files/SeqfromfileQ4.fasta', 'r') as fh:
    lines = fh.read()
#split and get the name of the fasta sequence
name_of_seq = lines.split('\n')[0][1:]
#get the DNA sequences
sequence = ''.join(lines.split('\n')[1:])
print(sequence)
#gives us unique character in DNA sequence
unique_character = set(sequence)

print('Unique set f charater in DNA is:' + str(unique_character))

#What is the letter and length of the longest repeating region?

import re
A = re.findall('A+|C+|G+|T+', sequence)
longest = max(A, key = len)
len_longest = len(longest)

print('longest sequence: ' + longest + ',' + 'length of longest: ' + str(len_longest) )


    

#How many ’ATG’s are in the DNA string?
sequence.find("ATG")





	


