# Customer Segmentation Analysis

## Overview
基于客户的 **账户余额(acct_bal)** 和 **交易流量(tx_amt_vol)** 两个核心维度，利用 K-Means 算法对客户进行价值分层。

## Methodology
1. **Data ETL**: 从 Oracle 聚合客户日均余额与交易量。
2. **Normalization**: 使用 L2 正则化处理数据，消除量纲影响。
3. **K-Means**: 使用手肘法 (Elbow Method) 确定最佳聚类数 K=6。
4. **Insight**: 识别出高净值低活跃、低净值高活跃等不同客群，用于精准营销。