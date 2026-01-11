# Fund Purchase Prediction Pipeline

## Overview
该子项目旨在预测银行存量客户在未来一个月内首次购买基金产品的概率。

## Key Features
1. **Sliding Window Aggregation**: 通过 `feature_engineering.py` 中的 `accum_n` 函数，自动将 M1/M3/M6 的交易数据进行时间窗口累加，捕捉长期资金流动趋势。
2. **Sparse Data Handling**: 使用 Pandas Pivot Table 处理高维稀疏的交易流水数据。
3. **Modeling**: 使用 XGBoost 进行二分类预测。

## File Description
* `fund_prediction_pipeline.ipynb`: 主流程代码。
* `feature_engineering.py`: 封装好的特征处理工具函数。