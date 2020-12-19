# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# from tqdm import tqdm
# import time
#
# alphabet = ['v', 'w', 'x', 'y', 'z']
# final = []
# name = []
# for i in tqdm(alphabet):
#     result = requests.get('https://kids-in-mind.com/'+str(i)+'.htm')
#     src = result.content
#     soup = BeautifulSoup(src, 'html.parser')
#     temp = soup.find_all('a', attrs={'target': '_blank', 'rel': 'noopener noreferrer'})
#     temp = temp[37:-9]
#     for j in temp:
#         x = str(j).split('"')[1]
#         final.append(x)
#     for k in temp:
#         x = str(k).split('>')[1]
#         x = x[0:-3]
#         if x in ['American, The']:
#             continue
#         else:
#             if x[-5:] == ', The':
#                 name.append('The ' + x[0:-5])
#             elif x[-4:] == ', An':
#                 name.append('An ' + x[0:-4])
#             elif x[-3:] == ', A':
#                 name.append('An ' + x[0:-3])
#             else:
#                 name.append(x)
#
# nudity = []
# violence = []
# language = []
# year = []
#
# for movie in tqdm(final):
#     result = requests.get('https://kids-in-mind.com' + str(movie))
#     src = result.content
#     soup = BeautifulSoup(src, 'lxml')
#     score = []
#     while True:
#         try:
#             div = soup.find_all('span', attrs={'style': 'font-size:14px !important'})
#             temp = str(div)
#             temp = temp[0:-8]
#             y = temp.split(' ')
#             year.append(y[3])
#             final_score = y[-1].split('.')
#             if final_score[0][-9:] == '/span&gt;':
#                 final_score[0] = final_score[0][:-9]
#                 nudity.append(int(final_score[0]))
#             elif final_score[0][-13:] == '<span></span>':
#                 final_score[0] = final_score[0][:-13]
#                 nudity.append(int(final_score[0]))
#             else:
#                 nudity.append(int(final_score[0]))
#             if final_score[1][-9:] == '/span&gt;':
#                 final_score[1] = final_score[1][:-9]
#                 violence.append(int(final_score[1]))
#             elif final_score[1][-13:] == '<span></span>':
#                 final_score[1] = final_score[1][:-13]
#                 nudity.append(int(final_score[1]))
#             else:
#                 violence.append(int(final_score[1]))
#             if final_score[2][-9:] == '/span&gt;':
#                 final_score[2] = final_score[2][:-9]
#                 language.append(int(final_score[1]))
#             elif final_score[2][-13:] == '<span></span>':
#                 final_score[2] = final_score[2][:-13]
#                 nudity.append(int(final_score[2]))
#             else:
#                 language.append(int(final_score[2]))
#             break
#         except IndexError:
#             div = soup.find_all('span', attrs={'style': 'font-size: 14px !important;'})
#             temp = str(div)
#             temp = temp[0:-8]
#             y = temp.split(' ')
#             year.append(y[3])
#             final_score = y[-1].split('.')
#             if final_score[0][-9:] == '/span&gt;':
#                 final_score[0] = final_score[0][:-9]
#                 nudity.append(int(final_score[0]))
#             elif final_score[0][-13:] == '<span></span>':
#                 final_score[0] = final_score[0][:-13]
#                 nudity.append(int(final_score[0]))
#             else:
#                 nudity.append(int(final_score[0]))
#             if final_score[1][-9:] == '/span&gt;':
#                 final_score[1] = final_score[1][:-9]
#                 violence.append(int(final_score[1]))
#             elif final_score[1][-13:] == '<span></span>':
#                 final_score[1] = final_score[1][:-13]
#                 nudity.append(int(final_score[1]))
#             else:
#                 violence.append(int(final_score[1]))
#             if final_score[2][-9:] == '/span&gt;':
#                 final_score[2] = final_score[2][:-9]
#                 language.append(int(final_score[1]))
#             elif final_score[2][-13:] == '<span></span>':
#                 final_score[2] = final_score[2][:-13]
#                 nudity.append(int(final_score[2]))
#             else:
#                 language.append(int(final_score[2]))
#             break
#     time.sleep(0.3)
#
# name = pd.DataFrame({'Name': name})
# year = pd.DataFrame({'Year': year})
# nudity = pd.DataFrame({'Nudity': nudity})
# violence = pd.DataFrame({'Violence': violence})
# language = pd.DataFrame({'Language': language})
# name.to_csv('1.csv')
# year.to_csv('2.csv')
# nudity.to_csv('3.csv')
# violence.to_csv('4.csv')
# language.to_csv('5.csv')
