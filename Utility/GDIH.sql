create table countries (country_code char(3) primary key,country_name varchar(100) not null,
    				    alpha2_code char(2) not null,currency_unit varchar(50) not null,
						region varchar(100) not null,income_group varchar(50) not null,
						lending_category varchar(50) not null,external_debt_reporting_status varchar(50) not null);
create table indicators (indicator_code varchar(50) primary key,indicator_name text not null,
    				    short_definition text not null,indicator_source text not null,
    					indicator_topic varchar(255) not null,aggregation_method varchar(100) not null);
create table countries_indicator (country_code char(3) not null,indicator_code varchar(50) not null,
								  description text not null,
								  constraint pk_countries_indicator primary key(country_code,indicator_code),
								  constraint fk_ci_country foreign key (country_code) references countries(country_code),
								  constraint fk_ci_indicator foreign key (indicator_code) references indicators(indicator_code));
create table footnote (country_code char(3) not null,indicator_code varchar(50) not null,
					   time_period smallint not null,description text not null,
					   constraint pk_footnote primary key(country_code,indicator_code,time_period),
					   constraint fk_footnote_country foreign key (country_code) references countries(country_code),
					   constraint fk_footnote_indicator foreign key (indicator_code) references indicators(indicator_code));
create table countries_debt (country_code char(3) not null,indicator_code varchar(50) not null,
    						 debt_year smallint not null,debt_amount numeric(20,2) not null,
							 constraint pk_countries_debt primary key(country_code,indicator_code,debt_year),
					   		 constraint fk_cb_country foreign key (country_code) references countries(country_code),
					         constraint fk_cb_indicator foreign key (indicator_code) references indicators(indicator_code));

