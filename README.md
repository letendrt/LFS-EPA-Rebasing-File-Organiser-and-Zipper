# LFS-EPA-Rebasing-File-Organiser-and-Zipper 🗃️🤐
Code to be used by future staff - automatically structures Labour Force Survey files for Borealis/Odesi submission.

## Code Purpose 🤔❓
1) Automatically formats month and year datasets for the Labour Force Survey and Enquête sur la population active rebasing.
2) Automatically creates a CSV template for subsequent rebasing script (includes DOIs, file paths, French/English alternative titles depending on selected language setting).
3) Mitigates mind-numbing file drag and drops.

## Minimum Python Requirements 🐍🔧
1) Local IDE (Jupyter, Wing, PyCharm, etc.) on a windows machine.
2) Minimum python version: 3.8+.

## File Requirements 📁🐜
1) A singular folder with ALL to-be rebased datafiles - no sub-folders necessary (just toss in all the data files, both English and French files can be in the same data folder). Must include: raw PRN files, raw CSV files, and SPSS (.sav) files for every month and every year that are being rebased. PRN and CSV are language agnostic. Only SPSS files require their French counterparts (assuming rebasing is being done for both English and French, otherwise only the language being rebased need to be present in the folder).

<kbd><img width="1352" height="222" alt="image" src="https://github.com/user-attachments/assets/d87ed534-17fb-427a-bd4b-34c30a3aa883" /></kbd>

2)  Documentation folder in which dataset documentation are split by year (documentation, in some cases, vary year over year, as such they must be seggregated in the folder of their respective years).

<kbd><img width="1296" height="465" alt="image" src="https://github.com/user-attachments/assets/9f760d5d-0cd2-409d-beeb-903b9fc1fbe1" /></kbd>

## User Guide 🔍🛃
⚠️ For successful file organisation/zipping and CSV sheet template creation, please make sure to read the steps below! ⚠️



