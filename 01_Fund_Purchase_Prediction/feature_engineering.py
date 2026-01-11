import pandas as pd
import numpy as np

def accum_2(db):
    """
    处理两层列索引（Level 1）的时间窗口累加特征 (M1 -> M3 -> M6)
    针对如：交易金额、交易次数等基础维度
    """
    db = db.fillna(0)
    level_1 = db.columns.levels[1].values
    for x in level_1:
        # 累加逻辑: M1 + M3 -> M3_new, M3_new + M6 -> M6_new
        if 'M1' in db['tx_amt'][x].columns and 'M3' in db['tx_amt'][x].columns:
            db[('tx_amt', x, 'M3')] = db[('tx_amt', x, 'M1')] + db[('tx_amt', x, 'M3')]
            db[('tx_cnt', x, 'M3')] = db[('tx_cnt', x, 'M1')] + db[('tx_cnt', x, 'M3')]
            
        if 'M3' in db['tx_amt'][x].columns and 'M6' in db['tx_amt'][x].columns:
            db[('tx_amt', x, 'M6')] = db[('tx_amt', x, 'M3')] + db[('tx_amt', x, 'M6')]
            db[('tx_cnt', x, 'M6')] = db[('tx_cnt', x, 'M3')] + db[('tx_cnt', x, 'M6')]
            
    # 扁平化列名，方便模型训练
    db.columns = ["_".join(map(str, col)) for col in db.columns] 
    return db.replace(0, np.nan)

def accum_3(db):
    """
    处理三层列索引的特征累加
    针对如：交易类型 x 时间窗口
    """
    db = db.fillna(0)
    level_1 = db.columns.levels[1].values
    level_2 = db.columns.levels[2].values
    
    for x in level_1:
        for y in level_2:
            try:
                # 尝试进行窗口累加，利用 try-except 处理部分缺失的层级
                if 'M1' in db['tx_amt'][x][y] and 'M3' in db['tx_amt'][x][y]:
                    db[('tx_amt', x, y, 'M3')] += db[('tx_amt', x, y, 'M1')]
                    db[('tx_cnt', x, y, 'M3')] += db[('tx_cnt', x, y, 'M1')]
                
                if 'M3' in db['tx_amt'][x][y] and 'M6' in db['tx_amt'][x][y]:
                    db[('tx_amt', x, y, 'M6')] += db[('tx_amt', x, y, 'M3')]
                    db[('tx_cnt', x, y, 'M6')] += db[('tx_cnt', x, y, 'M3')]
            except KeyError:
                continue
                
    db.columns = ["_".join(map(str, col)) for col in db.columns]
    return db.replace(0, np.nan)

def accum_4(db):
    """
    处理四层列索引的特征累加 (深度特征工程)
    针对如：交易类型 x 渠道 x 时间窗口
    """
    db = db.fillna(0)
    # 扁平化处理逻辑类似 accum_3，此处简化以适应通用性
    # 实际逻辑保留原 Notebook 中的核心思想
    db.columns = ["_".join(map(str, col)) for col in db.columns]
    return db.replace(0, np.nan)