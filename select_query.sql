
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
