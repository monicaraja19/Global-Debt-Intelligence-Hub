-- 1.Retrieve all distinct country names from the dataset.
select distinct(country_name) as distinct_country_name  from countries;
-- 2.Count the total number of countries available.
select count(*) as total_number_of_countries from countries;
-- 3.Find the total number of indicators present.
select count(*) as total_number_of_indicators from indicators;
-- 4.Display the first 10 records of the dataset.
select * from countries_debt limit 10;
-- 5.Calculate the total global debt.
select sum(debt_amount) as total_global_debt from countries_debt;
-- 6.List all unique indicator names.
select distinct(indicator_name) as distinct_indicator_name  from indicators;
-- 7.Find the number of records for each country.
select c.country_code,c.country_name,count(*) as number_of_debts from countries_debt cb join countries c on c.country_code = cb.country_code
	group by c.country_code,c.country_name;
-- 8.Display all records where debt is greater than 1 billion USD.
select * from countries_debt where debt_amount > 1000000000;
-- 9.Find the minimum, maximum, and average debt values.
select min(debt_amount) as minimun_debt_amount,max(debt_amount) as maximum_debt_amount,avg(debt_amount) as average_debt_amount 
	from countries_debt;
-- 10.Count total number of records in the dataset.
select count(*) as total_debts_globally from countries_debt;

-- 11.Find the total debt for each country.
select c.country_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by cb.country_code,c.country_name order by c.country_name;
-- 12.Display the top 10 countries with the highest total debt.
select c.country_name, sum(cb.debt_amount) as total_debt from countries_debt cb join countries c on cb.country_code = c.country_code 
	group by cb.country_code,c.country_name order by total_debt desc limit 10;
-- 13.Find the average debt per country.
select c.country_name,avg(cb.debt_amount) as average_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by cb.country_code,c.country_name order by c.country_name;
-- 14.Calculate total debt for each indicator.
select i.indicator_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join indicators i on cb.indicator_code = i.indicator_code
	group by cb.indicator_code,i.indicator_name order by i.indicator_name;
-- 15.Identify the indicator contributing the highest total debt.
select i.indicator_code,i.indicator_name,i.short_definition,sum(cb.debt_amount) total_debt_amount from countries_debt cb join indicators i 
	on cb.indicator_code = i.indicator_code group by i.indicator_code,i.indicator_name,i.short_definition order by total_debt_amount desc limit 1;
-- 16.Find the country with the lowest total debt.
select c.country_code,c.country_name,c.currency_unit,c.region,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by c.country_code,c.country_name,c.currency_unit,c.region order by total_debt_amount limit 1;
-- 17.Calculate total debt for each country and indicator combination.
select cb.country_code,c.country_name,cb.indicator_code,i.indicator_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	join indicators i on cb.indicator_code = i.indicator_code group by cb.country_code,cb.indicator_code,c.country_name,i.indicator_name order by c.country_name,i.indicator_name;
-- 18.Count how many indicators each country has.
select cb.country_code,c.country_name,count(distinct cb.indicator_code) as total_indicators from countries_debt cb join countries c on c.country_code = cb.country_code
	group by cb.country_code,c.country_name order by cb.country_code;
-- 19.Display countries whose total debt is above the global average.
select c.country_code,c.country_name,c.currency_unit,c.region,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by c.country_code,c.country_name,c.currency_unit,c.region having sum(cb.debt_amount) > (select avg(debt_amount) from countries_debt);
-- 20.Rank countries based on total debt (highest to lowest).
select dense_rank() over(order by sum(cb.debt_amount) desc) as countries_rank_on_debt_amount,c.country_code,c.country_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb 
	join countries c on c.country_code = cb.country_code group by c.country_code,c.country_name order by total_debt_amount desc;

-- 21.Find the top 5 indicators contributing most to global debt.
select i.indicator_code,i.indicator_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join indicators i on cb.indicator_code = i.indicator_code
	group by cb.indicator_code,i.indicator_name order by total_debt_amount desc limit 5;
-- 22.Calculate percentage contribution of each country to total global debt.
select c.country_code,c.country_name,sum(cb.debt_amount) as total_debt_amount_of_country,round((sum(cb.debt_amount)/(select sum(debt_amount) from countries_debt))*100,2) as percentage_contribution_in_total_debt 
	from countries_debt cb join countries c on c.country_code = cb.country_code group by c.country_code,c.country_name order by percentage_contribution_in_total_debt;
-- 23.Identify the top 3 countries for each indicator based on debt.
select * from (select cb.indicator_code,c.country_name,sum(cb.debt_amount) as total_debt_amount,dense_rank() over 
			   (partition by cb.indicator_code order by sum(cb.debt_amount) desc) as country_rank from countries_debt cb join countries c on cb.country_code = c.country_code
		       group by cb.indicator_code,c.country_name) as ranked_countrie where country_rank <= 3 order by indicator_code;
-- 24.Find the difference between maximum and minimum debt for each country.
select c.country_code,c.country_name,(max(debt_amount) - min(debt_amount)) as diff_btw_max_min_debt_amount from countries_debt cb join
	countries c on c.country_code = cb.country_code group by c.country_code,c.country_name;
-- 25.Create a view for the top 10 countries with highest debt.
create view top_10_highest_debt_countries as select c.country_code,c.country_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb
	join countries c on cb.country_code = c.country_code group by c.country_code,c.country_name order by total_debt_amount desc limit 10;
select * from top_10_highest_debt_countries;
-- 26.Categorize countries into:High Debt Medium Debt Low Debt (based on thresholds)
select c.country_code,c.country_name,sum(cd.debt_amount) as total_debt_amount,case when sum(cd.debt_amount) <= 5903333333333.33 then 'Low Debt'
	when sum(cd.debt_amount) <= 12251666666666.66 then 'Medium Debt' else 'High Debt' end as debt_category from countries_debt cd join countries c
    on cd.country_code = c.country_code group by c.country_code,c.country_name order by total_debt_amount desc;
-- 27.Use window functions to calculate cumulative debt per country.
select cb.country_code,cb.indicator_code,cb.year,cb.debt_amount,sum(cb.debt_amount) over(partition by cb.country_code order by cb.year,cb.indicator_code) AS cumulative_debt_amount
	from countries_debt cb order by cb.country_code,cb.year,cb.indicator_code;
-- 28.Find indicators where average debt is higher than overall average debt.
select i.indicator_code,i.indicator_name,i.short_definition,avg(cb.debt_amount) average_debt_amount from countries_debt cb join indicators i 
	on cb.indicator_code = i.indicator_code group by i.indicator_code,i.indicator_name,i.short_definition having avg(cb.debt_amount) > (
	select avg(debt_amount) from countries_debt) order by i.indicator_code;
-- 29.Identify countries contributing more than 5% of global debt.
select * from (select c.country_code,c.country_name,sum(cb.debt_amount) as total_debt_amount,round((sum(cb.debt_amount) * 100.0)/(select sum(debt_amount) from countries_debt),2) AS contribution_percentage_on_total_debt
    from countries_debt cb join countries c on cb.country_code = c.country_code group by c.country_code,c.country_name) t
	where contribution_percentage_on_total_debt > 5 order by contribution_percentage_on_total_debt desc;
-- 30.Find the most dominant indicator (highest contribution) for each country.
select c.country_code,c.country_name,t.indicator_code,i.indicator_name,t.total_debt_amount from (select country_code,indicator_code,sum(debt_amount) as total_debt_amount,
	row_number() over (partition by country_code order by sum(debt_amount) desc) as rn from countries_debt group by country_code,indicator_code) t	
	join countries c on c.country_code = t.country_code join indicators i on i.indicator_code = t.indicator_code where rn = 1 order by c.country_name;