This repository contains self-contained NLP examples.

### Table of Contents
- <a href='#word-vector'>Word-Vector</a> 
  - <a href='#word-vector-spacy'>WordVector-Spacy</a> 
  - <a href='#word-vector-gensim'>WordVector-Gensim</a> 
- <a href='#text-wrangling'>Text Wrangling</a> 
- <a href='#text-classification'>Text Classification</a>
- <a href='#spam-detection'>Spam Detection</a> 
- <a href='#sentiment-analysis'>Sentiment Analysis</a>
  - <a href='#sentiment-analysis-spacy'>SentimentAnalysis-Spacy</a>
  - <a href='#sentiment-analysis-vader'>SentimentAnalysis-VADER</a>
  - <a href='#sentiment-analysis-textblob'>SentimentAnalysis-TextBlob</a>
- <a href='#chatbot'>ChatBot</a>  
  
<hr>
 

- ###### [Word Vector Spacy:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/blob/Word-Vector/Spacy-Word2Vec.ipynb)
   ###### This example is an implementation of Word to Vector concept using Spacy Library. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/blob/Word-Vector/Spacy-Word2Vec.ipynb)  
  * Install Spacy on Anaconda:
![image](https://user-images.githubusercontent.com/689226/50120718-83af1300-027c-11e9-85c1-7bacb4c129db.png)
![image](https://user-images.githubusercontent.com/689226/50121286-49df0c00-027e-11e9-9ab2-5a3e5875008b.png)
![image](https://user-images.githubusercontent.com/689226/50174045-228c4b80-031f-11e9-9546-c189b7f0acf8.png)
  * Computes similarity among all tokens' combinations
 

<hr> 
  
- ###### [Word Vector Gensim:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/blob/Word-Vector/Gensim-Word2Vec.ipynb)
   ###### This example is an implementation of Word to Vector concept using Gensim Library. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/blob/Word-Vector/Gensim-Word2Vec.ipynb)
  * Install Gensim on Anaconda:
![image](https://user-images.githubusercontent.com/689226/50122009-bbb85500-0280-11e9-926b-7510761bcff8.png)
  * Compute similarity between all tokens
  
<hr>

- ###### [Text Wrangling:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/TextWrangling)
   ###### This example illustrates various processes involved during Text Cleaning. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/TextWrangling)
  * Install Spacy on Anaconda [Refer Above]
  * Convert sentence into Lemma
  * Removal of Pronoun 
  * Removal of Stop Words
  * Removal of Punctuations
  * Selecting Nouns
  * Word count and Frequency
  * Converting into Text -> List of Sentences -> List of Clean Sentences
  * BagOfWords/CountVectorizer/Sparse on Sentences
  * BagOfWords/CountVectorizer/Sparse on File
  * TF-IDF (Vectorizer) on Sentences
  * TF-IDF (Vectorizer) on File

<hr>

- ###### [Text Classification](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/TextClassification) 
   ###### This example exemplify Text Classification using TF-IDF. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/TextClassification)
   * Load the data [Consumer_Complaints.csv]
   * Select desired Columns
   * Removal of unwanted rows
   * Clean and Prepare Data
   * Split Dataframe as (Train+Test) </br>
   ![image](https://user-images.githubusercontent.com/689226/50539512-7d3b6800-0ba7-11e9-8cfe-52646d7d3bad.png)
   * Apply CountVectorizer
   * Apply TF-IDF (Transformer)
   * Apply ML Modeling with MultinomialNB
   * Make Predictions


<hr>

- ###### [Spam Detection](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SpamDetection) 
   ###### This example is an analysis on SMS Spam Predction. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SpamDetection)
   * Load the data [spam.csv]
   * Removal of unwanted columns
   * Break the complete dataset into data(for training and validation) + untouched data
   * Replacing Categorical Feature into Numerical Feature
   * Split Dataframe as (Train+Test)
     Refer above for (Train+Test) pictorial representation
   * Apply CountVectorizer/Sparse on train_X
   * Apply CountVectorizer/Sparse on test_X
   * Apply ML Modeling with MultinomialNB
   * Make Predictions
   
   
<hr>

- ###### [Sentiment Analysis Spacy:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/Spacy-TextClassification-SentimentAnalysis)
   ###### This example demonstrates Sentiment Analysis by Text Classification using Spacy Library. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/Spacy-TextClassification-SentimentAnalysis)
   * Install Spacy on Anaconda [Refer Above]
   * Load the data-Yelp+IMDB+Amazon[sentimentdataset.csv]
   * Clean Sentences
   * Tokenize
   * Vectorize
   * Classify
   * Predict the Sentiments.

<hr>

- ###### [Sentiment Analysis VADER:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/VADER-SentimentAnalysis)
   ###### This example demonstrates Sentiment Analysis using VADER Library. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/VADER-SentimentAnalysis)
   ######  VADER(Valence Aware Dictionary and sEntiment Reasoner) is a Lexicon and rule-based sentiment analysis library. It includes sentiment from emoticons (e.g, :-)), sentiment-related acronyms (e.g, LOL) and slang (e.g, meh). 
   * Install VADER on Anaconda
   * VADER Sentiment Scale:
  ![image](https://user-images.githubusercontent.com/689226/50122967-ddb3d680-0284-11e9-9a47-d59e8fdcb340.png)
   * Effect of Punctuations on Sentiments.
   * Effect of Spaces on Sentiments.
   * Effect of TypeCases on Sentiments.
   * Effect of TypeCases + Punctuations on Sentiments.
   * Effect of Degree Modifiers (Adjectives) on Sentiments.
   * Effect of Conjunctions on Sentiments.
   * Effect of Emojis and Emoticons on Sentiments.
   * Effect of Slangs on Sentiments.

<hr>

- ###### [Sentiment Analysis TextBlob:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/TextBlob-SentimentAnalysis)
   ###### This example demonstrates Sentiment Analysis using TextBlob Library. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/TextBlob-SentimentAnalysis)
   * Install TextBlob on Anaconda 
   * For each sentence, Textblobs returns Polarity and Subjectivity.  
   * **Polarity** is a float value within the range [-1.0 to 1.0] where 0 indicates neutral, +1 indicates a very positive sentiment and -1    represents a very negative sentiment.
   * **Subjectivity** is a float value within the range [0.0 to 1.0] where 0.0 is very objective and 1.0 is very subjective. Subjective  sentence expresses some personal feelings, views, beliefs, opinions, allegations, desires, beliefs, suspicions, and speculations where as Objective sentences are factual.
  ![image](https://user-images.githubusercontent.com/689226/50123800-29b44a80-0288-11e9-88ff-1fded1de452e.png)


<hr>

- ###### [ChatBot:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/ChatBot)
   ###### This example encapsulates ChatBot implementation using ChatterBot Library. [[Source Code]](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/ChatBot)
   * Install chatterbot library on Anaconda.
   * Prepare Chatbot.
   * Start Training the Chatbot.
   * To Test the Chatbot's Learning and Responding capabilities, issue get_response method with your question.
  ![image](https://user-images.githubusercontent.com/689226/50122157-4b5e0380-0281-11e9-8505-346ed795bec2.png)
