#MapPlot.py
#Name:
#Date:
#Assignment:

import video_games
import pandas
import matplotlib.pyplot as plt
video_game = video_games.get_video_game()
reviews = []
years = []


for game in video_game:
    review = game["Metrics"]["Review Score"]
    year = game["Release"]["Year"]
    reviews.append(review)
    years.append(year)

df = pandas.DataFrame([{"Reviews" : review, 
                        "Years": year}])
print(df)
plt.plot(years, reviews, 'ro')
plt.savefig("output")