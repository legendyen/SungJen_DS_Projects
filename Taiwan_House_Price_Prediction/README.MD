# Taiwan House Price Prediction

## Project Overview

This project aims to develop a predictive model for house prices in Taiwan based on several real-world factors such as proximity to public transportation, number of nearby convenience stores, and house age. The model helps to understand how these factors influence housing prices, assisting potential home buyers in better decision-making and financial planning.

## Dataset

The dataset consists of 414 real-world observations of house prices in Taiwan, with the following key features:
1. **Distance to MRT station (dist_to_mrt_m)**: Distance to the nearest MRT station in meters.
2. **Number of convenience stores (n_convenience)**: The number of convenience stores within a certain radius.
3. **House age (house_age_years)**: The age of the house in years, categorized into ranges.
4. **Price per square meter (price_twd_msq)**: The price per square meter of the house in New Taiwan Dollars (TWD).

## Project Goals

1. **Predictive Modeling**: Develop a machine learning model that predicts house prices based on the features provided.
2. **Feature Engineering**: Improve model performance by applying feature engineering techniques.
3. **Algorithm Comparison**: Compare the performance of different algorithms, including Linear Regression and Random Forest.
4. **Model Optimization**: Use ensemble methods and hyperparameter tuning to enhance the model’s accuracy and robustness.

## Methodology

### 1. Exploratory Data Analysis (EDA)
We first explored the dataset to understand the distribution of house prices and relationships between features. Some key insights:
- The closer the house is to the MRT station, the higher the price tends to be.
- A higher number of convenience stores within the vicinity also corresponds to higher house prices.

### 2. Feature Engineering
To improve model performance, feature engineering techniques were applied:
- **Categorization of house age**: House age was categorized into specific ranges (e.g., 0-15 years, 15-30 years, etc.) to provide more meaningful insights.
- **Scaling of numerical features**: Features such as distance to MRT were scaled to improve the performance of certain algorithms like Linear Regression.

### 3. Algorithms Used
#### 1. **Linear Regression**:
- A basic regression model was implemented to predict house prices based on the features. While this model provided a baseline for performance, it struggled to capture non-linear relationships between features and price.

#### 2. **Random Forest**:
- A Random Forest model was applied to capture more complex relationships between features. This ensemble method significantly improved accuracy by leveraging multiple decision trees and averaging predictions.

### 4. Model Performance

- **Linear Regression**:
  - Performance: The model had limited success, achieving an R-squared score of approximately 0.6, meaning it could explain around 60% of the variance in house prices.
  - Weakness: It failed to capture the non-linear relationships between features like distance to MRT and house prices.
  
- **Random Forest**:
  - Performance: The Random Forest model achieved a significantly higher R-squared score of approximately 0.85, showing its ability to better model the complex relationships between features.
  - Strength: By utilizing ensemble learning, Random Forest outperformed Linear Regression in both accuracy and robustness.

### 5. Hyperparameter Tuning and Cross-Validation
- Hyperparameters such as the number of trees in Random Forest and the depth of each tree were fine-tuned to further improve model performance.
- Cross-validation was used to ensure that the model generalizes well to unseen data.

## Results and Inference

- The **Random Forest model** was the most successful in predicting house prices, with an R-squared score of 0.85.
- Feature importance analysis from the Random Forest model revealed that **distance to MRT station** and the **number of nearby convenience stores** were the most significant factors affecting house prices.
- **Linear Regression** provided a reasonable baseline but was outperformed by Random Forest due to its inability to capture complex, non-linear relationships.

## Conclusion

This project demonstrates that housing prices in Taiwan are influenced by factors such as proximity to public transportation and availability of convenience stores. Random Forest proved to be the most effective model for predicting house prices, outperforming Linear Regression by a significant margin. Feature engineering and hyperparameter tuning played a key role in improving the model's performance.

## Future Work

- **Incorporate additional features**: Including other variables such as neighborhood crime rates or school quality could improve predictions.
- **Deep Learning models**: Experimenting with neural networks or deep learning techniques to see if they can further enhance prediction accuracy.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>

