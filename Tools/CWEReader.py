'''Module to parse XML of CWE and display them well-formatted

Data Source: Output of CWEParser.py
Destination: pretty output in terminal
Intermidiate format: json (so that we can optionally save those json files)

Note: those links are printed because I am using iTerm2 and can Command+Click to
      open this link in browser (easy!)

Challenge: the demonstrative example and detection methods are hard to parse and
           it turns out that html format is even better, so I paste the link here.

'''

import re
import sys
from lxml import etree

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def contentDictFromCWE(ID):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('cweXML/'+ID+'.xml', parser=parser)
    root = tree.getroot()

    resContent = dict()
    resContent['id'] = root.get("ID")
    resContent['name'] = root.get("Name")

    # save descriptions
    desc = root.find('Description')
    if desc is not None:
        summary = desc.find('Description_Summary')
        if summary is not None:
            resContent['summary'] = re.sub('\s+', ' ', summary.text)
        extended_summary = desc.find('Extended_Description')
        if extended_summary is not None:
            exsum = re.sub('<[^<]+>', ' ', etree.tostring(extended_summary))
            exsum = re.sub('\s+', " ", exsum)
            resContent['exsummary'] = exsum


    # discard relationship, not useful

    introduceTime = root.find('Time_of_Introduction')
    if introduceTime is not None:
        resContent['introducephase'] = list()
        for phase in introduceTime:
            resContent['introducephase'].append(phase.text)

    detection = root.find('Detection_Methods')
    mitigate = root.find('Potential_Mitigations')
    if mitigate is not None:
        resContent['link'] = "http://cwe.mitre.org/data/definitions/%s.html#Potential_Mitigations" % ID
    elif detection is not None:
        resContent['link'] = "http://cwe.mitre.org/data/definitions/%s.html#Detection_Methods" % ID
    else:
        resContent['link'] = "http://cwe.mitre.org/data/definitions/%s.html" % ID
    resContent['wikilink'] = "http://wiki.scap.org.cn/cwe/en/definition/" + ID
    return resContent

def displayCWE(DictCWE):

    # print CWE ID and name
    print
    print color.RED + DictCWE['id'] + color.END + ": " + color.BOLD + DictCWE['name'] + color.END

    # print CWE description
    print
    print color.RED + "Description:" + color.END
    print DictCWE['summary']
    if 'exsummary' in DictCWE:
        print color.PURPLE + DictCWE['exsummary'] + color.END

    # print introduction phases
    print
    if 'introducephase' in DictCWE:
        print color.RED + "Introduction Phase:" + color.END
        for phase in DictCWE['introducephase']:
            print "* " + phase

    # Link to original CWE
    print
    print color.RED + "Detection/Mitigation:" + color.END
    print color.UNDERLINE + DictCWE['link'] + color.END

    # Link to wiki
    print
    print color.RED + "Wiki:" + color.END
    print color.UNDERLINE + DictCWE['wikilink'] + color.END


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python CWEReader.py [CWE ID]"
        exit(0)
    CWE_JSON = contentDictFromCWE(str(sys.argv[1]))
    displayCWE(CWE_JSON)
