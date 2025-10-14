

# 🎮 Video Game Sales Prediction Model

## 📘 Overview

This project uses machine learning regression techniques to **predict global video game sales** based on features such as platform, genre, publisher, and critic scores.
By analyzing historical sales data, the model helps forecast how well future games might perform in the market.

---

## 🧩 Dataset

* **Source:** [Kaggle - Video Game Sales Dataset (VGChartz)](https://www.kaggle.com/datasets/gregorut/videogamesales)
* **Features:**
  `Name`, `Platform`, `Year_of_Release`, `Genre`, `Publisher`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`
* **Target Variable:** `Global_Sales`

---

## ⚙️ Project Workflow

1. **Data Collection & Cleaning**

   * Handled missing values and data type conversions
   * Encoded categorical variables (Platform, Genre, Publisher)

2. **Exploratory Data Analysis (EDA)**

   * Visualized sales trends by year, region, and genre
   * Checked correlations between variables

3. **Model Building**

   * Tested models: Linear Regression, Random Forest, XGBoost
   * Evaluated with MAE, RMSE, and R² Score

4. **Optimization**

   * Feature engineering (interaction features, scaling)
   * Hyperparameter tuning using GridSearchCV

5. **Prediction**

   * Used the optimized model to forecast sales of upcoming or new games

---

## 📊 Evaluation Metrics

* **Mean Absolute Error (MAE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**

---

## 🌍 Real-World Applications

* 🎮 **Game Developers:** Predict sales before release to plan production and budgets
* 💼 **Marketers:** Forecast demand and optimize ad campaigns
* 💰 **Publishers & Investors:** Identify high-potential titles for funding decisions

---

## 🚀 Tech Stack

* **Python**
* **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
* **Scikit-learn**, **XGBoost**

---

## 🧠 Author

**Marvie Cephas**
📧 Contact: [[marviecephas@gmail.com](mailto: marviecephas@gmail.com)]
💻 *“Data-driven insights for smarter game development.”*

---
