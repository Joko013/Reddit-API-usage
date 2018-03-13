# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:38:27 2018

@author: H
"""

import time
import praw
import pandas as pd
from datetime import datetime
import Reddit_login_info.login_info as login_info


reddit = praw.Reddit(client_id=login_info.client_id,
                     client_secret=login_info.client_secret,
                     password=login_info.password,
                     username=login_info.username,
                     user_agent=login_info.user_agent)   #top secret login info, create reddit object


class hots_sub(object):
    """ Object of Heroes of the Storm subreddit using Reddit API package - praw. """
    def __init__(self):

        self._hots_sub = reddit.subreddit('heroesofthestorm') #hots sub

    def get_submissions(self, date_from, date_to, query=None, export=False):   # enter dates as "DD.MM.YYYY"
        self._links = []
        
        if query == 'twitch':
            self._query = "(and site:'twitch.tv')"
        else:
            self._query = query
            
        try:
            self._date_from = datetime.strptime(date_from, "%d.%m.%Y").timestamp()   # convert dates to timestamp
            self._date_to = datetime.strptime(date_to, "%d.%m.%Y").timestamp()

            # submission from date_from to date_to as timestamp
            self._submissions = self._hots_sub.submissions(
                start=self._date_from,
                end=self._date_to, extra_query= self._query
            )

        except ValueError:
            print('Error! Please enter dates as "DD.MM.YYYY"')    
         
        for submission in self._submissions:
            self._links.append(
                {'link': submission.url,
                 'title': submission.title,
                 'created': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created))}
            )

        if export:
            self.export_links_to_xlsx()
            return "Saved {} submissions.".format(len(self._links))
        else:
            return self._links
    
    def export_links_to_xlsx(self):
        df = pd.DataFrame(columns=['link', 'title', 'created'])

        for item in self._links:
            app = pd.DataFrame(item, index=[len(self._links)], columns=['link', 'title', 'created'])
            df = df.append(app)
        writer = pd.ExcelWriter('links.xlsx')
        df.to_excel(writer, 'Sheet1')
        writer.save()

    @property    
    def count_submissions(self):
        return len(self._submissions)
    
    @property
    def submissions(self):
        return self._submissions
    
    
        
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        