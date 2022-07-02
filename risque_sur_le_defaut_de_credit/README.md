# Home Credit Default Risk

### Issue : *Predicting the risk of a bank making loans that will not be repaid* 

## Objectives
  
  - accuracy 70%
  - Roc_Auc_Score, Matrice de confusion
  - Minimise false positif ( that is to say the predictions paid off which are in reality not paid off )

## Machine learning issue

The dataset provided is an imbalanced dataset. Thus, we would need to address this imbalance wherever required, as some ML algorithms are sensitive to data imbalance for this use Undersampling.

We can identify that it is a Supervised Learning Classification problem, which contains the training data points along with their Class Labels. Here the Class Labels represent whether a given applicant is a Defaulter or not. Thus, for a given application of a client, using the given features, we have to predict the Class Label associated with that client.

## Classification models used

  - Linear Regression
  - Decision Tree
  - Random Forest Classifier
  - XGBoost

## Evaluation metricss

  - Accuracy
  - Precision
  - Recall
  - F1 score
  - AUC ROC Curve
  - Confusion matrix

## Get Data

https://www.kaggle.com/c/home-credit-default-risk/data

## Data context

**application_{train|test}.csv**
This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET).
Static data for all applications. One row represents one loan in our data sample.

**bureau.csv**
All client's previous credits provided by other financial institutions that were reported to Credit Bureau (for clients who have a loan in our sample).
For every loan in our sample, there are as many rows as number of credits the client had in Credit Bureau before the application date.

**bureau_balance.csv**
Monthly balances of previous credits in Credit Bureau.
This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample * # of relative previous credits * # of months where we have some history observable for the previous credits) rows.

**POS_CASH_balance.csv**
Monthly balance snapshots of previous POS (point of sales) and cash loans that the applicant had with Home Credit.
This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credits * # of months in which we have some history observable for the previous credits) rows.

**credit_card_balance.csv**
Monthly balance snapshots of previous credit cards that the applicant has with Home Credit.
This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credit cards * # of months where we have some history observable for the previous credit card) rows.

**previous_application.csv**
All previous applications for Home Credit loans of clients who have loans in our sample.
There is one row for each previous application related to loans in our data sample.

**installments_payments.csv**
Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample.
There is a) one row for every payment that was made plus b) one row each for missed payment.
One row is equivalent to one payment of one installment OR one installment corresponding to one payment of one previous Home Credit credit related to loans in our sample.

**HomeCredit_columns_description.csv**
This file contains descriptions for the columns in the various data files.

![alt text](https://storage.googleapis.com/kaggle-media/competitions/home-credit/home_credit.png)

### Resources :

https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction

https://www.kaggle.com/willkoehrsen/introduction-to-manual-feature-engineering

https://www.kaggle.com/willkoehrsen/introduction-to-manual-feature-engineering-p2

https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection

https://www.kaggle.com/willkoehrsen/intro-to-model-tuning-grid-and-random-search
