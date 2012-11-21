from lxml import etree
import re


def get_uncountable_nouns(input_file_name):

    context = etree.iterparse(input_file_name)

    uncountable_nouns = []
    temp_title = ''
    tag_title = '{http://www.mediawiki.org/xml/export-0.8/}title'
    tag_text = '{http://www.mediawiki.org/xml/export-0.8/}text'

    i = 0
    for event, element in context:
            if element.tag == tag_title:
            	temp_title = element.text
            if element.tag == tag_text:
                temp_text = element.text
                if not (temp_text is None) and re.search(r'{{en-noun(\|[a-z]+)?\|\-(\|[a-z]+)?}}', temp_text):
                    uncountable_nouns.append(temp_title)
            element.clear()
    return uncountable_nouns

def write_uncountable_nouns(input_file_name, output_file_name):
    result = []

    for item in get_uncountable_nouns(input_file_name):
        if re.match(r'\A[A-Za-z]+\Z', item.encode('utf-8')):
            result.append(item.encode('utf-8'))
            print item.encode('utf-8')

    f = open(output_file_name, 'w')
    for i in result:
        f.write("%s\n" % i)
    return result

write_uncountable_nouns('d:/1OKSANA/wictionary_parsing/enwiktionary-latest-pages-articles.xml', 'd:/1OKSANA/wictionary_parsing/f.txt')
