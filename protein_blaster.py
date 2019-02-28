import os
os.getcwd()
print('current working directory is:')
print(os.getcwd())
#we need to change this to work with any user or any OS
os.chdir('/Users/mattrump/Desktop/Lab/parg_evi/parg_fasta/') 
print('change directory to:')
print(os.getcwd())

#define num as an integer counter that starts at 1
num = 1

#define result as an empty string
result_str = ''

#import SeqID module from Bio python package
#create a list of sequence records
from Bio import SeqIO
records = list(SeqIO.parse("Ext_Parg_ppk.fasta","fasta"))

#import blast module & query the database for
#each record's sequence and append the return to the result_str variable
from Bio.Blast import NCBIWWW
for record in records:
   print("Processing Record Number " + str(num) + "\n")
   result = NCBIWWW.qblast("blastp", "nr", record.seq) #blast
   result_str += result.getvalue() + '\n'
   result.close()
   num += 1

#save blast as xml
save_file = open("blast.xml","w")
#save_file.write(result.read())
save_file.write(result_str)
save_file.close()


#parse blast data
result = open("blast.xml")
from Bio.Blast import NCBIXML
records = NCBIXML.parse(result)
blast_record = records.__next__()
for alignment in blast_record.alignments:
   for hsp in alignment.hsps:
       if hsp.expect <1e-160:
           print('****Alignment****')
           print('sequence:',alignment.title)
           print('length:', alignment.length)
           print('score:',hsp.score)
           #print('gaps:',hsp.gaps)
           print('e value:', hsp.expect)
           print(hsp.query[0:90]+'...')
           print(hsp.match[0:90]+'...')
           print(hsp.sbjct[0:90]+'...')