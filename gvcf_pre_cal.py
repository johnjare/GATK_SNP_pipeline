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
    output: str = "gatk --java-options '-Xmx28g' HaplotypeCaller -R /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/reference/streptococcus_macedonicus_ACA-DC_198.fna -I /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/mapped_reads/marked_bam/"+index+"_duplicates.bam -O /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/variant_calls/pre_calibration/per_isolate/"+index+".vcf.gz -ERC GVCF -ploidy 1"
    
    os.system(output)
