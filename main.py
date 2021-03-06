'''
Not used in reality.
Author: Yifeng Tao
Acknowledgement: Based on Weiguang Mao's scripts.
Function: Automated submit results.
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
    br.open('http://zincpharmer.csb.pitt.edu/pharmville/')
    form = list(br.forms())[0]
    br.form = form 
    
    form['receptor'] = ['traf2']
    form.add_file( open(outputBase+'minimized_results.sdf'), 'text/plain', 'upload.sdf')
    form['userid'] = 'yifengt'
    form['name'] = 'Test'
    response = br.submit()
    
    print str(count)+'.sdf'
    analysis = process()
    analysis.feed(response.read())
    analysis.close()
    br.close()

if __name__ == '__main__':
    count = 2
    for i in range(1, count + 1, 1):
        upload(i)
    print '\nAll submitted'
    
