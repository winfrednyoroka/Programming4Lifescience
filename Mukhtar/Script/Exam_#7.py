from path import Path
import os

files = Path('../Files')


with open('../Result/all_sequence_headers.txt', 'w') as f_out:
    for file_name in files.walk('*.fasta'):
        with open(file_name, 'r') as f_in:
            data = f_in.readlines()

            #length 
            for line in data:
                if line[0] == '>':
                    f_out.write(line)



        # print('%s is %d' %(file_name,length))
        # print(data)
        # open = data.index('>', end)  
        # print(open)
        #     end = data.find('\n', open)
    #     print(end)
    #     file_header = data[open:end]    #Extract the file header            
    #     print(file_header)
    # #search for the next position
    #     open = end
       

# #open all fasta sequence
# with open('all_sequence_headers.txt', 'w') as f_out:
#     for file_name in files.walk('*.fasta'):
#         with open(file_name, 'r') as f_in:
#             data = f_in.read()
                          
#         #initialize end
#         end = 0
#         #length 
#         length = len(data.split('>'))

#         for i in range(length): 
#             open = data.find('>', end)  
#             end = data.find('\n', open)
#             file_header = data[open:end]    #Extract the file header            
#             #search for the next position
#             open = end
#             f_out.write(file_header)
      