# ******************************************************************************************** #
# Packages                                                                                     #
# ******************************************************************************************** #
import urllib.request as ur
import pandas as pd
import zipfile
import os


# ******************************************************************************************** #
# Definition of Functions                                                                      #
# ******************************************************************************************** #

# Downloads the respective forms from the quarterly statements of the SEC #
def download(year_,qtr_):
    securl = "https://www.sec.gov/Archives/edgar/full-index/" + str(year_) + "/QTR" + str(qtr_) + "/company.zip"
    downloadfile = downloadfolder + "\\" + str(year_) + "QTR" + str(qtr_) + ".zip"
    ur.urlretrieve(securl, downloadfile)

# Unzip the quarterly files #
def unzip(year_,qtr_):
    path_to_zip_file = downloadfolder + "\\" + str(year_) + "QTR" + str(qtr_) + ".zip"
    directory_to_extract_to = exportfolder
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()

# Rename the quarterly text file #
def textfile(year_,qtr_):
    path_to_idx_file = exportfolder + "\\Company.idx"
    base = exportfolder + "\\"+ str(year_) + "QTR" + str(qtr_)
    os.rename(path_to_idx_file, base + ".txt")

# Removes the first lines of the text-file to extract the table #
def removehead(year_,qtr_):
    path_to_txt_file = exportfolder + "\\" + str(year_) + "QTR" + str(qtr_) + ".txt"
    with open(path_to_txt_file,"r+") as f:
        d = f.readlines()
        f.seek(0)
        for i,row in enumerate(d):
            if i > 9:    
                f.write(row)
        f.truncate()

# Defines the positions at which the text is split into a table #
def seperation_points(year_,qtr_):
    path_to_txt_file = exportfolder  + "\\" + str(year_) + "QTR" + str(qtr_) + ".txt"
    with open(path_to_txt_file, "r") as f:
        head_ = str(f.readlines()[0])
    comp_end = head_.find("Form") - 1
    form_end = head_.find("CIK") - 1
    cik_end = head_.find("Date") - 1
    fdate_end = head_.find("File Name") - 1
    cell_links = {"comp_end": comp_end, "form_end": form_end, "cik_end": cik_end,
                  "fdate_end": fdate_end}
    return cell_links

# Splits the rows in different columns at the splitting points #
def cleaning(text):
    #cell_points = end_points
    string = str(text)

    # Company Name
    comnam = (string[0:62])
    comnam = comnam.strip()

    # Forms
    form = (string[62:74])
    form = form.strip()

    # CIK
    cik = (string[74:86])
    cik = cik.strip()

    # Filing Date
    fdate = (string[86:98])
    fdate = fdate.strip()

    # Filing Name
    fname = (string[98:])
    fname = fname.strip()

    # Filing Index
    iname = fname.replace('.txt','-index.htm')

    # Accession Number
    accession = fname.replace('.txt','')
    accession = accession.replace('edgar/data/','')
    accession = accession[accession.find("/")+1:]
    
    filingdata = {'comnam': [comnam], 'form': [form], 'cik': [cik], 
                  'fdate': [fdate], 'fname': [fname], 'iname': [iname], 
                  'accession': [accession]}
    
    if form == "SC 13D":
        df_filingdata = pd.DataFrame(data=filingdata)
        return df_filingdata
    else:
        return None
    

# ******************************************************************************************** #
# Definition of Variables                                                                      #
# ******************************************************************************************** #
downloadfolder = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D"
exportfolder = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D"
path_to_csv_file = exportfolder + "SC 13D" + ".csv"
path_to_stata = exportfolder + "SC 13D.dta"

filings = pd.DataFrame(columns=['accession','cik','comnam','fdate','fname','form','iname'])

# ******************************************************************************************** #
# Loop over quarterly SEC Files                                                                #
# ******************************************************************************************** #
for i in range(1993,2019):
    year1_ = i
    for j in range(1,5):
        download(year1_,j)
        unzip(year1_,j)
        textfile(year1_,j)
        removehead(year1_,j)
        
        path_to_txt_file = exportfolder + "\\"+str(year1_) + "QTR" + str(j) + ".txt"
        path_to_zip_file = downloadfolder + "\\"+ str(year1_) + "QTR" + str(j) + ".zip"
        with open(path_to_txt_file, "r") as f:
            text = f.readlines()[1:]
            for row in text:
                cleaned = (cleaning(row))
                if cleaned is not None:
                    filings = filings.append(cleaned, ignore_index=True)
        
        os.remove(path_to_txt_file)
        os.remove(path_to_zip_file)

# Cleaning Filings #
filings['cik'] = pd.to_numeric(filings['cik'])        
filings['fdate'] = pd.to_datetime(filings['fdate'])
filings['iname'] = 'https://www.sec.gov/Archives/' + filings['iname'].astype(str)
filings['fname'] = 'https://www.sec.gov/Archives/' + filings['fname'].astype(str)


# Sample
filings.to_excel(downloadfolder + "\\" + "SC13DFilings.xlsx")
filings.to_pickle(downloadfolder + "\\" + "SC13DFilings.pickle")

print("Finish")