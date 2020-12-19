__IMDB RATING GENERATOR__

____________________________ METHODOLOGY __________________________________

We webscraped the https://kids-in-mind.com/ website to get a score of Nudity, Violence and Language for around 5200 movies. Using the resulting dataset, we scraped https://en.wikipedia.org/wiki/Main_Page site to download the plot of each movie and use this text as an input in sentiment analysis to see the positivity/ negativity of the movie. We used the IMDB dataset to download important details like budget and IMDB rating of each movie and this resulted in the final csv shown in this repository (ie. FinalMovieUpdated2.csv). 

Finally, we created a dash app that runs in a browser using flask. This serves as our 'front-end' to receive input data from the user. We intially planned on using AWS to display our results but the app slowed down because of the large csv file.

'knm.py' and 'wiki.py' were used to create the final dataset and show the webscraping process.

______________________STEPS TO USE THE DASH APP ___________________________

1. Download the entire repository into the desired directory
2. Open the 'main.py' and download the packages mentioned in the 'requirements.txt' text file.
3. Run the 'main.py' file and use the ip address mentioned in the result section to open the project in a browser
4. In the app, use the first section to enter input details of your movie. 
4. Choose a maximum of 3 genres at a time because the app only looks through movies in our dataset. 
5. The 'SEX/ NUDITY', 'VIOLENCE' and 'LANGUAGE' sections take in values between 0 (less) and 10 (more).
6. Enter the plot of the imaginary movie and please try to make the text as long as possible for better results.
7. Click the submit button and view the results at the bottom.
8. Based on your choices, the graph will show how 'Our Movie' fared against other movies with similar genres


__THANK YOU!!!!!!!!!!__
