# Helpfulness-Analysis

### Notebooks
__aspect_extraction.ipynb__: Extracting aspects and plot the relation between number 
of aspects and helpfulness score. 

__Detect_Plagiarism_smaller_data.ipynb__: Plagiarism detection and text quality measure 
for data sets which can load completely into memory. For other's storage to hard disk is 
required at some checkpoints (as done in Detect_Plagiarism_large_data.ipynb)

__timestamp_helpfulness.ipynb__: Analyse relation between timestamp and number of helpfulness
votes for items.

__deviation_plot.ipynb__: Notebook for plotting helpfulness ratio as 
a function of deviation from mean review rating. 
Plots also for different satandard deviation data.

__helpful_ml.ipynb__: Machine learning approach to predict helpfulness (TODO)

### Datasets
__data/data_frames__: 

[Item_Category].pkl - items with more than 5 helpfulness scores.
Contains info about itemID, reviewerID, helpfulness, star rating

[Item_Category].time.pkl - same as above but contains timestamp instead of star rating.

__plg/data_frames__:

[Item_Category].pkl - items with more than 10 helpfulness scores.
Contains all info as contained in original data set

__plg/data_frames_fp__:

[Item_Category].pkl - same as above but contains fingerprints computed instead of original 
review text

### Utility files

__generate_data[*].sh__: To process data in batches and store dataframes as pickle files.
Calls generate_data[*].py.

__generate_data[*].py__: Process data to extract what is required for each batch.
