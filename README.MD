This repository contains self-contained NLP examples.

### Table of Contents
- <a href='#word-vector'>Word-Vector</a> 
  - <a href='#word-vector-spacy'>WordVector-Spacy</a> 
  - <a href='#word-vector-gensim'>WordVector-Gensim</a> 
- <a href='#text-wrangling'>TextWrangling</a> 
- <a href='#spam-detection'>SpamDetection</a> 
- <a href='#sentiment-analysis'>Sentiment Analysis</a>
  - <a href='#sentiment-analysis-spacy'>SentimentAnalysis-Spacy</a>
  - <a href='#sentiment-analysis-vader'>SentimentAnalysis-VADER</a>
  - <a href='#sentiment-analysis-textblob'>SentimentAnalysis-TextBlob</a>
- <a href='#chatbot'>ChatBot</a>  
  
<hr>
 

- ###### [Word Vector Spacy:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/blob/Word-Vector/Spacy-Word2Vec.ipynb)
  * Install Spacy on Anaconda:
![image](https://user-images.githubusercontent.com/689226/50120718-83af1300-027c-11e9-85c1-7bacb4c129db.png)
![image](https://user-images.githubusercontent.com/689226/50121286-49df0c00-027e-11e9-9ab2-5a3e5875008b.png)
![image](https://user-images.githubusercontent.com/689226/50174045-228c4b80-031f-11e9-9546-c189b7f0acf8.png)
  * Computes similarity among all tokens' combinations
 

<hr> 
  
- ###### [Word Vector Gensim:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/blob/Word-Vector/Gensim-Word2Vec.ipynb)
  * Install Gensim on Anaconda:
![image](https://user-images.githubusercontent.com/689226/50122009-bbb85500-0280-11e9-926b-7510761bcff8.png)
  * Compute similarity between all tokens
  
<hr>

- ###### [Text Wrangling:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/TextWrangling)
  * Install Spacy on Anaconda [Refer Above]
  * Convert sentence into Lemma
  * Removal of Pronoun 
  * Removal of Stop Words
  * Removal of Punctuations
  * Selecting Nouns
  * Word count and Frequency
  * Converting into Text -> List of Sentences -> List of Clean Sentences
  * Bag Of Words (Sentences)
  * Bag Of Words (File)
  * TF-IDF (Sentences)
  * TF-IDF (File)

<hr>

- ###### [Spam Detection](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SpamDetection) 
   * Load the data [spam.csv]
   * Removal of unwanted columns
   * Break the complete dataset into data(for training and validation) + untouched data
   * Replacing Categorical Feature into Numerical Feature
   * Split the data(for training and validation) as train_X, test_X, train_Y, test_
   * Apply CountVectorizer on train_X
   * Apply CountVectorizer on test_X
   * Apply ML Modeling with MultinomialNB
   * Make Predictions. 
   
   
<hr>

- ###### [Sentiment Analysis Spacy:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/Spacy-TextClassification-SentimentAnalysis)
   * Install Spacy on Anaconda [Refer Above]
   * Clean Sentences
   * Tokenize
   * Vectorize
   * Classify
   * Predict the Sentiments.

<hr>

- ###### [Sentiment Analysis VADER:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/SentimentAnalysis/VADER-SentimentAnalysis)
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
   * Install TextBlob on Anaconda 
   * For each sentence, Textblobs returns Polarity and Subjectivity.  
   * **Polarity** is a float value within the range [-1.0 to 1.0] where 0 indicates neutral, +1 indicates a very positive sentiment and -1    represents a very negative sentiment.
   * **Subjectivity** is a float value within the range [0.0 to 1.0] where 0.0 is very objective and 1.0 is very subjective. Subjective  sentence expresses some personal feelings, views, beliefs, opinions, allegations, desires, beliefs, suspicions, and speculations where as Objective sentences are factual.
  ![image](https://user-images.githubusercontent.com/689226/50123800-29b44a80-0288-11e9-88ff-1fded1de452e.png)


<hr>

- ###### [ChatBot:](https://github.com/rahulvaish/NaturalLanguageProcessing-Python/tree/ChatBot)
   * Install chatterbot library on Anaconda.
   * Prepare Chatbot.
   * Start Training the Chatbot.
   * To Test the Chatbot's Learning and Responding capabilities, issue get_response method with your question.
  ![image](https://user-images.githubusercontent.com/689226/50122157-4b5e0380-0281-11e9-8505-346ed795bec2.png)
