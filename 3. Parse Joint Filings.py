# ******************************************************************************************** #
# This program parses the time when a particular SC 13D filing was published and publicly      #
# available to download from SEC Edgar.                                                        #
# ******************************************************************************************** #


# ******************************************************************************************** #
# Packages                                                                                     #
# ******************************************************************************************** #
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import pandas as pd

# ******************************************************************************************** #
# Functions                                                                                    #
# ******************************************************************************************** #
       
class filing_information_filer1:
    
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer1_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer1_info)
        self.share = self.parse_share(self.filer1_info)
        self.voting = self.parse_voting_power(self.filer1_info)
        self.information3 = str(self.name)+';'+str(self.share)+';'+str(self.voting)
        
    def clean_text(self, url):
        data = ur.urlopen(url) 
        webContent = data.read()
        body = webContent.decode('utf-8')
        cleantext = bs(body, "lxml").text
        cleantext = cleantext.upper()
        cleantext = cleantext.replace("\n","")
        cleantext = cleantext.replace("\xa0"," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        return cleantext
    
    def separate_filer_info(self, text):
        p1 = text.replace(" ","")
        p1 = p1.replace('NAMES','NAME')
        p1 = p1.replace('NAME(S)','NAME')
        p1 = p1.replace('PERSONS','PERSON')
        p1 = p1.replace('IDENTIFICATIONNO.OFREPORTINGPERSON','IDENTIFICATIONNO.')
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[0]
        return part2
    
    def parse_name(self, text):
        p1 = text.replace('(ENTITIESONLY)','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNOS.OFABOVEPERSONS','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNOS.OFABOVEPERSON','')
        p1 = p1.partition('CHECKTHE')
        part1 = p1[0]
        p1 = part1.partition('(')
        part1 = p1[0]
        p1 = part1.partition('I.R.S.')
        part1 = p1[0]
        p1 = part1.partition(',SOLEOWNEROF')
        part1 = p1[0]
        p2 = part1.partition('2')
        part2 = p2[0]
        p2 = part2.partition('THEREPORTINGPERSON')
        part2 = p2[0]
        part2 = part2.strip()
        part2 = part2.replace("S.S.OR","")
        part2 = part2.replace("S.SOR","")
        part2 = part2.replace(".","")
        part2 = part2.replace(":","")
        return part2
    
    def parse_share(self, text):
        p1 = text.replace("PERCENTOFCLASSREPRESENTEDBYROW11","PERCENTOFCLASSREPRESENTEDBYAMOUNTINROW(11)")
        p1 = p1.replace("ROW11","ROW(11)")
        p1 = p1.partition('PERCENTOFCLASSREPRESENTEDBYAMOUNTINROW(11)')
        part1 = p1[2]
        p2 = part1.partition("(")
        part2 = p2[0]
        p2 = part2.partition("TYPEOFREPORTINGPERSON")
        part2 = p2[0]
        p2 = part2.partition("OF")
        part2 = p2[0]
        p2 = part2.partition("-")
        part2 = p2[0]
        p2 = part2.partition("CLASS")
        part2 = p2[0]
        part2 = part2.replace(":","")
        part2 = part2.replace("#","")
        part2 = part2.replace("COMMONSTOCK","")
        part2 = part2.replace("*","")
        part2 = part2.replace("%114","%")
        part2 = part2.replace("%214","%")
        part2 = part2.replace("%.","%")
        part2 = part2.replace("%14","%")
        part2 = part2.replace("%14","%")
        part2 = part2.replace("014","")
        part2 = part2.replace("EXCLUDESCERTAINSHARES","")
        part2 = part2.replace("APPROXIMATELY","")
        return part2
    
    def parse_voting_power(self, text):
        part = text.partition("SOLEVOTINGPOWER")
        p1 = part[2]
        part1 = p1.partition("SHAREDVOTINGPOWER")
        p2 = part1[0]
        p2 = p2.replace("0","")
        p2 = p2.replace("8","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("SHARESOFCOMMONSTOCK","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("SHARESOFCOMMONSTOCK","")
        if p2 == "":
            return "SHARED"
        elif p4 =="":
            return "SOLE"
        else:
            return "COMBINATION"
        
    
    
class filing_information_filer2:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.information4 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
    def clean_text(self, url):
        data = ur.urlopen(url) 
        webContent = data.read()
        body = webContent.decode('utf-8')
        cleantext = bs(body, "lxml").text
        cleantext = cleantext.upper()
        cleantext = cleantext.replace("\n","")
        cleantext = cleantext.replace("\xa0"," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        cleantext = cleantext.replace("  "," ")
        return cleantext
    
    def separate_filer_info(self, text):
        p1 = text.replace(" ","")
        p1 = p1.replace('NAMES','NAME')
        p1 = p1.replace('NAME(S)','NAME')
        p1 = p1.replace('PERSONS','PERSON')
        p1 = p1.replace('IDENTIFICATIONNO.OFREPORTINGPERSON','IDENTIFICATIONNO.')
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[0]
        return part2  
    
    def parse_name(self, text):
        p1 = text.replace('(ENTITIESONLY)','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNOS.OFABOVEPERSONS','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNOS.OFABOVEPERSON','')
        p1 = p1.partition('CHECKTHE')
        part1 = p1[0]
        p1 = part1.partition('(')
        part1 = p1[0]
        p1 = part1.partition('I.R.S.')
        part1 = p1[0]
        p1 = part1.partition(',SOLEOWNEROF')
        part1 = p1[0]
        p2 = part1.partition('2')
        part2 = p2[0]
        p2 = part2.partition('THEREPORTINGPERSON')
        part2 = p2[0]
        part2 = part2.strip()
        part2 = part2.replace("S.S.OR","")
        part2 = part2.replace("S.SOR","")
        part2 = part2.replace(".","")
        part2 = part2.replace(":","")
        return part2
    
    def parse_share(self, text):
        p1 = text.replace("PERCENTOFCLASSREPRESENTEDBYROW11","PERCENTOFCLASSREPRESENTEDBYAMOUNTINROW(11)")
        p1 = p1.replace("ROW11","ROW(11)")
        p1 = p1.partition('PERCENTOFCLASSREPRESENTEDBYAMOUNTINROW(11)')
        part1 = p1[2]
        p2 = part1.partition("(")
        part2 = p2[0]
        p2 = part2.partition("TYPEOFREPORTINGPERSON")
        part2 = p2[0]
        p2 = part2.partition("OF")
        part2 = p2[0]
        p2 = part2.partition("-")
        part2 = p2[0]
        p2 = part2.partition("CLASS")
        part2 = p2[0]
        part2 = part2.replace(":","")
        part2 = part2.replace("#","")
        part2 = part2.replace("COMMONSTOCK","")
        part2 = part2.replace("*","")
        part2 = part2.replace("%114","%")
        part2 = part2.replace("%214","%")
        part2 = part2.replace("%.","%")
        part2 = part2.replace("%14","%")
        part2 = part2.replace("%14","%")
        part2 = part2.replace("014","")
        part2 = part2.replace("EXCLUDESCERTAINSHARES","")
        part2 = part2.replace("APPROXIMATELY","")
        return part2

    def parse_voting_power(self, text):
        part = text.partition("SOLEVOTINGPOWER")
        p1 = part[2]
        part1 = p1.partition("SHAREDVOTINGPOWER")
        p2 = part1[0]
        p2 = p2.replace("0","")
        p2 = p2.replace("8","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("-","")
        p2 = p2.replace("OFCOMMONSTOCK","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("OFCOMMONSTOCK","")
        if p2 == "":
            return "SHARED"
        elif p4 =="":
            return "SOLE"
        else:
            return "COMBINATION"
    
    def filer_2(self,text):
        if text == "":
            return "NO"
        else: 
            return "YES"
        
   # ******************************************************************************************** #
# Variables and Paths                                                                          #
# ******************************************************************************************** #
path_to_files2 = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D\\SC13DFilings_2.pickle"
path_to_files3 = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D\\SC13DFilings_3.pickle"
downloadfolder = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D"


# ******************************************************************************************** #
# Code                                                                                         #
# ******************************************************************************************** #
files13d = pd.read_pickle(path_to_files2)

files13d['filer1_info'] = files13d['fname'].map(lambda x: filing_information_filer1(x).information3)
files13d['name'], files13d['share'], files13d['voting_power'] = files13d['filer1_info'].str.split(';', 2).str

files13d['filer2_info'] = files13d['fname'].map(lambda x: filing_information_filer2(x).information4)
files13d['name_2'], files13d['share_2'], files13d['voting_power_2'], files13d['filer_2'] = files13d['filer2_info'].str.split(';', 3).str

del files13d['filer1_info'], files13d['filer2_info']

files13d.to_pickle(path_to_files3)
files13d.to_excel(downloadfolder + "\\" + "SC13DFilings_3.xlsx")
