# import wikipedia
# import pandas as pd
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# import tqdm
# import time
#
#
# data = pd.read_csv('Final_Movie.csv')
# print(len(data))
# analyzer = SentimentIntensityAnalyzer()
# score1 = []
# score2 = []
# score3 = []
#
#
# class Wiki:
#     def __init__(self, name):
#         self.name = str(name)
#
#     def wiki(self):
#         source = wikipedia.page(str(self.name))
#         text = source.content
#         paras = text.split('== Plot ==')
#         paras = paras[1].split('== Cast ==')
#         x = str(paras[0])
#         return x
#
#     def wiki1(self):
#         source = wikipedia.page(str(self.name))
#         text = source.content
#         paras = text.split('== Synopsis ==')
#         paras = paras[1].split('== Cast ==')
#         x = str(paras[0])
#         return x
#
#     def wiki2(self):
#         source = wikipedia.page(str(self.name))
#         text = source.content
#         paras = text.split('== Premise ==')
#         paras = paras[1].split('== Cast ==')
#         x = str(paras[0])
#         return x
#
#
# # x = Wiki('Four Kids and It (2020) (film)')
# # text = x.wiki2()
# # print(text)
# # s = analyzer.polarity_scores(text)
# # print((list(s.values())[-1]))
#
# for i in tqdm.tqdm(range(len(data))):
#     while True:
#         try:
#             x = Wiki(str(data['Name'][i]) + ' (' + str(data['Year'][i]) + ') (film)')
#             text = x.wiki()
#             s = analyzer.polarity_scores(text)
#             score1.append(list(s.values())[-1])
#             time.sleep(0.00001)
#             break
#         except Exception:
#             score1.append('')
#             break
#
#
# for i in tqdm.tqdm(range(len(data))):
#     while True:
#         try:
#             x = Wiki(str(data['Name'][i]) + ' (' + str(data['Year'][i]) + ') (film)')
#             text = x.wiki1()
#             s = analyzer.polarity_scores(text)
#             score2.append(list(s.values())[-1])
#             time.sleep(0.00001)
#             break
#         except Exception:
#             score2.append('')
#             break
#
# for i in tqdm.tqdm(range(len(data))):
#     while True:
#         try:
#             x = Wiki(str(data['Name'][i]) + ' (' + str(data['Year'][i]) + ') (film)')
#             text = x.wiki2()
#             s = analyzer.polarity_scores(text)
#             score3.append(list(s.values())[-1])
#             time.sleep(0.00001)
#             break
#         except Exception:
#             score3.append('')
#             break
#
# scores_results = pd.DataFrame({'1': score1, '2': score2, '3': score3})
# scores_results.to_csv('scoreresults.csv')
# # data = pd.read_csv('descriptions.csv')
# # analyzer = SentimentIntensityAnalyzer()
# # score = []
# # for i in range(len(data)):
# #     x = analyzer.polarity_scores(str(data['Name'][i]))
# #     score.append(list(x.values())[-1])
# # sentiment = pd.DataFrame({'Sentiment': score})
# # sentiment.to_csv('sentiment.csv')
