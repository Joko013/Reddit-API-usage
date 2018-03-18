import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from pprint import pprint
import datetime
from Reddit.reddit import hots_sub
from sentiment_analysis import Analyzer

hs = hots_sub()

sid = SentimentIntensityAnalyzer()

#ss = sid.polarity_scores(sent)
#for k in sorted(ss):
#    print('{0}: {1}, '.format(k, ss[k]), end='')

# data = pd.read_excel('links.xlsx', dtype=str)  # dtype={"title": str, "created": datetime }
# data["created"] = pd.to_datetime(data["created"])

compound = []
neg = []
neu = []
pos = []

#for title in data['title']:
    # sentiments.append(sid.polarity_scores(title))
   # compound.append(sid.polarity_scores(title)['compound'])
    #neg.append(sid.polarity_scores(title)['neg'])
   # neu.append(sid.polarity_scores(title)['neu'])
    #pos.append(sid.polarity_scores(title)['pos'])

# data['compound'] = compound
# data['neg'] = neg
# data['neu'] = neu
# data['pos'] = pos

an = Analyzer()
an.sentiment_analysis("01.03.2018", "17.03.2018")
# pprint(an.submissions)
print(an.plot_sentiment())

# data.groupby(data["created"].dt.date).mean()["pos"].plot()
# data.groupby(data["created"].dt.date).mean()["neg"].plot()
# data.groupby(data["created"].dt.date).mean()["compound"].plot()
# plt.show()

# x = '2018-01-01 08:06:41'
# print(type(datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')))






