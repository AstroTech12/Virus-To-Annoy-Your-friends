import webbrowser
import time
import random

while True:
        sites = random.choice(['google.com', 'bmovies.pro', 'youtube.com', 'y8.com'])
        visit = "http://{}".format(sites)
        webbrowser.open(visit)
        seconds = random.randrange(5, 20)
        