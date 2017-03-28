# python_histogramFeature
various Features that can be extracted from a histogram using pyhton

features:
  mean
  sigma
  FWHM (full width half maximum)
  higest bin and total population ratio 
  lowgest bin and total population ratio 
  percentile20 -> 20% energy of a histogram
  percentile40 -> 40% energy of a histogram
  percentile50 -> 50% energy of a histogram
  percentile60 -> 60% energy of a histogram
  percentile80 -> 80% energy of a histogram
  RMS
  Max population
  Range
  
  
  histFeature() - > here all the features have been measure using numpy histogram lib
  
  histFeatureCV() - > here all the features have been measure using openCV histogram lib. Added advantage is that a mask can be used for     ignoring certain data during histogram calculation. The mask is a binary image. It will consider black pixel location for ignoring data. 
