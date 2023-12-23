"""
author: sidiyeli@yahoo.com
"""


question_one = """
select txn_type, count(txn_type) as transaction_count
 from raw.transactions
 where ticker = 'BTC'
 group by txn_type, ticker
"""


question_two = """
 select EXTRACT(YEAR FROM txn_date::date) AS txn_year,
   txn_type,
   count(txn_type) as txn_count, 
   sum(quantity) as total_quantity, 
   avg(quantity) as average_quantity
   from raw.transactions
   where ticker = 'BTC'
   group by txn_year, txn_type , ticker
   order by txn_year
"""


question_three ="""
select 
	EXTRACT(MONTH FROM txn_date::date) AS calendar_month,
	sum(CASE WHEN txn_type = 'BUY' and ticker = 'ETH' THEN quantity ELSE 0 END) as buy_quantity,
    sum(CASE WHEN txn_type = 'SELL' and ticker = 'ETH' THEN quantity ELSE 0 END) as sell_quantity
from  raw.transactions
where  ticker = 'ETH' and EXTRACT(YEAR FROM txn_date::date) = 2020
group by calendar_month
order by calendar_month asc;
"""


question_four ="""
select first_name, 
 sum(quantity) as total_quantity
 from raw.members as members
 inner join raw.transactions as transactions
 on members.member_id = transactions.member_id 
 where ticker = 'BTC'
 group by first_name, ticker
 order by total_quantity desc 
 limit 3
"""