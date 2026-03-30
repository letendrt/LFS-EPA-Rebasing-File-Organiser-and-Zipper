# Autofile Organiser and Zipper
# Developed by: Thierry Letendre 
# On behalf of: Scholars Portal/Odesi/Borealis/MarkIt group
# Note: Recommended to run on Windows - may require edits otherwise

################################################################################
#------------------------------------LIBRARIES----------------------------------
################################################################################

import os
import shutil
import zipfile
import pandas as pd


################################################################################
#-------------------------FOLDER ARCHITECTURE PARAMETERS------------------------
################################################################################



# If one year, still put in list format - older to newer! (e.g., 2010, 2011, 2012, etc.)
# Example: rebasing_years = [2011, 2012, 2013, 2014, 2015, 2016]
rebasing_years = [2016, 2017]


# Year of the rebasing version
# Example: rebase_year = 2030
rebase_year = 2025


# The year of the last rebasing before this one
# Example: last_time_rebased = 2025
global last_time_rebased
last_time_rebased = 2025


# Directory to documentation location
# example: doc_folder_dir = r"C:\Users\thierry\Python Code\Autofile Organiser and Zipper\Documentation"
# KEEP THE 'r' BEFORE THE STRING (raw format) IF RUNNING IN WINDOWS
doc_folder_dir = r"copy\path\to\documentation\folder\here"

# Directory to data files (raw CSV, SPSS, PRN)
# Example: data_folder_dir = r"C:\Users\thierry\Python Code\Autofile Organiser and Zipper\Data_folder"
# KEEP THE 'r' BEFORE THE STRING (raw format) IF RUNNING IN WINDOWS
data_folder_dir = r"copy\path\to\data\folder\here"


# Select the language of folder architecture and CSV sheet (only one can be selected at a time)
# Comment out the one you are not using
language_setting = "French"
#language_setting = "English"


# Setting selection for whether to run the file architecture creation script
# Comment out the one you are not using
run_zipper = True
#run_zipper = False


create_csv_sheet = True
#create_csv_sheet = False



################################################################################
#-------------------------FOLDER ARCHITECTURE: CODE PROPER----------------------
################################################################################


root = data_folder_dir.split('\\')                   # Splitting directory val at directory indexing
root_folder = '\\'.join(root[:-1])                   # Setting root directory, derived from data_folder_dir defined above     


# Function that organises folders for each year and month of the rebasing
# Takes 5 arguments (all of which I defined above, unde "FOLDER ARCHITECTURE PARAMETERS")
def folder_architecture(language_setting, rebasing_years, rebase_year, doc_folder_dir, data_folder_dir):
    
    # Checking English language parameters to set folder name language
    if language_setting == "English":
        month_list = ['January', "February", "March",
                      "April", "May", "June",
                      "July", "August", "September",
                      "October", "November", "December"]
        rebased = 'rebased'
        data = "Data"
        raw = "RAW"
        lfs = "LFS"
    
    
    # Checking French language parameters to set folder name language
    elif language_setting == "French":
        month_list = ['janvier', 'fevrier', 'mars', 
                      'avril', 'mai', 'juin', 
                      'juillet', 'aout', 'septembre', 
                      'octobre', 'novembre', 'decembre']
        
        rebased = 'remanie'
        data = "Donnees"
        raw = "Brutes"
        lfs = "EPA"
    
    # Setting up list of month integer values
    num_val = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    
    
    os.mkdir(f"Root {rebased}")                       # Setting up name and creating top-level (root) directory
    c_pwd = os.getcwd()                               # Checks current working direcotry of the python code
    root_layer = rf'{c_pwd}\Root {rebased}'           # Assigns root directory to the variable 'root_layer'


    for year in rebasing_years:                       # For years in the list of years (defined in parameters section)
        os.chdir(root_layer)                          # Set current directory to the root layer (necessary for this recursive process)
        print()
        print("CREATING YEAR LAYER")        
        
        year_layer = f"micro{year}_{rebased}{rebase_year}"       # Setting up name for the year directory name
        os.mkdir(year_layer)                                     # Creating the year_layer folder for the current loop
        
        month_layer = rf'{root_layer}\{year_layer}'              # Setting up name for the month directory name
        os.chdir(month_layer)                                    # Changes working directory to the inside of the year folder
        
        print("CREATING MONTH LAYER & IMPORTING DOCUMENTATION")
        
        for months in month_list:                                                           # Iterating through months (within the year folder)
            os.chdir(month_layer)                                                           # Navigates back to the month layer (necessary for this recursive process)
            current_month_folder = f"micro{year}_{num_val[month_list.index(months)]}"       # Setting up name for the month LFS 
            os.mkdir(current_month_folder)                                                  # Creates LFS month folder
            print(current_month_folder)
            
            dataset_layer = rf"{month_layer}\{current_month_folder}"             # Setting up dataset layer directory name
            doc_layer = rf"{dataset_layer}\Documentation"                        # Setting up documentation layer directory name
            os.mkdir(doc_layer)                                                  # Creating documentation layer directory
            doc_dir = rf"{doc_folder_dir}\{year}"                                # Setting up name of folder from which documentation will be pulled                                
            shutil.copytree(doc_dir, doc_layer, dirs_exist_ok = True)            # Copy documentation folder directory into the indexed documentation folder
            
            data_layer = rf"{dataset_layer}\{data}"                          # Setting up data directory name
            os.mkdir(data_layer)                                             # Creating data directory name    
            
            raw_layer = rf"{data_layer}\{raw}"                               # Setting up name for raw data directory
            spss_layer = rf"{data_layer}\SPSS"                               # Setting up name for SPSS data directory
            os.mkdir(raw_layer)                                              # Creating raw data directory
            os.mkdir(spss_layer)                                             # Creating SPSS data directory
            
            csv_name = rf"pub{num_val[month_list.index(months)]}{str(year)[-2:]}.csv"      # Setting up to-be fetched CSV file name
            prn_name = rf"pub{num_val[month_list.index(months)]}{str(year)[-2:]}.prn"      # Setting up to-be fetched PRN file name
            spss_name = rf"{lfs}_{months}_{year}.sav"                                      # Setting up to-be fetched SPSS file name
            
            spss_file = rf"{data_folder_dir}\{spss_name}"                 # Setting up SPSS file to call for copying/zipping
            os.chdir(data_folder_dir)                                     # Navigate to the data folder/directory
            shutil.copy(spss_file, spss_layer)                            # Copying a raw copy of the SPSS file in the SPSS directory


            # Creating zipper with file path
            # Zipping file in file path directory
            with zipfile.ZipFile(rf'{raw_layer}\{csv_name}.zip', 'w') as zipf:
                zipf.write(csv_name)  
            with zipfile.ZipFile(rf'{raw_layer}\{prn_name}.zip', 'w') as zipf:
                zipf.write(prn_name)
            with zipfile.ZipFile(rf'{spss_layer}\{spss_name}.zip', 'w') as zipf:
                zipf.write(spss_name)
        
        
        os.chdir(month_layer)                      # Navigate to the month layer
        os.mkdir('Original')                       # Creating "original" copy folder (raw organised files)
        os.mkdir('ZIPs')                           # Creating "ZIPs" copy folder (zipped files for Borealis upload)
        print()
        
        for folder in os.scandir():                                                   # For folders in the current working directory
            if "micro" in folder.name:                                                # If micro is in the folder name (meaning it is a dataset folder)
                print(f'NOW ZIPPING {folder.name}')                                   
                shutil.make_archive(rf'{month_layer}\ZIPs\{folder.name}', "zip", 
                                    rf"{month_layer}", rf"{folder.name}")             # Create zipped copy of the dataset in the ZIPs folder
                shutil.move(folder.name, rf"Original\{folder.name}")                  # Move datset folder in the "Original" folder
    
   
    print('FILE FORMATTING COMPLETE')
    print()
    os.chdir(root_layer)                      # Navigate back to root directory



################################################################################
#-----------------------------------DOI FETCHER---------------------------------
################################################################################

# Function that parses through a list of all 2011-2025 LFS and EPA
# Takes 2 arguments - both of which are defined lower in the csv_template_creation function
def info_fetcher(month_and_year, cond):
    
    doi_df = pd.read_csv('RELEVANT_LFS_EPA.csv')                           # Read CSV file and convert to pandas dataframe
    val = doi_df[doi_df['Titles'].str.contains(f'{month_and_year}')]       # Find file names that contain the exact month_and_year label
    title_val = val.iloc[0]['Titles']                                      # Fetch dataset title 
    doi_val = val.iloc[0]['DOIs']                                          # Fetch dataset DOI
    
    edits = month_and_year.split(' ')               # Split the month and year 
    year = int(edits[1])                            # Fetch the year
    
    if cond == 1:                                      # If condition is 1
        return doi_val                                 # Return the dataset DOI
    
    elif cond == 2 and year < last_time_rebased:       # If condition is 2, and the dataset was previously rebased
        splits = title_val.split('[Canada]')           # Split the title on '[Canada]'
        to_remove = splits[1].strip()                  # Identify value from the title that needs to be edited at the next submission
        return to_remove                               # return the string that must be removed from the title during the rebasing process



################################################################################
#------------------------------CSV TEMPLATE CREATION----------------------------
################################################################################

# Function that creates the CSV file - is technically optional
# Can be a real time saver though. 
# Takes 4 arguments, all of which are defined above
def csv_template_creation(language_setting, rebasing_years, rebase_year, root_folder):
    
    os.chdir(root_folder)                                              # Set directory to root folder
    
    print('STARTING CSV SHEET CREATION')
    highest_year = rebasing_years[-1]                                  # Finds the top to-be rebased year
    lowest_year = rebasing_years[0]                                    # Finds lowest to-be rebased year
    
    
    # Setting up to-be populated dictionary. This dictionary is later converted to a CSV file
    dictionary = {"Year": [], "Month Name and Year": [], "Persistent Identifier": [], 
                  "DOI in Dataverse": [], 'Replace with /path': [], 'sav directory': [], 
                  'File Description': [], 'Title > Additions': [],
                  'Revision Additions: Citation > Descriptions': [],
                  'Replace w/File Name': [], 'Remove from Title': [],
                  'Keywords': [], 'Geographic Unit': [], 'WeightVariable': [],
                  'WeightException': [], 'Other Language Name': [],
                  'Other Language Month': [], 'Other Language Additions': []}
    
    # Assigns language settings to various variables 
    # - this is to prevent code redundency in French and English
    if language_setting == 'French':
        month_list_1 = ['janvier', 'février', 'mars','avril', 
                        'mai', 'juin','juillet', 'août', 
                        'septembre', 'octobre', 'novembre', 'décembre']
        
        month_list_2 = ['janvier', 'fevrier', 'mars','avril', 
                        'mai', 'juin','juillet', 'aout', 
                        'septembre', 'octobre', 'novembre', 'decembre']
        
        month_list_3 = ['January', "February", "March", "April", 
                         "May", "June", "July", "August", 
                         "September", "October", "November", "December"]
        
        rebase = "remanie"
        alt_REBASE = 'Rebased'
        data = 'Donnees'
        lfs = 'EPA'
        title_add = rf'[Remanié {rebase_year}]'
        geo_unit = 'Régions métropolitaines de recensement (RMR)'
        alt_name = 'Labour Force Survey,'
        keyword = "Emploi, Chômage, Employeur, Profession, Congé, Main-d'oeuvre, Conditions de travail, Milieu de travail"
    
    # Assigns language settings to various variables 
    # - this is to prevent code redundency in French and English
    if language_setting == "English":
        month_list_1 = ['January', "February", "March", "April", 
                         "May", "June", "July", "August", 
                         "September", "October", "November", "December"]
        
        month_list_2 = ['January', "February", "March", "April", 
                         "May", "June", "July", "August", 
                         "September", "October", "November", "December"]
        
        month_list_3 = ['janvier', 'février', 'mars','avril', 
                        'mai', 'juin','juillet', 'août', 
                        'septembre', 'octobre', 'novembre', 'décembre']       
        
        rebase = "rebase"
        alt_REBASE = 'Remanié'
        data = 'Data'
        lfs = 'LFS'
        title_add = rf'[Rebased {rebase_year}]'
        geo_unit = 'Census Metropolitan Area (CMA)'
        alt_name = 'Enquête sur la population active,'
        keyword = 'Employment, Unemployment, Employer, Vacation, Labour, Industries, Occupations, Hours of work, Work arrangements'
    
    
    df = pd.DataFrame(dictionary)                                  # Setting up dataframe with dictionary columns as headers
    
    
    month = 0                                                                                  # Setting up month loop
    num_val = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]         # Setting up month integers
    
    while highest_year != lowest_year - 1:                                                     # While not all years have been iterated through
        
        base_dir = rf'\Root {rebase}\micro{highest_year}_{rebase}{rebase_year}'                # Create base directory label for the year
        file = f'micro{highest_year}_{num_val[month]}'                                         # Setting up file to fetch
        
        
        row_dict = dictionary                                                                  # Create copy of dictionary
        
        ####################### start populating dictionary fields########################
        
        row_dict["Year"] = highest_year
        row_dict['Month Name and Year'] = f"{month_list_1[month]} {highest_year}"
        
        try:
            row_dict['Persistent Identifier'] = info_fetcher(row_dict['Month Name and Year'], 1)           # Check if copy of file already exists in CSV sheet
        except:
            row_dict['Persistent Identifier'] = '???'                                                      # If failure to find value, input ???
        
        try:
            row_dict['DOI in Dataverse'] = info_fetcher(row_dict['Month Name and Year'], 1).replace('doi:', 'doi.org/')               # Check if copy of file already exists in CSV sheet
        except:
            row_dict['DOI in Dataverse'] = '???'                                                                                      # If failure to find value, input ???
            
        row_dict['Replace with /path'] = rf'{base_dir}\ZIPs\micro{highest_year}_{num_val[month]}.zip'
        row_dict['sav directory'] = rf'{base_dir}\Original\micro{highest_year}_{num_val[month]}\{data}\SPSS\{lfs}_{month_list_2[month]}_{highest_year}.sav'
        row_dict['File Description'] = ''
        row_dict['Title > Additions'] = title_add
        row_dict['Revision Additions: Citation > Descriptions'] = ''
        row_dict['Replace w/File Name'] = rf'{lfs}_{month_list_2[month]}_{highest_year}.sav'
        row_dict['Remove from Title'] = info_fetcher(row_dict['Month Name and Year'], 2)
        row_dict['Keywords'] = keyword
        row_dict['Geographic Unit'] = geo_unit
        row_dict['WeightVariable'] = 'FINALWT'
        row_dict['WeightException'] = 'REC_NUM'
        row_dict['Other Language Name'] = alt_name
        row_dict['Other Language Month'] = rf'{month_list_3[month]}'
        row_dict['Other Language Additions'] = rf'[Canada] [{alt_REBASE} {rebase_year}]'

        
        df.loc[len(df)] = row_dict                 # Add dictionary line to our dataframe 
        month += 1                                 # Increase month increment
        
        if month == 12:                            # If month increment is at index value 12 (would be 13th month)
            highest_year -= 1                      # Pass to next year (decreasing)
            month = 0                              # Reset month index counter
    
    
    df.to_csv(f"Template_{title_add}.csv", index = False)            # Write CSV file
    print('FINISHED CSV SHEET CREATION')
    print()



################################################################################
#--------------------------FUNCTION RUNNING CONDITIONS--------------------------
################################################################################

# Runs function if conditions are met (defined in the top parameters selection section)
if run_zipper == True:
    folder_architecture(language_setting, rebasing_years, rebase_year, doc_folder_dir, data_folder_dir)

if create_csv_sheet == True:
    csv_template_creation(language_setting, rebasing_years, rebase_year, root_folder)
    
print('PROCESS COMPLETE')
