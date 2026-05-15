-- Write your query below

select distinct(name) from customers left outer join orders on customers.id=orders.customer_id where customer_id is null
