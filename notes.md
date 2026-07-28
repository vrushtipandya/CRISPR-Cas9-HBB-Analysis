# Day 1

## Project Title
Computational CRISPR-Cas9 Guide RNA Design and Off-Target Analysis for the HBB Gene

## Objective
To learn CRISPR-Cas9 and perform computational guide RNA design and off-target analysis for the HBB gene.

## Today's Work
- Created project folder
- Created subfolders
- Opened project in VS Code
- Created Day 1 notes
Gene Symbol: HBB
Gene Name: Hemoglobin Subunit Beta
Organism: Homo sapiens (Human)
Chromosome: 11

Observation:
Today I learned how to search and identify the HBB gene using the NCBI Gene database.
# Day 2

## Date
20 July 2026

## Objective
To explore the HBB gene transcript and learn how to obtain the DNA sequence for CRISPR analysis.

## Work Completed

1. Opened the official NCBI HBB Gene page.
2. Explored the HBB gene information.
3. Opened the transcript record (NM_000518.5).
4. Reached the NCBI Nucleotide page.
5. Opened the FASTA sequence page.
6. Learned that FASTA is the standard format used to store DNA sequences.
7. Created the project data folder for storing sequence files.

## Observation

Today I understood the difference between the Gene page, Transcript page, and Nucleotide page. I also learned what a FASTA sequence is and why it is required for CRISPR guide RNA design.

## Problem Faced

I initially tried to save the FASTA page using Ctrl + S, which saved the webpage (HTML) instead of the FASTA file. I learned that the correct method is to use the download option provided by NCBI.

## Skills Learned

- NCBI Gene Database
- NCBI Nucleotide Database
- Transcript accession (NM_000518.5)
- FASTA format
- Basic bioinformatics workflow

## Next Day Plan

- Download the FASTA file correctly.
- Read the FASTA file using Python.
- Start coding the CRISPR project.
# Day 3 – HBB Gene Sequence Analysis

## Objective
Download the HBB gene sequence and calculate its GC content using Python.

## Steps Performed
1. Created the CRISPER_Gene_Editing_project folder.
2. Created data, scripts, and notes folders.
3. Downloaded the HBB gene sequence in FASTA format from NCBI.
4. Saved the file as HBB_sequence.fasta.
5. Wrote a Python script to calculate GC content.
6. Successfully executed the script.

## Result
GC Content = 51.27%

## Conclusion
The GC content of the HBB gene sequence is *51.27%*. The Python program successfully read the FASTA file and calculated the percentage of G and C nucleotides.
# Day 4 – DNA Sequence Analysis

## Objective
To analyze the HBB gene sequence using Python.

## Work Done
1. Created a Python script named sequence_analysis.py.
2. Read the HBB FASTA sequence.
3. Calculated:
   - Sequence Length
   - Number of Adenine (A)
   - Number of Thymine (T)
   - Number of Guanine (G)
   - Number of Cytosine (C)
## Result
- Sequence Length = 628
- A Count = 139
- T Count = 167
- G Count = 165
- C Count = 157

## Conclusion
The nucleotide composition of the HBB gene was successfully analyzed using Python.
# Day 5 – Reverse Complement Analysis

## Objective
To generate the reverse complement sequence of the HBB gene using Python.

## Work Done
1. Created a Python script named reverse_complement.py.
2. Read the HBB FASTA sequence.
3. Generated the reverse sequence.
4. Converted the reverse sequence into its complementary DNA sequence.
5. Displayed the reverse complement sequence.

## Result
Reverse Complement Sequence = Successfully Generated

## Conclusion
The reverse complement sequence of the HBB gene was successfully generated using Python. This sequence can be used for further bioinformatics analysis such as CRISPR guide RNA design, primer design, and sequence comparison.
# Day 6
– PAM Site Identification

## Objective
To identify PAM (Protospacer Adjacent Motif) sites in the HBB gene sequence using Python.

## Work Done
1. Created a Python script named pam_finder.py.
2. Read the HBB FASTA sequence.
3. Scanned the sequence for PAM motifs (NGG).
4. Displayed the position of each PAM site.
5. Counted the total number of PAM sites.

## Result
Total PAM Sites Found = 52

## Conclusion
A total of 52 PAM (NGG) sites were identified in the HBB gene sequence. These PAM sites can be used to design potential CRISPR-Cas9 guide RNAs for gene editing.
# Day 7 – Guide RNA Selection

## Objective
To identify potential CRISPR-Cas9 guide RNA candidates from the HBB gene sequence.

## Work Done
1. Extracted 20-nucleotide guide RNA sequences located immediately before PAM (NGG) sites.
2. Generated multiple candidate guide RNAs.
3. Compared the candidate guide RNAs.
4. Selected one guide RNA for further analysis.

## Selected Guide RNA
Guide RNA: AAGGTGAACGTGGATGAAGT

PAM: TGG

## Conclusion
A potential CRISPR guide RNA was successfully selected from the HBB gene for further GC content and off-target analysis.
Day 7 – Guide RNA GC Content Analysis

## Aim
To calculate the GC content of the selected guide RNA using Python.

## Objective
The objective of this experiment is to determine the percentage of Guanine (G) and Cytosine (C) nucleotides present in the selected guide RNA sequence. GC content is an important parameter in CRISPR-Cas9 guide RNA design because it affects the stability and binding efficiency of the guide RNA.

## Selected Guide RNA
TTCCGGCGCGCCGAGTCCTT

## Python Code

python
guide = "TTCCGGCGCGCCGAGTCCTT"

g = guide.count("G")
c = guide.count("C")

gc = ((g + c) / len(guide)) * 100

print("Guide RNA =", guide)
print("Length =", len(guide))
print("GC Content =", round(gc, 2), "%")


## Output

Guide RNA = TTCCGGCGCGCCGAGTCCTT

Length = 20

GC Content = 80.0 %

## Explanation

The selected guide RNA sequence was analyzed using a Python program. The program counted the total number of Guanine (G) and Cytosine (C) nucleotides present in the sequence and calculated the GC content using the following formula:

GC Content (%) = ((G + C) / Total Number of Nucleotides) × 100

The guide RNA contains 20 nucleotides, and the calculated GC content is 80.0%.

## Observation
guide rna length = 20 nuleotides
gc content=80.0%
* The Python program successfully calculated the GC content.

## Result

The GC content of the selected guide RNA was successfully determined using Python.

## Conclusion

The selected guide RNA contains 20 nucleotides with a GC content of 80.0%. The GC content analysis was successfully completed using Python, and the guide RNA was further evaluated using the CRISPOR web tool for CRISPR-Cas9 guide RNA analysis.
# Day 8 – CRISPOR Guide RNA Evaluation and Off-Target Analysis

## Aim

To evaluate the selected guide RNA using the CRISPOR web tool and analyze its efficiency, specificity, and predicted off-target effects.

## Objective

The objective of this experiment is to evaluate the selected guide RNA using the CRISPOR online tool. CRISPOR predicts guide RNA efficiency, specificity, PAM sequence, and possible off-target sites to identify the most suitable guide RNA for CRISPR-Cas9 gene editing.

## Software Used
- CRISPOR (https://crispor.tefor.net/)
- Human Genome (hg38)
- CRISPR-Cas9 (SpCas9)
- PAM Sequence: NGG

## Procedure

1. Open the CRISPOR website.
2. Paste the HBB gene DNA sequence into the sequence input box.
3. Select the Human (hg38) reference genome.
3. Select the Human (hg38) reference genome.
4. Select the NGG PAM sequence for SpCas9.
5. Click the Submit button.
6. Wait for CRISPOR to analyze the sequence.
7. Observe the guide RNA ranking table.
8. Select the guide RNA with the highest specificity score.
9. Record the efficiency score, specificity score, and predicted off-target information.

## Selected Guide RNA

Guide RNA:
TTCCGGCGCGCCGAGTCCTT

PAM:
AGG

## CRISPOR Results

MIT Specificity Score = 97

CFD Specificity Score = 98

Doench 2016 Efficiency Score = 47

Moreno-Mateos Score = 57

Predicted Off-Target Sites = 14

## Observation

* CRISPOR successfully analyzed the HBB gene sequence.

* The selected guide RNA showed high specificity.

* The predicted efficiency score indicates that the guide RNA is suitable for CRISPR-Cas9 targeting.

* The number of predicted off-target sites is low and acceptable for further analysis.

## Result

The selected guide RNA was successfully evaluated using the CRISPOR web tool. The guide RNA showed high specificity and acceptable efficiency for CRISPR-Cas9 gene editing.

## Conclusion

CRISPOR analysis confirmed that the selected guide RNA is a suitable candidate for targeting the HBB gene. The guide RNA demonstrated high specificity, acceptable efficiency, and a manageable number of predicted off-target sites, making it appropriate for further CRISPR-Cas9 research.
# Day 9 – Final Project Summary

## Aim

To summarize the complete CRISPR-Cas9 guide RNA design workflow for the HBB gene using Python and the CRISPOR web tool.

## Objective

The objective of this project is to identify and evaluate a suitable guide RNA for the HBB gene using bioinformatics tools. The workflow includes DNA sequence analysis, GC content calculation, reverse complement generation, PAM site identification, guide RNA selection, and CRISPOR evaluation.

## Workflow Summary

The following steps were successfully completed during the project:

1. Downloaded the HBB gene DNA sequence from the NCBI database.
2. Read the FASTA sequence using Python.
3. Calculated the GC content of the HBB gene.
4. Performed sequence analysis.
5. Generated the reverse complement sequence.
6. Identified PAM (NGG) sites.
7. Extracted 20-nucleotide guide RNA candidates.
8. Calculated the GC content of the selected guide RNA.
9. Evaluated the guide RNA using the CRISPOR web tool.
10. Selected the best guide RNA based on specificity and efficiency scores.

## Final Results

Gene: HBB (Hemoglobin Beta)

Selected Guide RNA:
TTCCGGCGCGCCGAGTCCTT

PAM:
AGG

Guide RNA Length:
20 nucleotides

MIT Specificity Score:
97

CFD Specificity Score:
98

Doench 2016 Efficiency Score:
47

Moreno-Mateos Score:
57

Predicted Off-Target Sites:
14

## Observation
* The HBB gene sequence was successfully analyzed using Python.
* GC content and reverse complement were calculated successfully.
* PAM sites and guide RNA candidates were identified.
* The selected guide RNA showed high specificity and acceptable efficiency.
* CRISPOR successfully evuluated the selected guide rna
##Result
a suitable guide RNA for the HBB gene was successsfully and evaluated using python and CRISPOR
##conclusion
this project successfully demonstrated the complate bionformatics workflow for CRISPER-cas9 guide RNA design trageting the HBB gene.python was used for sequance processing and guide RNA extraction,while CRISPOR was used to evaulate guide RNA efficency,specificity,and predicated off-target sites.the selected  guide RNA showed high specificity and is suitable candidate for future CRISPR- Cas9 gene editing studies

