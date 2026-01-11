# Financial Data Mining & Prediction Portfolio

## 📖 Introduction
本项目集合了我在金融领域的三个核心数据挖掘实战案例，涵盖了从 **Oracle数据库取数**、**复杂时序特征工程** 到 **XGBoost/K-Means 建模** 的全流程。项目展示了如何处理高维稀疏的金融交易数据，并将其转化为可落地的业务预测模型。

## 🛠 Tech Stack
* **Languages:** Python 3.8+
* **Data Processing:** Pandas, NumPy, SQLAlchemy
* **Machine Learning:** XGBoost, Scikit-learn (K-Means, PCA)
* **Database:** Oracle (cx_Oracle)
* **Visualization:** Matplotlib, PyEcharts

## 📂 Project Structure
* **01_Fund_Purchase_Prediction/**: 基金购买行为预测（核心项目）。包含特征工程管道封装和 XGBoost 分类模型。
* **02_Customer_Segmentation/**: 基于交易行为的客户分群。使用 K-Means 进行客户价值分层。
* **03_Salary_Anomaly_Analysis/**: 薪资数据异常检测。基于统计学规则清洗代发工资数据。

## 🚀 Setup
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```