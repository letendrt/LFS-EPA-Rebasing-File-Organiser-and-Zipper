# LFS-EPA-Rebasing-Automatic-File-Organiser-and-Zipper
Code to be used by future staff - automatically structures Labour Force Survey files for Borealis/Odesi submission.

## Code Purpose
1) Automatically formats month and year datasets for the Labour Force Survey and Enquête sur la population active rebasing.
2) Automatically creates a CSV template for subsequent rebasing script (includes DOIs, file paths, French/English alternative titles depending on selected language setting).
3) Mitigates mind-numbing file drag and drops.

## Minimum Python Requirements
1) Local IDE (Jupyter, Wing, PyCharm, etc.) on a windows machine.
2) Minimum python version: 3.8+.

## File Requirements
1) A singular folder with ALL to-be rebased datafiles - no sub-folders necessary (just toss in all the data files, both English and French files can be in the same data folder). Must include: raw PRN files, raw CSV files, and SPSS (.sav) files for every month and every year that are being rebased. PRN and CSV are language agnostic. Only SPSS files require their French counterparts (assuming rebasing is being done for both English and French, otherwise only the language being rebased need to be present in the folder).

   <kbd><img width="688" height="225" alt="image" src="https://github.com/user-attachments/assets/fa3b155a-fc09-4105-a092-02013992afe1" /></kbd>

2)  Documentation folder in which dataset documentation are split by year (documentation, in some cases, vary year over year, as such they must be seggregated in the folder of their respective years).  

## User Guide
