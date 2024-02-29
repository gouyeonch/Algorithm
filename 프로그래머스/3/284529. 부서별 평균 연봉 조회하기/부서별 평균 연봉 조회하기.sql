-- 코드를 작성해주세요
with tbl as (select d.DEPT_ID, count(*) CNT, SUM(e.SAL) as SUMSAL
    from HR_DEPARTMENT d
        join HR_EMPLOYEES e
        on d.DEPT_ID = e.DEPT_ID
    group by d.DEPT_ID)

select d.DEPT_ID, d.DEPT_NAME_EN, ROUND(SUMSAL/CNT) as AVG_SAL
    from HR_DEPARTMENT d
        join tbl t
        on d.DEPT_ID = t.DEPT_ID
    order by AVG_SAL desc