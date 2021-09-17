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
    output: str = "gatk BaseRecalibrator -I /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/mapped_reads/marked_bam/"+index+"_duplicates.bam -R /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/reference/streptococcus_macedonicus_pangenome.fa --known-sites /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/variant_calls/pre_calibration/snps_cohort_precal-filtered.vcf.gz -O /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/mapped_reads/recal_tables/"+index+".table"

    os.system(output)
    
    output2: str = "gatk ApplyBQSR -R /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/reference/streptococcus_macedonicus_pangenome.fa -I /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/mapped_reads/marked_bam/"+index+"_duplicates.bam --bqsr-recal-file /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/mapped_reads/recal_tables/"+index+".table -O /nfs3/FST/Waite-Cusic_Lab/til_residency/streptococcus/seq_files/mapped_reads/recal_bam/"+index+"_recal.bam"
    
    os.system(output2)

