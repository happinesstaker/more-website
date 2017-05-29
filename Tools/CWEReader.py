from lxml import etree
import re

def contentDictFromCWE(ID):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('cweXML/'+ID+'.xml', parser=parser)
    root = tree.getroot()

    resContent = dict()
    resContent['id'] = root.get("ID")
    resContent['name'] = root.get("Name")

    # save descriptions
    desc = root.find('Description')
    if desc:
        summary = desc.find('Description_Summary')
        if summary:
            resContent['summary'] = re.sub('\s+', ' ', summary.text)
        extended_summary = desc.find('Extended_Description')
        if extended_summary:
            resContent['exsummary'] = re.sub('\s+', ' ', extended_summary.text)

    # discard relationship, not useful

    introduceTime = root.find('Time_of_Introduction')
    if introduceTime:
        resContent['introducephase'] = list()
        for phase in introduceTime.getChildren():
            resContent['introducephase'].append(phase.text)

    # let's stop this work, better directly view the website
