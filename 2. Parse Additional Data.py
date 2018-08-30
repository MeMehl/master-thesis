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
class filing_information:

    def __init__(self, url):
        self.fileurl = url
        self.cik = url.split("/")[6]
        self.rawsitetext = self.parse_site(self.fileurl)
        self.filer_type = self.parse_filer_type(self.rawsitetext, self.cik)
        self.ftime = self.parsetime(self.rawsitetext)
        self.link = self.parse_link(self.rawsitetext)
        self.information = str(self.ftime) + ";" + str(self.filer_type) + ";" + str(self.link)
        
    def parse_site(self, url):
        readwebsite = ur.urlopen(url).read()
        website = bs(readwebsite, "html.parser")
        return website

    def parsetime(self, urltext):
        leadinfo = urltext.find_all("div", class_="info")
        leadinfo = list(leadinfo)
        return leadinfo[1].get_text()

    def parse_filer_type(self, urltext, cik_):
        info = urltext.find_all("div", class_="companyInfo")
        info = [row for row in info if cik_ in str(row)]
        
        if "(Subject)" in str(info):
            filer_type = 'Subject'
        elif "(Filed by)" in str(info):
            filer_type = 'Filed by'
        else:
            filer_type = 'Not identified'
            
        return filer_type

    def parse_link(self, urltext):
        linkinfo = urltext.find("table", class_="tableFile").find_all('a')
        link = linkinfo[0].get('href')
        return link
    
class filing_information_common:
    
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.subject_stateinfo = self.parse_state_subject(self.cleanfile)
        self.industry = self.parse_industry(self.cleanfile)
        self.filer_stateinfo = self.parse_state_filer(self.cleanfile)
        self.purpose = self.parse_purpose(self.cleanfile)
        self.cusip = self.parse_cusip(self.cleanfile)
        self.information2 = str(self.subject_stateinfo)+';'+str(self.industry)+';'+str(self.filer_stateinfo)+';'+str(self.purpose)+';'+str(self.cusip)
        
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
        
    def parse_state_subject(self, text):
        p = text.partition('STATE OF INCORPORATION:')
        part = p[2]
        p2 = part.partition('FISCAL YEAR END:')
        part2 = p2[0]
        p3 = part2.partition('FILING VALUES')
        subject_stateinfo = (p3[0])
        subject_stateinfo = subject_stateinfo.strip()
        alt_p = text.partition('STATE:')
        alt_part = alt_p[2]
        alt_p1 = alt_part.partition('ZIP:')
        state = alt_p1[0]
        business_state = state.strip()
        if subject_stateinfo == "":
            return business_state
        else:
            return subject_stateinfo
    
    def parse_industry(self, text):
        p = text.partition('STANDARD INDUSTRIAL CLASSIFICATION:')
        part = p[2]
        p2 = part.partition('IRS NUMBER:')
        industry = (p2[0])
        industry = industry.strip()
        if industry == "":
            return "N/A"
        else:
            return industry
    
    def parse_state_filer(self, text):
        p1 = text.partition('STATE:')
        part1 = p1[2]
        p2 = part1.partition('STATE:')
        part2 = p2[2]
        p3 = part2.partition('STATE:')
        part3 = p3[2]
        p4 = part3.partition('BUSINESS')
        part4 = p4[0]
        p5 = part4.partition('SC 13')
        part5 = p5[0]
        p6 = part5.partition('ZIP:')
        part6 = p6[0]
        filer_stateinfo = part6.strip()
        if filer_stateinfo == "":
            return "N/A"
        else:
            return filer_stateinfo
        
    def parse_purpose(self, text):
        text = text.replace("PURPOSE OF THE TRANSACTION","PURPOSE OF TRANSACTION")
        p1 = text.partition('PURPOSE OF TRANSACTION')
        part1 = p1[2]
        p2 = part1.partition('ITEM 5')
        purpose = p2[0]
        purpose = purpose.replace(";",",")
        purpose = purpose.replace(".","")
        purpose = purpose.strip()
        if purpose == "":
            return "N/A"
        else:
            return purpose
        
    def parse_cusip(self, text):
        p = text.replace("&nbsp;"," ")
        p = p.partition("FILING T")
        p = p[2]
        p = p.partition('CUSIP NO.')
        part = p[2]
        part = part.partition("(")
        part2 = part[0]
        part2 = part2.partition('PAGE')
        part3 = part2[0]
        p2 = part3.partition('1.')
        part3 = (p2[0])
        p3 = part3.partition('13D')
        part4 = (p3[0])
        p3 = part4.partition('-')
        part4 = (p3[0])
        p4 = part4.partition('NAME')
        part4 = (p4[0])
        p4 = part4.partition('THE')
        part4 = (p4[0])
        p4 = part4.partition('SCHEDULE')
        cusip = (p4[0])
        cusip = cusip.replace(":","")
        cusip = cusip.replace("CUSIP NO.",";")
        cusip = cusip.replace("NOT APPLICABLE","N/A")
        cusip = cusip.replace("NONE","N/A")
        cusip = cusip.replace(" 1 ","")
        cusip = cusip.replace("1)","")
        cusip = cusip.replace(" ","")
        cusip = cusip.replace("-","")
        cusip = cusip.replace("13D","")
        cusip = cusip.strip()
        if cusip == "":
            p = text.replace(" ","")
            p = p.partition("(TITLEOFCLASSOFSECURITIES)")
            part = p[2]
            p2 = part.partition("(CUSIPNUMBER)")
            p2 = p2[0]
            p2 = p2.partition("-")
            p2 = p2[0]
            p2 = p2.partition("_")
            p2 = p2[0]
            p2 = p2.partition("13D")
            p2 = p2[0]
            p2 = p2.partition("(")
            p2 = p2[0]
            p2 = p2.partition(")")
            p2 = p2[0]
            part2 = p2.replace("NOTAPPLICABLE","N/A")
            part2 = part2.replace("APPLIEDFOR","N/A")
            part2 = part2.replace("NONE","N/A")
            part2 = part2.replace(" 1 ","")
            part2 = part2.replace(" ","")
            part2 = part2.replace("1)","")
            part2 = part2.replace("-","")
            part2 = part2.replace("13D","")
            part2 = part2.strip()
            return part2
        else: 
            return cusip
        

   # ******************************************************************************************** #
# Variables and Paths                                                                          #
# ******************************************************************************************** #
path_to_files = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D\\SC13DFilings.pickle"
path_to_files2 = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D\\SC13DFilings_2.pickle"
downloadfolder = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D"


# ******************************************************************************************** #
# Code                                                                                         #
# ******************************************************************************************** #
files13d = pd.read_pickle(path_to_files)

# Only Accessions with Filer and Subject #
files13d['d'] = files13d.duplicated(subset='accession', keep=False)
files13d = files13d[files13d['d']==True]

files13d['info'] = files13d['iname'].map(lambda x: filing_information(x).information)
files13d['ftime'], files13d['type'], files13d['link'] = files13d['info'].str.split(';', 2).str

files13d['common_info'] = files13d['fname'].map(lambda x: filing_information_common(x).information2)
files13d['subject_state'], files13d['industry'], files13d['filer_state'], files13d['purpose'], files13d['cusip'] = files13d['common_info'].str.split(';', 4).str

del files13d['info'], files13d['d'], files13d['common_info']

files13d.to_pickle(path_to_files2)
files13d.to_excel(downloadfolder + "\\" + "SC13DFilings_2.xlsx")

print("Finish")
