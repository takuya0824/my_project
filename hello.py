import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# サンプルデータの作成
data = {
    'employee_id': range(1001, 1011),  # 従業員ID
    'name': [
        '山田太郎', '鈴木花子', '佐藤一郎', '田中美咲', 
        '中村健一', '小林裕子', '加藤誠', '渡辺春香', 
        '伊藤光男', '高橋恵子'
    ],
    'department': [
        '営業部', '人事部', '技術部', '営業部',
        '技術部', '財務部', '営業部', '人事部',
        '技術部', '財務部'
    ],
    'position': [
        '課長', '主任', '部長', '社員',
        '主任', '課長', '社員', '社員',
        '課長', '主任'
    ],
    'salary': [
        350000, 280000, 450000, 250000,
        300000, 380000, 250000, 250000,
        400000, 290000
    ],
    'hire_date': [
        '2015-04-01', '2018-04-01', '2010-04-01', '2020-04-01',
        '2017-04-01', '2016-04-01', '2021-04-01', '2019-04-01',
        '2012-04-01', '2018-04-01'
    ],
    'email': [
        'yamada.t@example.com', 'suzuki.h@example.com', 'sato.i@example.com',
        'tanaka.m@example.com', 'nakamura.k@example.com', 'kobayashi.y@example.com',
        'kato.m@example.com', 'watanabe.h@example.com', 'ito.m@example.com',
        'takahashi.k@example.com'
    ]
}

# DataFrameの作成
df = pd.DataFrame(data)

# Excelファイルとして保存
df.to_excel('employee_data.xlsx', index=False)

# SELECT文の生成
select_sql = """
SELECT 
    employee_id AS 従業員ID,
    name AS 氏名,
    department AS 部署,
    position AS 役職,
    salary AS 給与,
    hire_date AS 入社日,
    email AS メールアドレス
FROM 
    employees
WHERE 
    department = '営業部'
ORDER BY 
    salary DESC;
"""

# SQLファイルとして保存
with open('select_query.sql', 'w', encoding='utf-8') as f:
    f.write(select_sql)