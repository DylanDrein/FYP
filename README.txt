# FYP
## Final year CS project

https://github.com/DylanDrein/Python-FYP

+ [Download and install Anaconda for Package and Environment](https://www.continuum.io/downloads)
+ Conda package manager comes preinstalled. [Here's a thorough walkthrough of package management with Conda](https://conda.io/docs/test-drive.html)
+ In command prompt, use 'conda install [packagename]' to install relevant packages in your Python environment

## Packages to install:
1. Numpy
2. Scipy
3. Matplotlib
4. Pandas

## All imports used throughout the project are:
+ from __future__ import print_function
+ import json
+ import csv
+ import os
+ import numpy as np
+ import matplotlib.pyplot as plt
+ import scipy
+ import statsmodels
+ from scipy import stats
+ from operator import itemgetter, attrgetter, methodcaller
+ from collections import OrderedDict
+ from scipy.stats import ttest_ind, ttest_ind_from_stats
+ from scipy.special import stdtr
+ from statsmodels import +
+ from decimal import Decimal

__The data used for this project is saved in a file over 19.6GB in size before cleaning, ~9GB after cleaning. Not possible to include here.__

### ActualVsOptimalCalculator.py
Initial script used for exploration of data. Calculated actual and optimal distances for each user, saves them as well as efficiency (optimal/actual) in separate user files. No time distinction yet.

### Axis_Error_Analysis.py
Calculates the optimal and actual distances for both x and y components of in lab and out of lab click sequences
Writes these values from numpy arrays to 8 different CSV output files.

### CSVScript.py
Reads data from reversed JSON file, outputs to user categorised CSV file.

### ClickWaitTime.py
Calculates time the cursor hovered over click point and writes it to individual output files for each user which it creates

### ClickWaitTimes-relevant.py
Much more refined version of above deals with constraints and error values

### DayTimeWrite.py
Outputs all mouse events which took place on the day of each lab (the full 24 hour period)

### DotPlotScript.py
Creates scatter plots of all Click Sequences by individual user. 128 plots created in all.

### EfficiencyWithTimeGraphs.py
Reads in efficiency and time CSV files and plots efficiency using histograms and boxplots. Time used as a weight in histograms.

### EffvsTime.py
Creates scatter plot of mouse movement within both lab environments over time.

### FileReverse.py
Reverses original log file

### FixerScript.py
Kind of a rough work file

### GraphsTime.py
Histograms and box plots of Click Sequence time duration data

### HistogramScript.py
Individual user histograms of efficiency. Reads in JSON rather than CSV. Subsequently replaced.

### HovertimeGraphs.py
Histograms and box plots of mouse hover time

### In_Lab_X_Axes_Graphs.py
Analysis of x axis mouse movement in lab environment

### In_Lab_Y_Axes_Graphs.py
Analysis of y axis mouse movement in lab environment

### InitialCleaning.py
Initial script used to clean the data, removes unnecessary fields and outputs data to individual user JSON files

### LabBoxPlots.py
Box plots of data in lab environment

### LabDayHist.py
Histogram of mouse activity on day of lab exams

### LabDotPlot.py
individual user scatter plots of in lab data

### LabWeekData.py
Generates and outputs data from entire week of lab exam to CSV files

### LabWeekHist.py
Creates Histograms of mouse activity over week of lab exams

### MousePathScript.py
Plots all mouse events on a scatter plot, recreates path of mouse movements. Only used to generate a sample, way too many to generate all of them.

### Out_Lab_X_Axes_Graphs.py
Analysis of x axis mouse movement out of lab environment

### Out_Lab_Y_Axes_Graphs.py
Analysis of y axis mouse movement out of lab environment

### Overshoot-relevant.py
Calculates overshoot for relevant lab times

### Overshoot.py
Calculates overshoot for all click sequences 

### OvershootGraph.py
Graphs overshoot data

### SemesterTimeWrite.py
Creates data for mouse activity over entire semester

### SemesterTimeHist.py
Graphs mouse movement activity over semester

### SpeedwithTime.py
Generates data for speed with time weighting

### SpeedwithTimeGraph.py
Graphs the above

### TimeGraphs.py
Various graphs of time data

### TotalEfficiencyGraphs.py
Graphs various efficiency graphs using different weightings

### inVsOutLabData.py
Generates all CSV files for metrics and outputs them to files for in or out of lab

### ttest.py
Script used to do all hypothesis t-testing using Welch's t-test