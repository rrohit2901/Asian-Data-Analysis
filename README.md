# Social Data Analysis

### Initial Dataset analysis
This dataset contained posts of Indian, Chinese, Phillipino and Vietnamese people residing in America on social media websites. I performed analysis on this dataset to look for patterns in political posts made by members of these communities
Performed following analysis for posts of all 4 communities:
1. Temporal analysis on number of posts
2. Extracted statistics about pages posting on content and sorted them based on number of posts made by the account/page and number of subscribers.
3. Analysed most frequently used words in the dataset.
4. Logged average and standard deviation of number of reactions on post to study reach of posts
5. Extracted popular URLs in the posts in the dataset.
6. Performed topic modelling on the data set
7. Trained word2vec model on the posts to study similar words corresponding to words of intrest like america, politics, etc.

### Scraping data from crowdTangle
Collected posts correspondong to given hashtags using crowdtangle api, for the span of 3 years.

### Analysis of collected data
This dataset contained Facebook and Instagram posts related to hashtags like #stopasianhate, #stopaapihate, etc. I perfomed analysis on this dataset to study potential patterns in counterspeech against hate being spread against Asians on social media. Following methods were used to separately study facebook and instagram posts:
1. Temporal analysis on number of posts
2. Extracted statistics about pages posting on content and sorted them based on number of posts made by the account/    page and number of subscribers.
3. Analysed most frequently used words in the dataset.
4. Logged average and standard deviation of number of reactions on post to study reach of posts
5. Extracted popular URLs in the posts in the dataset.
6. Performed topic modelling on the data set.
7. Trained word2vec model on the posts to study similar words corresponding to words of intrest like asian, virus, corona etc.
8. Analysed common hashtags occuring in the posts to understand the message being conveyed
9. Formed similarity graph of words using similar words upto 2 levels using word2vec model trained.
10. Applied community detection method on word similarity graphs to understand words used in similar context in the posts.
11. Formed co-occurence graph of hashtags and applied community detection algorithm on the graph to study similar hashtags used together frequently in the posts.
12. Analysed number of posts of each language in the dataset to see if there are other languages in which large number of poeple are posting counterspeech content.

### Indian Political Data
I also collected data on Indian Political System to study BJP ecosphere in India.
Properties of collected data:-
- Collected using hashtags related to BJP and Indian political system
- Has posts spanning from last 7 years
- Has posts from both Facebook and Instagram
I did following analysis on data, separately for facebook and Instagram:-
1. Temporal analysis on number of posts                                                                                                                                                                        
2. Extracted statistics about pages posting on content and sorted them based on number of posts made by the account/page and number of subscribers.                                                         
3. Analysed most frequently used words in the dataset.                                                                                                                                                         
4. Logged average and standard deviation of number of reactions on post to study reach of posts                                                                                                                
5. Extracted popular URLs in the posts in the dataset.                                                                                                                                                         
6. Performed topic modelling on the data set.                                                                                                                                                                  
7. Trained word2vec model on the posts to study similar words corresponding to words of intrest like asian, virus, corona etc.                                                                                 
8. Analysed common hashtags occuring in the posts to understand the message being conveyed                                                                                                                     
9. Formed similarity graph of words using similar words upto 2 levels using word2vec model trained.                                                                                                            
10. Applied community detection method on word similarity graphs to understand words used in similar context in the posts.                                                                                     
11. Formed co-occurence graph of hashtags and applied community detection algorithm on the graph to study similar hashtags used together frequently in the posts.                                              
12. Analysed number of posts of each language in the dataset to see if there are other languages in which large number of poeple are posting counterspeech content.

### Failed Experiments
As a part of exploratory data analysis, I tried other things which ended up yeilding no results. Some of these were:-
- Using OCR to get images from text - This was a very time taking process and yet the results generated from the experiment was inconclusive and very inaccurate
- Translation of Non-english posts to english - This was again done using Google Translate Python API which was very slow for such large number of posts and hence the idea was discarded
- Using Hierachical clustering in hashtag analysis - Results were similar to community detection only and hence was discarded

### Description of files in the repo
1. DataAnalysis - This file contains analysis of initial data provided. It also contains analysis of translated text as a part of content in the posts were in languages different from english.
2. Facebook - This file contains analysis of counterspeech posts collected from Facebook.
3. FileToCSV - This has utility to read all files in folder and convert them into unified CSV.
4. HashtagPosts - This file has utility to check for number of posts corresponding to particular hashtag for any span in the past on Facebook and Instagram.
5. Instagram - This file contains analysis of counterspeech posts collected from Instagram.
6. Word2Vec - This file contains word2vec analysis of the initial data set provided.
7. Scraper.py - This file contains utility to collect posts corresponding to hashtag from crowdtangle.
8. Indian-Political-Data - This folder contains codes for analysis of Indian Political Data

### Datasets used
- Intial dataset used - https://drive.google.com/drive/u/6/folders/1NMO1ulcDDThJsa8SVyr5rKTyxK4Ig3ys
- Collected data on asian counterspeech - https://drive.google.com/drive/u/6/folders/1oA2XWtCqDvriOpw1n1QutVndK5GlCp5A
- Collected data on Indian Political Scenario - https://drive.google.com/file/d/1zBlx0-JVtSx3PtZkcEAUiqUg2RF8uTC8/view?usp=sharing
