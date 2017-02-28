import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handlein = open("./Efficiencies/inlab.csv", 'rb')
handleout = open("./Efficiencies/outlab.csv", 'rb')

inlabeff = []
outlabeff = []


with handlein as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabeff = np.array(list(row)).astype(np.float)


with handleout as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabeff = np.array(list(row)).astype(np.float)

bins = np.arange(0, 1.01, 0.01)

sdvinlab = np.std(inlabeff)
meaninlab = np.mean(inlabeff)
label1 = ["SD: " + str(sdvinlab) + "\n" + "Mean: " + str(meaninlab)]
plt.hist(inlabeff, bins, normed=True, label = label1)
plt.title("Probability Density Function of in-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length")
plt.ylabel("Probability density")
plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
#plt.xticks(bins1, ["{:d}".format(int(v)) for v in hours], rotation = 'vertical')
#plt.xticklabels(["{:d}".format(int(v)) for v in hours]) 
#plt.subplots_adjust(bottom=0.15)
#xposition = range(firstlabmidnight - 3*(daymilliseconds), firstlabmidnight + 3*(daymilliseconds), daymilliseconds)
#for xc in xposition:
#    plt.axvline(x=xc, color='r', linestyle='solid', linewidth = 0.5)
plt.legend()
plt.show()
#plt.savefig('./Histograms/' + "LabWeek1" + '.png')
plt.clf()

sdvoutlab = np.std(outlabeff)
meanoutlab = np.mean(outlabeff)
label2 = ["SD: " + str(sdvoutlab) + "\n" + "Mean: " + str(meanoutlab)]
plt.hist(outlabeff, bins, normed=True, label = label2)
plt.title("Probability Density Function of out-of-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length")
plt.ylabel("Probability density")
plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
#plt.xticks(bins1, ["{:d}".format(int(v)) for v in hours], rotation = 'vertical')
#plt.xticklabels(["{:d}".format(int(v)) for v in hours]) 
#plt.subplots_adjust(bottom=0.15)
#xposition = range(firstlabmidnight - 3*(daymilliseconds), firstlabmidnight + 3*(daymilliseconds), daymilliseconds)
#for xc in xposition:
#    plt.axvline(x=xc, color='r', linestyle='solid', linewidth = 0.5)
plt.legend()
plt.show()
#plt.savefig('./Histograms/' + "LabWeek1" + '.png')
plt.clf()
