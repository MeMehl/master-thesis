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
        p1 = p1.replace('[ENTITIESONLY]','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNOS.OFABOVEPERSONS','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNOS.OFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
        p1 = p1.partition('CHECKTHE')
        part1 = p1[0]
        p1 = part1.partition('(')
        part1 = p1[0]
        p1 = part1.partition('I.R.S.')
        part1 = p1[0]
        p1 = part1.partition('-')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
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
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer3:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information5 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer4:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information6 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer5:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information7 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer6:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information8 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer7:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information9 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer8:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information10 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer9:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information11 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer10:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information12 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer11:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information13 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer12:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information14 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer13:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information15 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer14:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information16 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
        
class filing_information_filer15:
    
        
    def __init__(self, url):
        self.filingurl=url
        self.cleanfile=self.clean_text(self.filingurl)
        self.filer2_info = self.separate_filer_info(self.cleanfile)
        self.name = self.parse_name(self.filer2_info)
        self.share = self.parse_share(self.filer2_info)
        self.filer2 = self.filer_2(self.filer2_info)
        self.voting = self.parse_voting_power(self.filer2_info)      
        self.information17 = str(self.name)+';'+str(self.share)+';'+str(self.voting)+';'+str(self.filer2)
        
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
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
        p1 = p1.partition('NAMEOFREPORTINGPERSON')
        p1 = p1[2]
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
        p1 = p1.replace('I.R.S.IDENTIFICATIONOFABOVEPERSON','')
        p1 = p1.replace('I.R.S.IDENTIFICATIONNO.OFABOVEPERSON','')
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
        part2 = part2.replace(".S.OR","")
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
        p2 = p2.replace("(","")
        p2 = p2.replace(")","")
        p2 = p2.replace(".","")
        p2 = p2.replace(":","")
        p2 = p2.replace("-","")
        p2 = p2.replace("COMMONSTOCK","")
        p2 = p2.replace("BENEFICIALLY","")
        p2 = p2.replace("OWNED","")
        p2 = p2.replace("SHARES","")
        p2 = p2.replace("OF","")
        p2 = p2.replace("NUMBER","")
        p2 = p2.replace("BY","")
        p2 = p2.replace("EACH","")
        p2 = p2.replace("REPORTING","")
        p2 = p2.replace("PERSON","")
        p2 = p2.replace("WITH","")
        p2 = p2.replace("NONE","")
        p3 = part1[2]
        part2 = p3.partition("SOLEDISPOSITIVEPOWER")
        p4 = part2[0]
        p4 = p4.replace("0","")
        p4 = p4.replace("9","")
        p4 = p4.replace("(","")
        p4 = p4.replace(")","")
        p4 = p4.replace(".","")
        p4 = p4.replace(":","")
        p4 = p4.replace("-","") 
        p4 = p4.replace("COMMONSTOCK","")
        p4 = p4.replace("BENEFICIALLY","")
        p4 = p4.replace("OWNED","")
        p4 = p4.replace("SHARES","")
        p4 = p4.replace("OF","")
        p4 = p4.replace("NUMBER","")
        p4 = p4.replace("BY","")
        p4 = p4.replace("EACH","")
        p4 = p4.replace("REPORTING","")
        p4 = p4.replace("PERSON","")
        p4 = p4.replace("WITH","")
        p4 = p4.replace("NONE","")
        if self.filer2=="NO":
            return "N/A"
        elif p2 == "":
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
files13d['name_1'], files13d['share_1'], files13d['voting_power_1'] = files13d['filer1_info'].str.split(';', 2).str

files13d_2 = files13d[files13d['name'] != '']

files13d['filer2_info'] = files13d_2['fname'].map(lambda x: filing_information_filer2(x).information4)
files13d['name_2'], files13d['share_2'], files13d['voting_power_2'], files13d['filer_2'] = files13d['filer2_info'].str.split(';', 3).str

files13d_3 = files13d[files13d['name_2'] != '']

files13d['filer3_info'] = files13d_3['fname'].map(lambda x: filing_information_filer3(x).information5)
files13d['name_3'], files13d['share_3'], files13d['voting_power_3'], files13d['filer_3'] = files13d['filer3_info'].str.split(';', 3).str

files13d_4 = files13d[files13d['name_3'] != '']

files13d['filer4_info'] = files13d_4['fname'].map(lambda x: filing_information_filer4(x).information6)
files13d['name_4'], files13d['share_4'], files13d['voting_power_4'], files13d['filer_4'] = files13d['filer4_info'].str.split(';', 3).str

files13d_5 = files13d[files13d['name_4'] != '']

files13d['filer5_info'] = files13d_5['fname'].map(lambda x: filing_information_filer5(x).information7)
files13d['name_5'], files13d['share_5'], files13d['voting_power_5'], files13d['filer_5'] = files13d['filer5_info'].str.split(';', 3).str

files13d_6 = files13d[files13d['name_5'] != '']

files13d['filer6_info'] = files13d_6['fname'].map(lambda x: filing_information_filer6(x).information8)
files13d['name_6'], files13d['share_6'], files13d['voting_power_6'], files13d['filer_6'] = files13d['filer6_info'].str.split(';', 3).str

files13d_7 = files13d[files13d['name_6'] != '']

files13d['filer7_info'] = files13d_7['fname'].map(lambda x: filing_information_filer7(x).information9)
files13d['name_7'], files13d['share_7'], files13d['voting_power_7'], files13d['filer_7'] = files13d['filer7_info'].str.split(';', 3).str

files13d_8 = files13d[files13d['name_7'] != '']

files13d['filer8_info'] = files13d_8['fname'].map(lambda x: filing_information_filer8(x).information10)
files13d['name_8'], files13d['share_8'], files13d['voting_power_8'], files13d['filer_8'] = files13d['filer8_info'].str.split(';', 3).str

files13d_9 = files13d[files13d['name_8'] != '']

files13d['filer9_info'] = files13d_9['fname'].map(lambda x: filing_information_filer9(x).information11)
files13d['name_9'], files13d['share_9'], files13d['voting_power_9'], files13d['filer_9'] = files13d['filer9_info'].str.split(';', 3).str

files13d_10 = files13d[files13d['name_9'] != '']

files13d['filer10_info'] = files13d_10['fname'].map(lambda x: filing_information_filer10(x).information12)
files13d['name_10'], files13d['share_10'], files13d['voting_power_10'], files13d['filer_10'] = files13d['filer10_info'].str.split(';', 3).str

files13d_11 = files13d[files13d['name_10'] != '']

files13d['filer11_info'] = files13d_11['fname'].map(lambda x: filing_information_filer11(x).information13)
files13d['name_11'], files13d['share_11'], files13d['voting_power_11'], files13d['filer_11'] = files13d['filer11_info'].str.split(';', 3).str

files13d_12 = files13d[files13d['name_11'] != '']

files13d['filer12_info'] = files13d_12['fname'].map(lambda x: filing_information_filer12(x).information14)
files13d['name_12'], files13d['share_12'], files13d['voting_power_12'], files13d['filer_12'] = files13d['filer12_info'].str.split(';', 3).str

files13d_13 = files13d[files13d['name_12'] != '']

files13d['filer13_info'] = files13d_13['fname'].map(lambda x: filing_information_filer13(x).information15)
files13d['name_13'], files13d['share_13'], files13d['voting_power_13'], files13d['filer_13'] = files13d['filer13_info'].str.split(';', 3).str

files13d_14 = files13d[files13d['name_13'] != '']

files13d['filer14_info'] = files13d_14['fname'].map(lambda x: filing_information_filer14(x).information16)
files13d['name_14'], files13d['share_14'], files13d['voting_power_14'], files13d['filer_14'] = files13d['filer14_info'].str.split(';', 3).str

files13d_15 = files13d[files13d['name_14'] != '']

files13d['filer15_info'] = files13d_15['fname'].map(lambda x: filing_information_filer15(x).information17)
files13d['name_15'], files13d['share_15'], files13d['voting_power_15'], files13d['filer_15'] = files13d['filer15_info'].str.split(';', 3).str

del files13d['filer1_info'], files13d['filer2_info'], files13d['filer3_info'], files13d['filer4_info'], files13d['filer5_info']
del files13d['filer6_info'], files13d['filer7_info'], files13d['filer8_info'], files13d['filer9_info'], files13d['filer10_info']
del files13d['filer11_info'], files13d['filer12_info'], files13d['filer13_info'], files13d['filer14_info'], files13d['filer15_info']

files13d.to_pickle(path_to_files3)
files13d.to_excel(downloadfolder + "\\" + "SC13DFilings_3.xlsx")

print("Finish")
