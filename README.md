#Welcome to Heart Attack Estimator!  
Heart disease, which is one of the leading causes of mortality worldwide, calls for an early detection for effective intervention.   
In this project, We aim to build an explainable machine learning model to predict potential heart attacks and give users proper suggestions.   
Our dataset consists of 253,680 survey responses to the CDC’s The Behavioral Risk Factor Surveillance System in 2015.   
The responses were collected by phone calls.   
The interviews were done throughout the year, covering various days and times to capture a representative sample of the population.  

#Prediction with Basic Models  
The basic models we used in the project are decision trees, random forests, and XGBoost.    

#Prediction with Ensemble Learning  
In order to improve the general prediction ability of the model, we need to make many improvements other than simply XGBoost.   
Therefore, we employ ensemble learning.   
This method combines the predictions from multiple models to improve the overall accuracy and robustness of the predictions.   
The ensemble consists of three different base learners: XGBoost, LightGBM, and Random Forest, each chosen for their unique strengths in handling the prediction.

We use a `StandardScaler` to standardize the features of the training, validation, and test sets, ensuring that each feature contributes equally to the model's decision process. Following scaling, feature selection is the same as previous models.
We have tried models 

LightGBM is used as the main model for its efficiency with large datasets and high dimensionality. It is set up with `num_leaves` to control the complexity of the model, `min_data_in_leaf` to avoid overfitting on data with too many features, and both `feature_fraction` and `bagging_fraction` to randomly select a subset of features on each iteration, which adds more randomness to the model training process. This randomness helps improve model accuracy by reducing overfitting risk. Regularization is applied through `lambda_l1` and `lambda_l2` parameters, which are L1 and L2 regularization terms on weights, respectively, reducing overfitting and making the model more generalized.

As for hyperparameter optimization, Hyperopt is a powerful tool that employs Bayesian optimization techniques, specifically the Tree-structured Parzen Estimator (TPE) method, which intelligently explores the hyperparameter space and converges faster to the optimal solution compared to grid search or random search methods. The optimized hyperparameters can be found in the auxiliary picture.

All in all, the ensemble model effectively learns to best combine the predictions from the base models, adjusting weights to each base model's prediction based on their performance, which typically results in improved accuracy over any single model. The ensemble method leverages the strengths of each individual learner, while compensating for their weaknesses.


Website Demo
We developed a website demo to realize real time interface and heart attack prediction for users to estimate their health condition.   
In our website demo, we accomplished several functionalities:
1. Using our model to give predictions based on the user's inputs(See Figure A in Appendix).
2. Giving advice on health data such as BMI, providing dietary advice and exercise advice based on the health condition of different users.(See Figure B, C in Appendix)
Given our website is used more of a reference, we put a lot of healthy tips on daily lifestyle rather than giving serious medical diagnosis.

#How to run our website?
pip install requirements.txt
flask run
