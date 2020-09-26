# AdmissionPrediction

Hello all. I will be applying different Regression algorithms on the Admission Prediction dataset and learn more about their perfromance. The dataset is from Kaggle and the link for the same is https://www.kaggle.com/mohansacharya/graduate-admissions

Context
This dataset is created for prediction of Graduate Admissions from an Indian perspective.

Content
The dataset contains several parameters which are considered important during the application for Masters Programs.
The parameters included are :

1) GRE Scores ( out of 340 )
2) TOEFL Scores ( out of 120 )
3) University Rating ( out of 5 )
4) Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
5) Undergraduate GPA ( out of 10 )
6) Research Experience ( either 0 or 1 )
7) Chance of Admit ( ranging from 0 to 1 )

The Chance of Admit is the dependent variable that we will be predicting

Day 1 -> Applied a Simple Linear Regression model on the dataset and found the r2_score to be 0.81 and made a webapp using Flask , deployed it in Heroku.                           
Day 2 -> Applied a Lasso,Ridge,ElasticNet models on the dataset and found the r2_score is almost similar to that of Simple Linear Regression.                                       


