from DatabaseConnectionAndQuery.DataBaseConnection import getDBConnection 
import pandas as pd

#getting database connection
db_engine = getDBConnection()

#Basic query
def show_basic_query():
    query_result_1 = pd.read_sql("select distinct(country_name) as distinct_country_name  from countries", db_engine)
    query_result_2 = pd.read_sql("select count(*) as total_number_of_countries from countries", db_engine)
    query_result_3 = pd.read_sql("select count(*) as total_number_of_indicators from indicators", db_engine)
    query_result_4 = pd.read_sql("select * from countries_debt limit 10", db_engine)
    query_result_5 = pd.read_sql("select sum(debt_amount) as total_global_debt from countries_debt", db_engine)
    query_result_6 = pd.read_sql("select distinct(indicator_name) as distinct_indicator_name  from indicators", db_engine)
    query_result_7 = pd.read_sql("""select c.country_code,c.country_name,count(*) as number_of_debts from countries_debt cb join countries c on c.country_code = cb.country_code
	group by c.country_code,c.country_name""", db_engine)
    query_result_8 = pd.read_sql("select * from countries_debt where debt_amount > 1000000000", db_engine)
    query_result_9 = pd.read_sql("""select min(debt_amount) as minimun_debt_amount,max(debt_amount) as maximum_debt_amount,avg(debt_amount) as average_debt_amount 
	from countries_debt""", db_engine)
    query_result_10 = pd.read_sql("select count(*) as total_debts_globally from countries_debt", db_engine)
    return query_result_1,query_result_2,query_result_3,query_result_4,query_result_5,query_result_6,query_result_7,query_result_8,query_result_9,query_result_10

#Intermediate query
def show_intermediate_query():
    query_result_11 = pd.read_sql("""select c.country_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by cb.country_code,c.country_name order by c.country_name""", db_engine)
    query_result_12 = pd.read_sql("""select c.country_name, sum(cb.debt_amount) as total_debt from countries_debt cb join countries c on cb.country_code = c.country_code 
	group by cb.country_code,c.country_name order by total_debt desc limit 10""", db_engine)
    query_result_13 = pd.read_sql("""select c.country_name,avg(cb.debt_amount) as average_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by cb.country_code,c.country_name order by c.country_name""", db_engine)
    query_result_14 = pd.read_sql("""select i.indicator_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join indicators i on cb.indicator_code = i.indicator_code
	group by cb.indicator_code,i.indicator_name order by i.indicator_name""", db_engine)
    query_result_15 = pd.read_sql("""select i.indicator_code,i.indicator_name,i.short_definition,sum(cb.debt_amount) total_debt_amount from countries_debt cb join indicators i 
	on cb.indicator_code = i.indicator_code group by i.indicator_code,i.indicator_name,i.short_definition order by total_debt_amount desc limit 1""", db_engine)
    query_result_16 = pd.read_sql("""select c.country_code,c.country_name,c.currency_unit,c.region,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by c.country_code,c.country_name,c.currency_unit,c.region order by total_debt_amount limit 1""", db_engine)
    query_result_17 = pd.read_sql("""select cb.country_code,c.country_name,cb.indicator_code,i.indicator_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	join indicators i on cb.indicator_code = i.indicator_code group by cb.country_code,cb.indicator_code,c.country_name,i.indicator_name order by c.country_name,i.indicator_name""", db_engine)
    query_result_18 = pd.read_sql("""select cb.country_code,c.country_name,count(distinct cb.indicator_code) as total_indicators from countries_debt cb join countries c on c.country_code = cb.country_code
	group by cb.country_code,c.country_name order by cb.country_code""", db_engine)
    query_result_19 = pd.read_sql("""select c.country_code,c.country_name,c.currency_unit,c.region,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join countries c on c.country_code = cb.country_code
	group by c.country_code,c.country_name,c.currency_unit,c.region having sum(cb.debt_amount) > (select avg(debt_amount) from countries_debt)""", db_engine)
    query_result_20 = pd.read_sql("""select dense_rank() over(order by sum(cb.debt_amount) desc) as countries_rank_on_debt_amount,c.country_code,c.country_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb 
	join countries c on c.country_code = cb.country_code group by c.country_code,c.country_name order by total_debt_amount desc""", db_engine)
    return query_result_11,query_result_12,query_result_13,query_result_14,query_result_15,query_result_16,query_result_17,query_result_18,query_result_19,query_result_20

#Advanced query
def show_advanced_query():
    query_result_21 = pd.read_sql("""select i.indicator_code,i.indicator_name,sum(cb.debt_amount) as total_debt_amount from countries_debt cb join indicators i on cb.indicator_code = i.indicator_code
	group by i.indicator_code,i.indicator_name order by total_debt_amount desc limit 5""", db_engine)
    query_result_22 = pd.read_sql("""select c.country_code,c.country_name,sum(cb.debt_amount) as total_debt_amount_of_country,round((sum(cb.debt_amount)/(select sum(debt_amount) from countries_debt))*100,2) as percentage_contribution_in_total_debt 
	from countries_debt cb join countries c on c.country_code = cb.country_code group by c.country_code,c.country_name order by percentage_contribution_in_total_debt""", db_engine)
    query_result_23 = pd.read_sql("""select * from (select cb.indicator_code,c.country_name,sum(cb.debt_amount) as total_debt_amount,dense_rank() over 
			   (partition by cb.indicator_code order by sum(cb.debt_amount) desc) as country_rank from countries_debt cb join countries c on cb.country_code = c.country_code
		       group by cb.indicator_code,c.country_name) as ranked_countrie where country_rank <= 3 order by indicator_code""", db_engine)
    query_result_24 = pd.read_sql("""select c.country_code,c.country_name,(max(debt_amount) - min(debt_amount)) as diff_btw_max_min_debt_amount from countries_debt cb join
	countries c on c.country_code = cb.country_code group by c.country_code,c.country_name""", db_engine)
    query_result_25 = pd.read_sql("""select * from top_10_highest_debt_countries""", db_engine)
    query_result_26 = pd.read_sql("""select c.country_code,c.country_name,sum(cd.debt_amount) as total_debt_amount,case when sum(cd.debt_amount) <= 5903333333333.33 then 'Low Debt'
	when sum(cd.debt_amount) <= 12251666666666.66 then 'Medium Debt' else 'High Debt' end as debt_category from countries_debt cd join countries c
    on cd.country_code = c.country_code group by c.country_code,c.country_name order by total_debt_amount desc""", db_engine)
    query_result_27 = pd.read_sql("""select cb.country_code,cb.indicator_code,cb.debt_year,cb.debt_amount,sum(cb.debt_amount) over(partition by cb.country_code order by cb.debt_year,cb.indicator_code) AS cumulative_debt_amount
	from countries_debt cb order by cb.country_code,cb.debt_year,cb.indicator_code""", db_engine)
    query_result_28 = pd.read_sql("""select i.indicator_code,i.indicator_name,i.short_definition,avg(cb.debt_amount) average_debt_amount from countries_debt cb join indicators i 
	on cb.indicator_code = i.indicator_code group by i.indicator_code,i.indicator_name,i.short_definition having avg(cb.debt_amount) > (
	select avg(debt_amount) from countries_debt) order by i.indicator_code""", db_engine)
    query_result_29 = pd.read_sql("""select * from (select c.country_code,c.country_name,sum(cb.debt_amount) as total_debt_amount,round((sum(cb.debt_amount) * 100.0)/(select sum(debt_amount) from countries_debt),2) AS contribution_percentage_on_total_debt
    from countries_debt cb join countries c on cb.country_code = c.country_code group by c.country_code,c.country_name) t
	where contribution_percentage_on_total_debt > 5 order by contribution_percentage_on_total_debt desc""", db_engine)
    query_result_30 = pd.read_sql("""select c.country_code,c.country_name,t.indicator_code,i.indicator_name,t.total_debt_amount from (select country_code,indicator_code,sum(debt_amount) as total_debt_amount,
	row_number() over (partition by country_code order by sum(debt_amount) desc) as rn from countries_debt group by country_code,indicator_code) t	
	join countries c on c.country_code = t.country_code join indicators i on i.indicator_code = t.indicator_code where rn = 1 order by c.country_name""", db_engine)
    return query_result_21,query_result_22,query_result_23,query_result_24,query_result_25,query_result_26,query_result_27,query_result_28,query_result_29,query_result_30