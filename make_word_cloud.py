#!/usr/bin/env python

"""Builds word cloud from csv file of terms and frequencies
$ python make_word_cloud.py {csv_file.csv}
"""

import argparse
import csv
import random

import numpy as np
from PIL import Image
from wordcloud import WordCloud

COLORS = [
	"hsl(306, 100%, 59%)",
	"hsl(231, 100%, 69%)",
	"hsl(180, 76%, 39%)",
	"hsl(224, 17%, 43%)",
]

# make word cloud in the shape of an image
IMAGE_FILE = "wordcloud_assets/girl.png"

parser = argparse.ArgumentParser()
parser.add_argument("csv_file", type=str, nargs=1)
args = parser.parse_args()
csv_file = args.csv_file[0]

# read csv file with terms and frequencies
with open(csv_file, mode='r') as f:
    reader = csv.reader(f)
    # skip header
    next(reader)
    freq_dict = {rows[0]:int(rows[1]) for rows in reader}

# custom colors
def color_func(word, font_size, position, orientation, **kwargs):
    return random.choice(COLORS)

# custom mask (image to put words into)
mask = np.array(Image.open(IMAGE_FILE))

# configure and build word cloud
wordcloud = WordCloud(
	background_color="white",
	font_path="wordcloud_assets/SourceSansPro-Regular.ttf",
	max_words=30,
	color_func=color_func,
	mask=mask,
	contour_width=3,
	contour_color='steelblue',
)
wordcloud.generate_from_frequencies(freq_dict)

# save as png
img_filename = csv_file.split('.')[0] + '_wordcloud.png'
wordcloud.to_file(img_filename)
print(f"Saved as {img_filename}")
