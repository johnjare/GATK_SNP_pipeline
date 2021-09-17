from typing import Any, List, IO
import io
import os
import re

os.system("ls -d /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/raw_seqs/* > ./file_paths/raw_seqs.txt")

fhandle: IO = io.open("./file_paths/raw_seqs.txt", "r")

line: str
seqlist: List[str] = list()

for line in fhandle:
    linestripped: str = line.strip()
    seqlist.append(linestripped[:-14])


index: str
R1_tag: str = "1_001.fastq.gz"
R2_tag: str = "2_001.fastq.gz"
    
for index in set(seqlist):
    # change the letters in the bracket below (i.e. E and T) to match the letters used in the isolate names - for Acinetobacter isolates this will be a C. 
    isolate: str = re.findall(r"[E,T]{1}[0-9]{1,3}", index)
    output: str = "java -jar /local/cluster/bin/trimmomatic.jar PE -phred33 "+ index+R1_tag + " " + index+R2_tag + " ILLUMINACLIP:NexteraPE-PE.fa:2:30:10 -baseout ./seq_files/trimmed_seqs/"+isolate[0]+".fastq.gz HEADCROP:10 LEADING:3 SLIDINGWINDOW:10:30 MINLEN:100"

    os.system(output)
