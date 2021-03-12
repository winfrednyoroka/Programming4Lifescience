#Write a function that reverse complements this sequence (10mks) DNA="ATCGATCGATCAGATTTAAACGGCATATCATAGCACGTACATGACG"
def reverse_complement (DNA):
    """ Computes the reverse complement of the DNA sequence. """
    complement = ""
    for nucleotide in DNA:
        if nucleotide == "A":
            complement = "T" + complement
        elif nucleotide == "T":
            complement = "A" + complement
        elif nucleotide == "G":
            complement = "C" + complement
        elif nucleotide== "C":
            complement = "G" + complement
    return complement
DNA="ATCGATCGATCAGATTTAAACGGCATATCATAGCACGTACATGACG"
reverse_complement(DNA)
#Write a for loop that prints values 4-10 (2.5mks)
for value in range(4, 11):
    print(value)
#Create a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console. (2.5mks)
x = 0
while x <= 5:
    print(x)
    x +=1
#Using a DNA sequence read from file, answer the following questions: (20mks) a. Show that the DNA string contains only four letters
f= open("SeqfromfileQ4noheader.fasta","w+")
lines = open("SeqfromfileQ4.fasta").readlines()

for line in lines:
    if line[0] != '>':
        f.write(line[1:])
f.close()

filename = "SeqfromfileQ4noheader.fasta"
with open(filename) as file_object:
    DNA= file_object.read()
    
def validate_dna (DNA):
    """ Checks if DNA sequence is valid. Returns True is sequence is valid, or False otherwise. """ 
    seqm = DNA
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G")+ seqm.count("T") 
    if valid == len(seqm): 
        return True 
    else: 
        return False
    
validate_dna(DNA)
#Write a script that counts the number of sequences in each fasta file in the Exam_dataset. It should print to console the name of the file and the number of sequences, each separated by a tab. For example, if sequence1.fasta has 10 sequences, it should print: sequence1.fasta: 10
filename = "SeqfromfileQ4.fasta"
with open(filename) as file_object:
    DNA= file_object.read()
fh = open("SeqfromfileQ4.fasta")
n = 0
for line in fh:
    if line.startswith(">"):
        n += 1
        print(n)
fh.close()
from Bio import SeqIO

records = list(SeqIO.parse("SeqfromfileQ4.fasta", "fasta"))
print("SeqfromfileQ4.fasta: %i" % len(records))
from Bio import SeqIO

records = list(SeqIO.parse("Sequence1.fasta", "fasta"))
print("Sequence1.fasta: %i" % len(records))
from Bio import SeqIO

records = list(SeqIO.parse("Sequence1.fasta", "fasta"))
print("Sequence2.fasta: %i" % len(records))
from Bio import SeqIO

records = list(SeqIO.parse("Sequence1.fasta", "fasta"))
print("Sequence3.fasta: %i" % len(records))
#Write a script that extracts the sequence headers of all the provided fasta files, and writes the output in the Results directory to a file all_sequence_headers.txt
f= open("all_sequence_headers.txt","w+")
lines = open("SeqfromfileQ4.fasta").readlines()

for line in lines:
    if line[0] == '>':
        f.write(line[1:])
        
lines = open("Sequence1.fasta").readlines()

for line in lines:
    if line[0] == '>':
        f.write(line[1:])
        
lines = open("Sequence_2.fasta").readlines()

for line in lines:
    if line[0] == '>':
        f.write(line[1:])

lines = open("Sequence_3.fasta").readlines()

for line in lines:
    if line[0] == '>':
        f.write(line[1:])
        
f.close()