'''Helper module to parse complete CWE XML data into CWE entries according to ID

Original Data: CWE complete list (v2.11) from CWE website (https://cwe.mitre.org/)
Destination: List of XML files in folder, each containing one CWE, so that we can search and parse them easier later

'''

from lxml import etree

NAMESPACE = {'capec':'http://capec.mitre.org/capec-2'}

def parseCWEAll():

    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('CWE-complete-2.11.xml', parser=parser)
    root = tree.getroot()
    weakness_list = root.find('Weaknesses').findall('Weakness')
    for i in range(len(weakness_list)):
        # content = etree.tostring(weakness_list[0], pretty_print=True)
        ID = weakness_list[i].get('ID')
        etree.ElementTree(weakness_list[i]).write('cweXML/'+ID+'.xml', pretty_print=True, encoding="utf-8")

if __name__ == '__main__':
    parseCWEAll()
