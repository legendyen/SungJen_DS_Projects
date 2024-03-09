**Project Description**

As more telecom companies emerge in the market, customers now have more options to choose from among the service providers. This selection process involves comparing prices, monthly usage, and coverage quality.
Consequently, telecom companies need to swiftly adjust their market positions to target the right customers for them and expand their user base.

As a marketing consultant team, we aim to receive monthly updates on all interactions between customers and their chosen service providers. This will enable us to predict which customers are most likely to churn and which may provide valuable connections to others. In doing so, they can become the focal point of our targeting network.

**Motivation**

1. Implement PySpark MLlib to build a scalable machine learning pipeline for data transformation, feature engineering, and model training.
2. Implement the Spark Streaming API to simulate streams for analyzing live data.
3. Implement the ROC curve for model comparison under different business contexts for cost-benefit analysis.
4. Use Matplotlib to visualize the analysis results.

**Data Source**

See attachments in the folder (telecom_data_new.csv, telecom_data_customer.csv)


**Analysis Result**
![image](https://github.com/legendyen/SungJen_DS_Projects/assets/20420765/0bf50734-7707-47d3-9870-4f25c2b2d9ec)

Considering the telecom market, as service providers, **we care more about false negatives since they are "expensive"—meaning that we would rather identify all the customers who will churn (at the cost of mistakenly classifying some customers who will stay anyway)**. In this case, our logistic regression model might have strictly better performance.

With similar AUCs for both models, although the random forest model correctly predicts more outcomes, **the logistic regression model might be better at distinguishing between the positive and negative classes when we consider a false positive rate acceptance threshold under 0.2.**
