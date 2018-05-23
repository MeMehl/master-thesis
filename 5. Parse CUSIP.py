# ******************************************************************************************** #
# This program parses the time when a particular SC 13D filing was published and publicly      #
# available to download from SEC Edgar.                                                        #
# ******************************************************************************************** #


# ******************************************************************************************** #
# Packages                                                                                     #
# ******************************************************************************************** #
import urllib.request as ur
import csv
from bs4 import BeautifulSoup as bs
import time
import random
import pandas as pd
import re
import datetime as dt

# ******************************************************************************************** #
# Functions                                                                                    #
# ******************************************************************************************** #
def parsecusip(url, cusiplist):

    splitword1 = '(NAMEOFISSUER)'
    splitword2 = '(DATEOFEVENTWHICHREQUIRESFILINGOFTHISSTATEMENT)'

    try:
        site13d = ur.urlopen(url).read()
        website13d = bs(site13d, "html.parser")
        content = website13d.get_text()
        content = re.sub(" ", "", content)
        content = re.sub(r'\n', "", content)
        content = re.sub(r'\s', "", content)
        content = re.split(splitword2, content, flags=re.IGNORECASE)
        content = re.split(splitword1, content[0], flags=re.IGNORECASE)
        content = re.sub(r'[\W_]+', "", content[2])

        cusip = re.compile('|'.join(cusiplist),re.IGNORECASE).search(content)
        if cusip is not None:
            return cusip[0]
        else:
            return "Not found in CRSP"
        
    except ur.HTTPError:
        return 'HTTPError'
    except:
        return 'n/a'

def cleaning(df_):
    df_ = df_[df_['type']=='Subject']
    df_['link'] = files13d['link'].map(lambda x: 'https://www.sec.gov' + str(x))
    df_ = df_.reset_index(drop=True)
    return df_

def list_cusip(df):
    df = df[df['nameendt'] >= dt.datetime(2004,1,1)]
    ncusip = df['ncusip'].tolist()
    cusip = set(ncusip)
    return cusip

# ******************************************************************************************** #
# Variables and Paths                                                                          #
# ******************************************************************************************** #
inputfolder = "C:/Users/NicolasKube/Documents/Research/SC13D/Analysis/Input/"
path_to_files = inputfolder + "SC13DFilingsInfo.pickle"
path_crspnames = inputfolder + "CRSPNames.dta"
path_to_files2 = inputfolder + "Reports_complete.pickle"

# ******************************************************************************************** #
# Code                                                                                         #
# ******************************************************************************************** #
names = pd.read_stata(path_crspnames)
cusip = list_cusip(names)


files13d = pd.read_pickle(path_to_files)
files13d = cleaning(files13d)
files13d['cusip'] = files13d['link'].map(lambda x: parsecusip(x,cusip))      
files13d.to_pickle(path_to_files2)
