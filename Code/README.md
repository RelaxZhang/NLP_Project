## NLP Project

### Code Folder (Including Self-Implemented Function Packages and Jupyter Notebooks)

#### Data_Exploration.ipynb - Run through all chunks to obtain information of the given data (train, dev, test, evi)

#### FineTune_BERT.ipynb - Preliminary version of fine-tune bert model implemented based on the bert tutorial
#### (*) Not Sugeest to run the training part since it takes 9 hours to process with CPU in local machine or consume a lot computing unit on colab

#### LSA_TFIDF_NNM.ipynb - Further investigation of the TF-IDF method by adding the Latent Semantic analysis process to reduce the matrix dimension
#### (*) The performance is bad since the reduced dimension has contain informative data and the manully set dimension is ambiguous

#### PreTrained_BERT.ipynb - Apply pre-trained bert model to embed the claim and evidence sentence for further computing their cosine-similarity
#### (*) Run all the chunks from the begining until 'Task 2' could obtain a 3NN unsupervised evidence retrieval model (underperform)

#### Pure_BoW_NNM.ipynb - Apply the BoW to embed te claim and evidence sentence for computing the cosine-similarity in 3NN model for prelimiarny test
#### (*) Run all the chunks from the begining until 'Task 2' could obtain a 3NN unsupervised evidence retrieval model (less optimal)

#### Pure_Doc2Vec_NMM.ipynb - Apply the doc2vec to embed the claim and evidence sentence for computing the cosine-similarity in 3NN model
#### (*) Run all the chunks from the begining until 'Task 2' could obtain a 3NN unsupervised model (Poor Performance due to low mapping dimension)

#### Pure_TFIDF_NNM.ipynb - Apply the TF-IDF method to embed all claim and evidence and use them for computing cosine-similarity in 3NN model
#### (*) Run all chunks until 'Task 2' and obtain the local optimal model among the four main types of embedding methods
#### (*) Since TF-IDF performs well, it worths further investigation

#### Topic_TFIDF_NNK.ipynb - Adding the topic filtering before embedding the claim and evidence
#### Apply the weighted voting method along with kNN logic to obtain the classification of Task 2
#### (*) Run all the chunk to obtain the result for task 1 and 2 (the F-score is improved, while the accuracy can be further improved)

#### Topic_TFIDF_NNM_dev.ipynb - Code for obtaining hyper-parameter value by evaluting the performance with development set
#### (*) Run through all the code block could help to obtain the plots for Number of topics, Number of Neighbour tuning

#### Topic_TFIDF_FINAL.ipynb - Code with tuned hyper-parameter for task 1 and various of classification method for task 2
#### (*) Run the code until Task 2 can help to obtain the current optimal task 1 result
#### (*) For task 2, only run a block after task 1 each of the time to obtain a type of task 2 model's result
#### (*) Candidate model for task 2: Majority voting, Weighted Voting, SVM, FNN based on the embedded concat claim-evidence sentence

#### nlp_function.py - Python file that include the self-implemented function for Jupyter Notebook's usage