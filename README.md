# WhatsApp Chat Analysis 
An exploratory data analysis project which analyses the traits of users in a whatsapp chat. It also analyses the sentiments using nlp lib VADER.

Link: [https://hinglishchatanalysis.herokuapp.com/](https://hinglishchatanalysis.herokuapp.com/)

[![Web App GIF](https://i.imgur.com/dPbBY80.gif)](https://hinglishchatanalysis.herokuapp.com/)

## Inspiration
Whatsapp is an excellent platform for groups with friends, family and colleagues to coexist. Over the years we would have sent out thousands of messages and read millions of messages in the app. A lot of insights can be dug up from just a single chat. 

Hence analysing these messages will figure out the messaging pattern of the individual by checking the time at which he normally sends messages in the morning and evening and in turn their sleeping pattern, understanding if he/she is a conversation starter or not? Understand how active they are in certain groups and the list is endless.
These insights will help paint a picture of the nature of a person.

## Overview
This `Streamlit` app takes chat from the user in the form of text file.

The data is cleaned and preprocessed using `preprocessor.py`. The chat may include hinglish, so I have used `stop_hinglish.txt` which contains stopwords of both english and hindi.

The data is analysed using `helper.py` and is visualized using bar/line graph, wordcloud, heatmap, pie charts.

## Installation
The Code is written in Python 3.9.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download CLI to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

create new app and provide an unique app name. This name will be depicted in the url of your app.

1. To deploy using Heroku Git:
Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), and run these commands
```bash
    heroku login
```
```bash
    cd <go-to-your-project-directory>/
```
```bash
    git init
```
```bash
    heroku git:remote -a <add-your-app-name>
```
```bash
    git add .
```
```bash
    git commit -am "make it better"
```
```bash
    git push heroku master
```
2. To deploy using github:
Connect this app to GitHub and search for a repository to connect to. Then choose between automatic or manual deployment. Heroku will start building the app and satisfying the requirements from requirements.txt

## Directory Tree 
```
├── Procfile
├── README.md
├── app.py
├── helper.py
├── nltk.txt
├── preprocessor.py
├── requirements.txt
├── setup.sh
├── stop_hinglish.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)[<img target="_blank" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width=200>](https://streamlit.io/) [<img target="_blank" src="https://matplotlib.org/3.1.1/_static/logo2_compressed.svg" width=200>](https://matplotlib.org/) [<img target="_blank" src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_bf0fb4cb7fe948c42f37ded73895638f/salesforce-heroku.png" width=170>](https://en.wikipedia.org/wiki/Heroku) 
