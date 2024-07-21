# Credit Card Fraud Detection

This project focuses on analyzing a dataset of credit card transactions and detecting credit card fraud. It includes data preprocessing, model training, and serving the model via a FastAPI application. The focus is on prioritizing precision for non-fraudulent transactions and recall for fraudulent transactions, with models being fine-tuned accordingly.

The dataset used in this project is sourced from Kaggle and contains credit card transactions labeled as fraudulent or non-fraudulent. It consists of various features including transaction amount, type of transaction (online or chip and pin), time of transaction, etc.  

## Repository Structure:

```
.
├── README.md
├── data
│   └── card_transdata.csv
├── fastapi-rf-clf
│   ├── Dockerfile
│   ├── main.py
│   └── model
│       └── rf_clf.pkl
├── models
│   └── rf_clf.pkl
└── notebooks
    └── credit-card-fraud-detection.ipynb
```

## Detailed Description:

1. **README.md**

- This file provides an overview of the project, instructions for setting up and running the project, and descriptions of each component.

2. **data/card_transdata.csv**

- This CSV file contains the credit card transaction data used for training and testing the fraud detection model. It includes features extracted from transactions and a label indicating whether each transaction is fraudulent.

3. **fastapi-rf-clf**

- This directory contains the FastAPI application that serves the fraud detection model.

  - `Dockerfile` - A Dockerfile to containerize the FastAPI application for easy deployment.
  - `main.py` - The main Python script that defines the FastAPI application. It loads the trained Random Forest model and provides an endpoint for assessing a transaction as being fraudulent (1) or non-fraudulent (0).
  - `model/rf_clf.pkl` - The serialized Random Forest model used by the FastAPI application for making predictions.

4. **models**

- This directory contains chosen models trained and evaluated in the `notebooks/credit-card-fraud-detection.ipynb` notebook.

5. **notebooks/credit-card-fraud-detection.ipynb**

### Notebook Structure:

#### Dataset Overview & Clean-up
- Dataset Overview
- Dataset Clean-up

#### Exploratory Data Analysis
- Comparing dataset values for fraudulent and non-fraudulent transactions
- Checking features correlation with the target (fraud)
- Comparing security of chip and pin transactions
- Comparing fraudulent and non-fraudulent cases for online transactions
- Checking feature importance

#### Building And Evaluating Models
- Logistic Regression
- Support Vector Machines (SVC)
- DecisionTreeClassifier
- RandomForestClassifier


## Running the FastAPI Application

1. Build the Docker image:
```bash
docker build -t fastapi-rf-clf ./fastapi-rf-clf
```

2. Run the Docker container:
```bash
docker run -d -p 5000:5000 --name fastapi-rf-clf fastapi-rf-clf
```
3. The API will be available at http://localhost:5000. You can access the Swagger documentation at http://localhost:5000/docs.

## Usage

### API Endpoint

- `POST /predict`
  - Input: JSON object containing list of transactions. Each transaction containing transaction features values:
<pre style="font-size: 12px;">
    {
      "inputs": [
      [&lt;distance_from_home>, &lt;distance_from_last_transaction>, &lt;ratio_to_median_purchase_price>, 
      &lt;repeat_retailer>, &lt;used_chip>, &lt;used_pin_number>, &lt;online_order>]
      ]
    }
</pre>
  - Output: JSON object with the prediction result (0 - non-fraudulent, 1 - fraudulent).

### Example Request
```bash
curl -X POST "http://localhost:5000/predict" -H "Content-Type: application/json" -d '{
  "inputs": [
  [131.56029999005267, 1.8798586040689265, 0.5761089559751786, 1, 0, 0, 1],
  [130.34704276433706, 0.4231516875330257, 0.1563897314923115, 1, 0, 0, 1],
  [2.7987007888209297, 2.308785475162721, 6.689793457624547, 1, 0, 0.0, 1]
  ]
}'
```

### Example Response
```bash
{
    "predictions":[1,1,1]
}
```
