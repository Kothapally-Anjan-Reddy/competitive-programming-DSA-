CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
        SELECT temp.Salary from (
            select *, dense_rank() over (order by e.Salary DESC)as rnk from Employee e
        ) as temp
        where rnk=N limit 1
        
  );
END;
$$ LANGUAGE plpgsql;
