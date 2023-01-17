import pandas as pd
from pandasql import sqldf
from pandasql import load_births

births = load_births()

#print(sqldf("SELECT * FROM births where births > 250000 limit 5;",locals()))

q = """
    select
        date(date) as DOB,
        sum(births) as "Total Births"
    from
        births
    group by
        date
        limit 10;
"""

def pysqldf(q):
    return sqldf(q,globals())

print(pysqldf(q))