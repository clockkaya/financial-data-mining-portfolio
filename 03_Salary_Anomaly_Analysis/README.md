# Salary Anomaly Detection & Potential Investor Mining

## Overview
针对银行代发工资数据进行清洗与挖掘，目的是识别数据录入错误（异常值）并挖掘高潜理财客户。

## Key Steps
1. **Outlier Removal**: 识别并处理单月 >100W 的异常工资流水（通常为数据录入错误），使用均值插补。
2. **Statistical Analysis**: 分析薪资发放的季节性波动（如1月年终奖效应）。
3. **Lead Generation**: 结合用户的理财持仓数据，筛选 "高薪资 + 低理财渗透" 的客户作为营销白名单。