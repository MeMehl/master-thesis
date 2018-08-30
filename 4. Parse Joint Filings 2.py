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
        self.fundsinfo = self.parse_funds(self.filer1_info)
        self.investor_type = self.parse_investortype(self.filer1_info)
        self.information3 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part3 = p3[0]
        p5 = part3.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        if fundsinfo == "":
            return "N/A"
        else:
            return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
    
class filing_information_filer2:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer2_info)
        self.investor_type = self.parse_investortype(self.filer2_info)
        self.information4 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
        
class filing_information_filer3:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer3_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer3_info)
        self.investor_type = self.parse_investortype(self.filer3_info)
        self.information5 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        part2 = p2[2]
        p3 = part2.partition('NAMEOFREPORTINGPERSON')
        part3 = p3[2]
        p4 = part3.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type

class filing_information_filer4:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer4_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer4_info)
        self.investor_type = self.parse_investortype(self.filer4_info)
        self.information6 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer5:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer5_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer5_info)
        self.investor_type = self.parse_investortype(self.filer5_info)
        self.information7 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer6:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer6_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer6_info)
        self.investor_type = self.parse_investortype(self.filer6_info)
        self.information8 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer7:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer7_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer7_info)
        self.investor_type = self.parse_investortype(self.filer7_info)
        self.information9 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer8:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information10 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer9:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information11 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer10:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information12 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer11:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information13 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer12:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information14 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
 
class filing_information_filer13:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information15 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
class filing_information_filer14:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information16 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
    
    
class filing_information_filer15:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer8_info = self.separate_filer_info(self.cleanfile)
        self.fundsinfo = self.parse_funds(self.filer8_info)
        self.investor_type = self.parse_investortype(self.filer8_info)
        self.information17 = str(self.fundsinfo)+';'+str(self.investor_type)
        
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
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p1 = part1.partition('NAMEOFREPORTINGPERSON')
        part1 = p1[2]
        p2 = part1.partition('NAMEOFREPORTINGPERSON')
        part2 = p2[2]
        p4 = part2.partition('NAMEOFREPORTINGPERSON')
        part4 = p4[0]
        return part4
        
    def parse_funds(self, text):
        p = text.partition('OFFUNDS')
        part = p[2]
        p = part.partition('6')
        part = p[0]
        p = part.partition('1')
        part = p[0]
        p = part.partition('(SEEITEM')
        part = p[0]
        p2 = part.partition('CHECK')
        part2 = p2[0]
        p2 = part.partition('-')
        part2 = p2[0]
        p3 = part2.partition('5')
        part3 = p3[0]
        p3 = part3.partition('FUNDS')
        part3 = p3[0]
        p3 = part3.partition('OF')
        part3 = p3[0]
        p3 = part3.partition('FOR')
        part4 = p3[0]
        p5 = part4.partition('.')
        fundsinfo = (p5[0])
        fundsinfo = fundsinfo.replace('SEE','')
        fundsinfo = fundsinfo.replace('INSTRUCTIONS','')
        fundsinfo = fundsinfo.replace('INSTRUCTION','')
        fundsinfo = fundsinfo.replace('ITEM3','')
        fundsinfo = fundsinfo.replace("*",'')
        fundsinfo = fundsinfo.replace("AND",',')
        fundsinfo = fundsinfo.replace("&",',')
        fundsinfo = fundsinfo.replace(':','')
        fundsinfo = fundsinfo.replace("(",'')
        fundsinfo = fundsinfo.replace("PERSONAL",'PF')
        fundsinfo = fundsinfo.replace("CASHRESERVE",'CASH RESERVE')
        fundsinfo = fundsinfo.replace("/",',')
        fundsinfo = fundsinfo.replace(";",',')
        fundsinfo = fundsinfo.replace(")",'')
        fundsinfo = fundsinfo.replace("00",'OO')
        fundsinfo = fundsinfo.replace("NOTAPPLICABLE",'N/A')
        fundsinfo = fundsinfo.replace("N,A",'N/A')
        fundsinfo = fundsinfo.replace(".",'')
        fundsinfo = fundsinfo.replace("OOOTHER",'OO,OTHER')
        fundsinfo = fundsinfo.strip()
        return fundsinfo
        
    def parse_investortype(self, text):
        text = text.replace(" ", "")
        p = text.partition('TYPEOFREPORTINGPERSON')
        part = p[2]
        part = part.replace('SEEINSTRUCTIONS','')
        p2 = part.partition("(A)")
        part = (p2[0])
        p2 = part.partition("ITEM")
        part = (p2[0])
        p2 = part.partition("1")
        part = (p2[0])
        p2 = part.partition("2")
        part = (p2[0])
        p2 = part.partition("CUSIP")
        part = (p2[0])
        p2 = part.partition("CONSIST")
        part2 = (p2[0])
        p2 = part2.partition("REPRESENT")
        part2 = (p2[0])
        p2 = part2.partition("THIS")
        part2 = (p2[0])
        p2 = part2.partition("3")
        part2 = (p2[0])
        p2 = part2.partition("_")
        part2 = (p2[0])
        p2 = part2.partition("6")
        part2 = (p2[0])
        p2 = part2.partition("5")
        part2 = (p2[0])
        p2 = part2.partition("ORIGINAL")
        part2 = (p2[0])
        p2 = part2.partition("=")
        part2 = (p2[0])
        p2 = part2.partition("BENEFICIAL")
        part2 = (p2[0])
        p2 = part2.partition("INADDITION")
        part2 = (p2[0])
        p2 = part2.partition("DOES")
        part2 = (p2[0])
        p2 = part2.partition("SCHEDULE")
        part2 = p2[0]
        p2 = part2.partition("BASED")
        part2 = p2[0]
        p2 = part2.partition("AS")
        part2 = (p2[0])
        p3 = part2.partition("–")
        part3 = p3[0]
        p3 = part3.partition("INCLUDES")
        part3 = p3[0]
        p3 = part3.partition("PAGE")
        part3 = p3[0]
        p3 = part3.partition("GENERAL")
        part3 = p3[0]
        p3 = part3.partition("REFLECTS")
        part3 = p3[0]
        p3 = part3.partition("FOOTNOTES")
        part3 = p3[0]
        p3 = part3.partition("PERCENTAGE")
        part3 = p3[0]
        p3 = part3.partition("BEFORE")
        part3 = p3[0]
        p3 = part3.partition("EXPLANATORY")
        part3 = p3[0]
        p3 = part3.partition("THE")
        part3 = p3[0]
        p3 = part3.partition("INTRO")
        part3 = p3[0]
        p3 = part3.partition("AMOUNT")
        part3 = p3[0]
        p4 = part3.partition("-")
        investor_type = p4[0]
        investor_type = investor_type.replace("*",'')
        investor_type = investor_type.replace("SEE",'')
        investor_type = investor_type.replace("INSTRUCTIONS",'')
        investor_type = investor_type.replace("INDIVIDUAL",'IN')
        investor_type = investor_type.replace("LIMITEDLIABILITYCOMPANY",',CO')
        investor_type = investor_type.replace("AND",',')
        investor_type = investor_type.replace("&",',')
        investor_type = investor_type.replace(':','')
        investor_type = investor_type.replace('00','OO')
        investor_type = investor_type.replace('INB','IN')
        investor_type = investor_type.replace("(",'')
        investor_type = investor_type.replace(")",'')
        investor_type = investor_type.replace(";",',')
        investor_type = investor_type.strip()
        return investor_type
   # ******************************************************************************************** #
# Variables and Paths                                                                          #
# ******************************************************************************************** #
path_to_files3 = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D\\SC13DFilings_3.pickle"
path_to_files4 = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D\\SC13DFilings_4.pickle"
downloadfolder = "C:\\Users\\mehl-\\Documents\\Master Thesis\\13D"


# ******************************************************************************************** #
# Code                                                                                         #
# ******************************************************************************************** #
files13d = pd.read_pickle(path_to_files3)

files13d['filer1_info'] = files13d['fname'].map(lambda x: filing_information_filer1(x).information3)
files13d['funds_1'], files13d['investor_type_1'] = files13d['filer1_info'].str.split(';', 1).str

files13d_2 = files13d[files13d['name'] != '']

files13d['filer2_info'] = files13d_2['fname'].map(lambda x: filing_information_filer2(x).information4)
files13d['funds_2'], files13d['investor_type_2'] = files13d['filer2_info'].str.split(';', 1).str

files13d_3 = files13d[files13d['name_2'] != '']

files13d['filer3_info'] = files13d_3['fname'].map(lambda x: filing_information_filer3(x).information5)
files13d['funds_3'], files13d['investor_type_3'] = files13d['filer3_info'].str.split(';', 1).str

files13d_4 = files13d[files13d['name_3'] != '']

files13d['filer4_info'] = files13d_4['fname'].map(lambda x: filing_information_filer4(x).information6)
files13d['funds_4'], files13d['investor_type_4'] = files13d['filer4_info'].str.split(';', 1).str

files13d_5 = files13d[files13d['name_4'] != '']

files13d['filer5_info'] = files13d_5['fname'].map(lambda x: filing_information_filer5(x).information7)
files13d['funds_5'], files13d['investor_type_5'] = files13d['filer5_info'].str.split(';', 1).str

files13d_6 = files13d[files13d['name_5'] != '']

files13d['filer6_info'] = files13d_6['fname'].map(lambda x: filing_information_filer6(x).information8)
files13d['funds_6'], files13d['investor_type_6'] = files13d['filer6_info'].str.split(';', 1).str

files13d_7 = files13d[files13d['name_6'] != '']

files13d['filer7_info'] = files13d_7['fname'].map(lambda x: filing_information_filer7(x).information9)
files13d['funds_7'], files13d['investor_type_7'] = files13d['filer7_info'].str.split(';', 1).str

files13d_8 = files13d[files13d['name_7'] != '']

files13d['filer8_info'] = files13d_8['fname'].map(lambda x: filing_information_filer8(x).information10)
files13d['funds_8'], files13d['investor_type_8'] = files13d['filer8_info'].str.split(';', 1).str

files13d_9 = files13d[files13d['name_8'] != '']

files13d['filer9_info'] = files13d_9['fname'].map(lambda x: filing_information_filer9(x).information11)
files13d['funds_9'], files13d['investor_type_9'] = files13d['filer9_info'].str.split(';', 1).str

files13d_10 = files13d[files13d['name_9'] != '']

files13d['filer10_info'] = files13d_10['fname'].map(lambda x: filing_information_filer10(x).information12)
files13d['funds_10'], files13d['investor_type_10'] = files13d['filer10_info'].str.split(';', 1).str

files13d_11 = files13d[files13d['name_10'] != '']

files13d['filer11_info'] = files13d_11['fname'].map(lambda x: filing_information_filer11(x).information13)
files13d['funds_11'], files13d['investor_type_11'] = files13d['filer11_info'].str.split(';', 1).str

files13d_12 = files13d[files13d['name_11'] != '']

files13d['filer12_info'] = files13d_12['fname'].map(lambda x: filing_information_filer12(x).information14)
files13d['funds_12'], files13d['investor_type_12'] = files13d['filer12_info'].str.split(';', 1).str

files13d_13 = files13d[files13d['name_12'] != '']

files13d['filer13_info'] = files13d_13['fname'].map(lambda x: filing_information_filer13(x).information15)
files13d['funds_13'], files13d['investor_type_13'] = files13d['filer13_info'].str.split(';', 1).str

files13d_14 = files13d[files13d['name_13'] != '']

files13d['filer14_info'] = files13d_14['fname'].map(lambda x: filing_information_filer14(x).information16)
files13d['funds_14'], files13d['investor_type_14'] = files13d['filer14_info'].str.split(';', 1).str

files13d_15 = files13d[files13d['name_14'] != '']

files13d['filer15_info'] = files13d_15['fname'].map(lambda x: filing_information_filer15(x).information17)
files13d['funds_15'], files13d['investor_type_15'] = files13d['filer15_info'].str.split(';', 1).str

del files13d['filer1_info'], files13d['filer2_info'], files13d['filer3_info'], files13d['filer4_info'], files13d['filer5_info'], files13d['filer6_info'], files13d['filer7_info']
del files13d['filer8_info'], files13d['filer9_info'], files13d['filer10_info'], files13d['filer11_info'], files13d['filer12_info'], files13d['filer13_info'], files13d['filer14_info']
del files13d['filer15_info']
files13d.to_pickle(path_to_files4)
files13d.to_excel(downloadfolder + "\\" + "SC13DFilings_4.xlsx")

