# Bangalore_House_Price_Prediction-Data_Science_Project
The main idea of this project is to predict the house price at various locations in Bangalore and to deploy the model in the flask server. The dataset is collected from [kaggle](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data). 

* First the data is preprocessed which includes data cleaning, feature engineering and outlier removal. This is done with the help of numpy and pandas libraries. (Detailed explanation is given in the Jupyter Notebook)
* Various Machine Learning models are applied to the preprocessed data which includes Multiple Linear Regression, Decision Tree Regression and Random Forest Regression to find the best suitable model.
* It is found that Multiple Linear Regression performs better compared to the other two with a decent accuracy of 78.31%. (Detailed explanation is given in the Jupyter Notebook)
* Then the model weights are stored in a pickle file so that it can be useful while building the flask server.
* A website is designed with the use of HTML5 and CSS3 and deployed it in a Flask server where python is used as the backend programming language. 
* To make the website public, the website is deployed in the AWS Elastic Bean Stalk. (It is the fastest and simplest way to get web applications up and running on AWS. Developers simply upload their application code and the service automatically handles all the details such as resource provisioning, load balancing, auto-scaling, and monitoring.)
