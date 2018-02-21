# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:38:27 2018

@author: H
"""

import time
import praw
import csv
import pandas as pd
from datetime import datetime
import nltk
import login_info


reddit = praw.Reddit(client_id=login_info.client_id,
                     client_secret=login_info.client_secret,
                     password=login_info.password,
                     username=login_info.username,
                     user_agent=login_info.user_agent)   #top secret login info, create reddit object


class hots_sub(object):
    def __init__(self, date_from, date_to, query=None): #enter dates as "DD.MM.YYYY"
        
        if query == 'twitch':
            self._query = "(and site:'twitch.tv')"
        else:
            self._query = query
        
        self._hots_sub =  reddit.subreddit('heroesofthestorm') #hots sub
        self._count = 0
        try:
            self._date_from = datetime.strptime(date_from, "%d.%m.%Y").timestamp() #convert dates to timestamp
            self._date_to = datetime.strptime(date_to, "%d.%m.%Y").timestamp()
            self._submissions = self._hots_sub.submissions(start=self._date_from,end=self._date_to, extra_query= self._query) #submission from date_from to date_to as timestamp
        except ValueError:
            print('Error! Please enter dates as "DD.MM.YYYY"')

    
           
    def get_twitch_links(self, export = False):
        self._twitch_links = []
        for submission in self._submissions:
            if 'twitch.tv' in submission.url: #only submissions with 'twitch' in the url
                self._twitch_links.append({'link': submission.url, 'title': submission.title, 'created': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created))})
        if export == True:
            self.export_links_to_xlsx()
        return self._twitch_links
    
    def export_links_to_xlsx(self):
        df = pd.DataFrame(columns = ['link', 'title', 'created'])
        for item in self._twitch_links:
            app = pd.DataFrame(item, index=[self._count], columns = ['link', 'title', 'created'])
            df = df.append(app)
            self._count += 1
        writer = pd.ExcelWriter('twitch_links.xlsx')
        df.to_excel(writer,'Sheet1')
        writer.save()

    def export_titles_to_csv(self):
        self._titles = []
        df = pd.DataFrame(columns = ['link', 'title'])
        for submission in self._submissions:
            self._titles.append({'title': submission.title, 'date': submission.created , 'link': submission.url,})
        for item in self._titles:    
            app = pd.DataFrame(item, index = [self._count], columns = ['date', 'title', 'link'])
            df = df.append(app)
            self._count += 1
        df.to_csv('titles.csv')
        return "Saved {} submissions.".format(self._count)
        
    @property    
    def count_submissions(self):
        return self._count
    
    @property
    def submissions(self):
        return self._submissions
    
    
        
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        