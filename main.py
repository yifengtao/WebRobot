'''
author: Yifeng Tao
acknowledgement: based on Weiguang Mao's scripts.
'''

import re
from mechanize import Browser
from HTMLParser import HTMLParser
MaxLigand = 1000

pattern = re.compile('Best*')

outputBase = '/Users/yifeng/Documents/Github/localData'

class process(HTMLParser):
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
    br.form = [form for form in br.forms()][0]



















