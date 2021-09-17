from typing import Any, List, IO
import io
import os
import re

# import isolate info & remove '/n'
fhandle: IO = io.open("/nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/file_paths/isolates.txt", "r")

line: str
isolist: List[str] = list()
for line in fhandle:
    linestripped: str = line.strip()
    isolist.append(linestripped)
  
# map reads to reference
index: str
for index in isolist:
    output: str = "bwa mem -R '@RG\\tID:"+index+"\\tLB:"+index+"\\tPL:ILLUMINA\\tPM:HISEQ\\tSM:"+index+"' ./reference/streptococcus_macedonicus_pangenome ./seq_files/trimmed_seqs/"+index+"_1P.fastq.gz ./seq_files/trimmed_seqs/"+index+"_2P.fastq.gz > ./seq_files/mapped_reads/raw_sam/"+index+".sam"
    
    os.system(output)
 
 # convert SAM to BAM, sort the BAM, and remove the unsorted BAM and compress the SAM.
index: str
for index in isolist:
    output: str = "samtools view -Sb ./seq_files/mapped_reads/raw_sam/"+index+".sam > ./seq_files/mapped_reads/raw_sort_bam/"+index+".bam"
    
    os.system(output)

    os.system("gzip ./seq_files/mapped_reads/raw_sam/"+index+".sam")
    
    output2: str = "gatk SortSam -I seq_files/mapped_reads/raw_sort_bam/"+index+".bam -O seq_files/mapped_reads/raw_sort_bam/"+index+"_sorted.bam -SORT_ORDER coordinate"
    
    os.system(output2)
    
    os.system("rm ./seq_files/mapped_reads/raw_sort_bam/"+index+".bam")
