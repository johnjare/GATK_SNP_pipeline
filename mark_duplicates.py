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
     
index: str
for index in isolist:
    output: str = "java -jar /local/cluster/picard-tools-2.0.1/dist/picard.jar MarkDuplicates I=./seq_files/mapped_reads/raw_sort_bam/"+index+"_sorted.bam O=./seq_files/mapped_reads/marked_bam/"+index+"_duplicates.bam M=./seq_files/mapped_reads/marked_bam/"+index+"_metrics.txt"
    
    os.system(output)

    output2: str = "gatk BuildBamIndex -I seq_files/mapped_reads/marked_bam/"+index+"_duplicates.bam"
    
    os.system(output2)


