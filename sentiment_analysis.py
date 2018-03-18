import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from pprint import pprint
import datetime
from Reddit.reddit import hots_sub


class Analyzer(object):
    """ Analyzer for reddit sentiment analysis. """
    def __init__(self):
        self._hs = hots_sub()
        self._df_submissions = pd.DataFrame()

    def sentiment_analysis(self, date_from, date_to, query=None):
        """ Analyse submissions specified by [date_from], [date_to] and optional [query] parameters. """

        self._submissions = self._hs.get_submissions(date_from, date_to, query)

        df = pd.DataFrame(self._submissions)
        df["created"] = pd.to_datetime(df["created"])

        sid = SentimentIntensityAnalyzer()

        # self._analyzed = df["title"].apply(lambda x: sid.polarity_scores(x))

        df['compound'] = df["title"].apply(lambda x: sid.polarity_scores(x)['compound'])
        df['pos'] = df["title"].apply(lambda x: sid.polarity_scores(x)['pos'])
        df['neu'] = df["title"].apply(lambda x: sid.polarity_scores(x)['neu'])
        df['neg'] = df["title"].apply(lambda x: sid.polarity_scores(x)['neg'])

        self._df_submissions = df

        return "Analyzed {} submissions".format(len(self._df_submissions))

    def plot_sentiment(self):
        """ Plot analysed submissions. """

        if self._df_submissions.empty:
            return "No submissions to be plotted, run sentiment_analysis first. "
        else:
            self._df_submissions.groupby(self._df_submissions["created"].dt.date).mean()["compound"].plot()
            plt.show()

    @property
    def submissions(self):
        if self._df_submissions.empty:
            return "No submissions to be printed. "
        else:
            return self._df_submissions












