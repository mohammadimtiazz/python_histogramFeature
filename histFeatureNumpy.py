# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:56:41 2017

@author: Mohammad Imtiaz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt



def medianHistCal(binCount, binValue, percentile):
    dum = percentile/100.0
    totalPopulation = np.sum(binCount)
    medianBin = totalPopulation*dum
    binWithCounts = np.nonzero(binCount)
    sumBinCount = 0.0
    medianHist = 0.0
    for j in range(0, len(binWithCounts[0][:])):
        pos = binWithCounts[0][j]
        sumBinCount = sumBinCount + binCount[pos]
        if sumBinCount <= medianBin:
            nextKnownPos = binWithCounts[0][j+1]
            needStep = medianBin - sumBinCount
#            nextPos = binWithCounts[0][j+1]
            lowBinRange = binValue[pos]
            highBinRange = binValue[pos + 1]
            medianHist = lowBinRange + ((needStep/binCount[nextKnownPos]) * (highBinRange - lowBinRange))
        else:
            pass
    return medianHist



def histFeature(roi_gray):
    histR, binNumR = np.histogram(roi_gray, bins = 100)
#    plt.figure(1)
#    plt.bar(binNumR[:-1], histR, width = 1)
#    plt.xlim(min(binNumR), max(binNumR))
#    plt.show()
    
    #Mean Histogram
    num1 = 0.0
    dum1 = 0.0    
    for j in range(0,len(histR)):
        num1 = num1 + (histR[j] * binNumR[j])
        dum1 = dum1 + histR[j]
    meanHist = num1/dum1
    #meanHistSave.append(meanHist)
    
    
    #Sigma Histogram
    num2 = 0.0
    dum2 = 0.0
    for j in range (0, len(histR)):
        num2 = num2 + (histR[j] * (binNumR[j] - meanHist)**2)
        dum2 = dum2 + (float(histR[j]))
    sigmaHist = np.sqrt(float(num2/(dum2 -1)))
    #sigmaHistSave.append(sigmaHist)
    
    #FWHM of hist
    fwhmHist = 2* np.sqrt(2*np.log(2)) * sigmaHist
#	fwhmHistSave.append(fwhmHist)    
    
    #Measure Histogram HIgh: rightmost of all populated histogram bins
    binWithCounts = np.nonzero(histR)
    totalPopulation = np.sum(histR)
    highHist = (binNumR[binWithCounts[0][len(binWithCounts[0]) - 1]])/totalPopulation
#	highHistSave.append(highHist)    
    
    #Measure Histogram Low: rightmost of all populated histogram bins
    lowHist = (binNumR[binWithCounts[0][0]])/totalPopulation     
#    lowHistSave.append(lowHist)
    
    #call function medianHistCal function
    percintileHist50 = medianHistCal(histR, binNumR, 50) 
#	percintileHist50Save.append(percintileHist50)


    #Measuer RMS hist
    totalPos = binWithCounts[0][:]
    num3 = ((binNumR[totalPos])**2) * histR[totalPos]
    num3sum = np.sum(num3)
    rmsHist = np.sqrt(num3sum/totalPopulation)            
#	rmsHistSave.append(rmsHist)    
    
    #Measure maximum population
    maxPopulation = max(histR)
#    maxPopulationSave.append(maxPopulation)

     #Measure Range
    areaHist = binNumR[totalPos]
    rangeHist = abs(areaHist[0] - areaHist[len(areaHist) - 1])            
#    rangeHistSave.append(rangeHist)
    
#    Measure Percentile 
    percintileHist20 = medianHistCal(histR, binNumR, 20) 
    percintileHist40 = medianHistCal(histR, binNumR, 40) 
    percintileHist60 = medianHistCal(histR, binNumR, 60) 
    percintileHist80 = medianHistCal(histR, binNumR, 80)             
	
#	percintileHist20Save.append(percintileHist20)
#	percintileHist40Save.append(percintileHist40)
#	percintileHist60Save.append(percintileHist60)
#	percintileHist80Save.append(percintileHist80)     

    return meanHist, sigmaHist, fwhmHist, highHist, lowHist, rmsHist, maxPopulation, rangeHist, percintileHist20, percintileHist40, percintileHist50, percintileHist60, percintileHist80

    





img = cv2.imread('Strauss_GL (83)_FlatIris.pgm')
imgM = cv2.imread('Strauss_GL (83)_FlatMask.pgm')

img = img[:,:,0]
imgM = imgM[:,:,0]

#using numpy feature
hist, binNum = np.histogram(img, bins = 100) 
histM, binNumM = np.histogram(imgM, bins = 100) 
plt.figure(1)
plt.bar(binNum[:-1], hist, width = 1)
plt.xlim(min(binNum), max(binNum))
plt.show() 

plt.figure(2)
plt.bar(binNumM[:-1], histM, width = 1)
plt.xlim(min(binNumM), max(binNumM))
plt.show() 

meanHist_m, sigmaHist_m, fwhmHist_m, highHist_m, lowHist_m, rmsHist_m, maxPopulation_m, rangeHist_m, percintileHist20_m, percintileHist40_m, percintileHist50_m, percintileHist60_m, percintileHist80_m = histFeature(img)