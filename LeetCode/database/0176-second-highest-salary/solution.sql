-- Write your PostgreSQL query statement below

select max(temp.salary) as SecondHighestSalary from(
    select *, dense_rank() over(order by e.salary DESC)rnk from employee e
) as temp
where rnk=2;
