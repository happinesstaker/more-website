from cwe.models import Category
from cwe.models import Keyword
from cwe.models import CWE
from cwe.cwe_search import CWESearchLocator
from django.db import IntegrityError

from lxml import etree
import re
import traceback


NAMESPACE = {'capec':'http://capec.mitre.org/capec-2'}

def getNsTagged(tag):
    ns = 'http://www.w3.org/2001/XMLSchema-instance'
    return '{%s}%s' % (ns, tag)

def readXML():
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('scripts/CWE-list.xml', parser=parser)
    root = tree.getroot()
    weakness_list = root.find('Weaknesses').findall('Weakness')
    cwe_search = CWESearchLocator.get_instance()

    try:
        for weakness in weakness_list:

            ID = weakness.get('ID')
            Name = weakness.get('Name')

            keywordList = list()
            keywords = Name.split()
            for keyword in keywords:
                # since keyword is stemmed before save, we cannot simply use get_or_create
                stemmed_name = cwe_search.stem_text([keyword.lower()])
                if stemmed_name:
                    try:
                        tryKeyword = Keyword.objects.get(name=stemmed_name[0])
                    except Keyword.DoesNotExist:
                        # No exist stemmed keyword in DB, create and add
                        tryKeyword = Keyword(name=keyword)
                        tryKeyword.save()
                    keywordList.append(tryKeyword)

            descriptionString = ""

            description = weakness.find('Description')
            summary = description.find('Description_Summary')
            if summary is not None:
                descriptionString += re.sub('\s+', ' ', summary.text)

                detail = description.find('Extended_Description')
            if detail is not None and detail.find('Text') is not None:
                descriptionString += re.sub('\s+', ' ', detail.find('Text').text)

            curCWE, created = CWE.objects.update_or_create(code=int(ID), name=Name, description=descriptionString)
            if len(curCWE.keywords.all()) == 0:
                for keywordObj in keywordList:
                    curCWE.keywords.add(keywordObj)
                curCWE.save()
    except Exception as e:
        traceback.print_exc()



def run():
    print "Start Analyzing XML..."
    readXML()
