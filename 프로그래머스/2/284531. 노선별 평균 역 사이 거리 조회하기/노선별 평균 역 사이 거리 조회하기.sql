-- 코드를 작성해주세요
select 
    ROUTE, 
    CONCAT(ROUND(sum(D_BETWEEN_DIST),1),"km") as TOTAL_DISTANCE,
    CONCAT(ROUND(sum(D_BETWEEN_DIST)/count(*),2),"km") as AVERAGE_DISTANCE
    
    from SUBWAY_DISTANCE
    group by ROUTE
    order by ROUND(sum(D_BETWEEN_DIST),1) desc