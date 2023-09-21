*Topsters*

![image](https://raw.githubusercontent.com/knnthchng/topsters/main/Visuals/topsters_sample.jpg)

**BACKGROUND**
----------------------------------------------------------------------------------------
For the past few months, I have been taking classes in data analytics and visualization, and after learning how to use Python, Pandas, and MatPlotLib, I decided to create and analyze a dataset of my favorite albums of all time, which I have kept a running tally of for the past 8 or so years.

During my adolescence, I became interested in exploring popular music after picking up an issue of Q magazine with the cover story of the greatest albums ever as voted by their readers. Such lists from that magazine and other outlets, as well as year-end best-of lists from Q and other publishers, have helped guide my musical explorations, in addition to other discoveries I've made on my own. 

With this dataset, I wanted to profile my musical tastes, exploring which years, genres, and countries are predominantly represented in my list, and conversely those which are underrepresented. With these analyses, I can also identify opportunities to further diversify and round out my musical explorations, by finding genres, years, or even countries whose music I should seek out next.

**DATASET**
----------------------------------------------------------------------------------------
The dataset consists of 200+ albums, with each entry consisting of the album's title, artist, release year, genre, length (in minutes), the releasing record label, and the artist's country of origin. 

The albums were originally listed in my personal iTunes library, and album metadata was applied automatically by iTunes from Gracenote's database. Wikipedia was referenced to verify each album's release year, genre, length, record label, artist's country of origin, and whether or not it is a compilation album. All of this information was manually entered into Microsoft Excel, and the spreadsheet was saved in CSV format.

**CONTENTS**
----------------------------------------------------------------------------------------

* Data - Folder contains the album data in both CSV and XLSX format

* Reports - Folder will have documents containing the data analyses and conclusions

* Visuals - Folder contains plots generated from the Jupyter notebooks, in JPG and PNG format.

* Jupyter notebooks - Several Jupyter notebooks have been made to run data analyses. The notebooks named with matplotlib or sns at the end focus on the use of those respective Python libraries for visualization.

* input_form.py - This Python script can be used to add new albums to the CSV file in the Data folder. (Currently troubleshooting an issue where input data gets added to the right of the last row instead of being added as a new row on the bottom)

**"VERSION LOG"**
----------------------------------------------------------------------------------------

As I kept working on this project, I decided to expand the scope of my analyses by adding more data fields to analyze. The input form and the data files are all marked with version numbers, charting the evolution of my analyses.

* v.1: Initial version of Topsters database. Data surveyed consists of album title, artist, release year, genre, album length, record label, and whether it's a compilation or not.

* v.2: Added data and fields for subgenres and descriptors, based on such data available from RateYourMusic.

* v.3: Added total number of tracks/songs each album contains.