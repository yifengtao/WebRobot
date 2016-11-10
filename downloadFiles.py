'''
author: Yifeng Tao
acknowledgement: based on Weiguang Mao's scripts.
'''

import re
from mechanize import Browser
import HTMLParser

pattern = re.compile('Best*')

outputBase = '/Users/yifeng/Documents/Github/localData/'

class process(HTMLParser.HTMLParser):
    html_text = False
    def handle_starttag(self, tag, attr):
        if tag == 'h3':
            self.html_text = True
    def handle_endtag(self, tag):
        if tag == 'h3':
            self.html_text = False
    def handle_data(self, data):
        if self.html_text:
            if pattern.match(data):
                print data

def upload(count):
    br = Browser()
    br.set_handle_robots(False)
    br.open('http://zincpharmer.csb.pitt.edu/pharmer.html')
    #form = list(br.forms())[0]
    #br.form = form 
    formcount=0
    for form in br.forms():  
        if str(form.attrs['id']) == 'receptorForm': break
        formcount=formcount+1
    br.select_form(nr=formcount)
    form = br.form
    print form

    form.add_file( open(outputBase+str(count)+'.sdf'), 'text/plain', 'receptor.pdb')    
    #print form
    response = br.submit()
    # print response.read()
    # analysis
    print str(count)+'.sdf'
    analysis = process()
    analysis.feed(response.read())
    analysis.close()
    br.close()

if __name__ == '__main__':
    
    count = 1

    for i in range(1, count + 1, 1):
        #print i
        upload(i)
    print '\nAll submitted'


