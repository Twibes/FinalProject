![CodeChella Banner](application/static/img/codec.png)
![Logo](application/static/img/logo.png)

# Twibes - *the vibes you share*

## About Twibes
<br>

### What is Twibes?
<br>

Twibes is a web application that allows you to uplift your mental health with the help of music therapy.

Twibes analyzes your social media activity on Twitter to understand how positive or negative the content you share is and accordingly using Spotify's recommendation system to deliver music that will help uplift your mood. We also have a therapy chatbot that the people can use for preliminary counselling and support.
<br>
<br>

### Why the world needs Twibes
<br>

**The year 2020 has not been the best year for most of our community.** Whether we consider the Black Lives Matter protests in response to the killing of George Floyd and several other incidents, the Delhi Riots that occurred due to protests against the Citizenship Amendment Act in India, the End SARS movement in response to police brutality in Nigeria, or the COVID-19 pandemic which affected folks across the world or any other major issue, the year has definitely taken a toll on all of our health.

While a lot of us can cope with taking care of our physical health, most people are not well equipped to manage their mental health. A major reason for this is that there is a lot of stigma revolving around discussions of mental health in most parts of the world. That combined with the lack of education on mental health, **most people are either unaware of or reject the existence of mental health issues**.

Ever since the pandemic began, we have been restricted to the confines of our homes, limiting our interactions with our peers and acquaintances in the outside world. This has made it difficult for most people to find "safe spaces" where they can be themselves without any external worry. Due to this, one of the most convenient platforms for people to express is social media. **Social media is a great platform to quickly spread awareness** about different matters, **however it can promote as well as reinforce certain ideas or perspectives in peoples' minds, some of which may be highly detrimental**.

In this huge crisis around mental health, **we want to give people a chance to take their first steps in comfortable tracking the status of their mental health and heal it using** one of our favourite means, **music**. Music therapy is an evidence-based clinical use of musical interventions to improve peoples' quality of life that has existed for thousands of years. With this solution, **we look forward to enabling people all around the world to develop a habit of tracking their own mental health and care better for themselves**.
<br>
<br>

### Prospective Revenue Model for Twibes
<br>

For the time-being, all features in Twibes are available to test for free. However, when we launch this product in the market, we believe that the best revenue model for our product is a ***freemium model***.

The differences in the **Free** and **Premium** models, once the **Twibes** platform is fully ready, are stated below:

| | Free | Premium |
| - | - | - |
| Cost | No charge | $10 / month |
| Uses per Month | 5 | No limit |
| Tweets analyzed at a time | Last 30 tweets | Entire Twitter History |
| Automated therapy chatbot | ✔ | ✔ |
| Therapists-as-a-Service | ❌ | ✔ |
| Weekly analysis and email report | ❌ | ✔ |

*Need to add more points here*
<br>
<br>

### What's next for Twibes
<br>

We have several functionalities that we intend to implement in Twibes in the near future:
<br>

* Functionality to connect Premium users with therapists (Therapists-as-a-Service)
* Incorporate more social media feeds, like Facebook or Instagram.
* Automated weekly analysis of social media feed as well as emailed report.
* Improved track recommendations.
* Incorporate state of the art sentiment analysis models based in deep learning.
* Adding support for a continued sentiment analysis, so that we can predict and detect in advance when a person will need assistance.
* We plan to do a continued analysis, over tweets of premium users over a longer time period, (using Premium Twitter API) and make them analyze improvements, on      their mental health.


<br>

---

## Developing Twibes
<br>

### How we built Twibes
<br>

The tech stack used to create **Twibes** is as follows:

* The web app has been built using **Flask**.
* The web app has been deployed using **Azure App Service**.
* The front end of the web app has been built using **HTML**, **CSS**, and **Bootstrap**.
* The OAuth and social media data has been obtained using the **Twitter API**.
* The Twitter feed is accessed using the **Twitter API** and **tweepy**.
* The sentiment analysis is carried out by using a **fasttext** model, analyzing sentence by sentence.
* Sentence tokenization is done by means of a **Punkt sentence tokenizer**, provided by **NLTK**.
* The music playlists based on the user's sentiment are generated using the **Spotify API**.
* The therapy chatbot has been built using **Azure QnA Maker** and **Azure Bot Service**.

<br>

<img src="https://img.icons8.com/color/48/000000/python.png"><img src="https://img.icons8.com/color/48/000000/azure.png"><img src="https://img.icons8.com/color/48/000000/twitter.png"><img src="https://img.icons8.com/color/48/000000/spotify.png"><img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg"><img src="https://fasttext.cc/img/ogimage.png" height="55"><img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" height="50"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" height="50">

### Features that Twibes covers
<br>

We have various features in the platform designed to help the users better understand their mental state:

* Twitter feed analysis & Insights
* Sentiment-based music playlists
* Automated therapy chatbot

<br>
<br>

### Challenges that we faced in the process
<br>

* We really struggled deciding how the Twitter feed analysis was going to be carried out, but in the end we succeded.
* Documentation for Twitter OAuth was missing from the portal had to use multiple old tutorials to get the OAuth up and running. Twitter Ouath plus flask is bit tricky ever since the new update

<br>
<br>

### Accomplishments that we're proud of
<br>

* We're really proud of having successfully implemented a Twitter feed sentiment analysis.
* We're also really proud of having successfully trained and incorporated a chatbot tailored for emotional support.
* Last but not least, we're also really proud of having created an application that puts together the Twitter and Spotify API in a meaningful way.
* Setted up the Twitter Oauth through extensive trail and error
---

## The Team Behind Twibes
<br>

| <img src="application/static/img/Anush.jpg" height=150> | <img src="application/static/img/Aanisha.jpg" height=150> | <img src="application/static/img/Victor.jpg" height=150> | <img src="application/static/img/Onajite.jpg" height=150> | <img src="application/static/img/Aditya.jpeg" height=150> |
| - | - | - | - | - |
| Anush Krishna V | Aanisha Bhattacharyya | Victor Dorado Javier | Onajite Taire | Aditya Oberai |
| [@Anush_krishna_v](https://twitter.com/Anush_krishna_v) | [@AanishaBhattac2](https://twitter.com/AanishaBhattac2) | [@TheVidoja](https://twitter.com/TheVidoja) | [@wonataire](https://twitter.com/wonataire) | [@adityaoberai1](https://twitter.com/adityaoberai1) |
