import pandas as pd
import yfinance as yf
import sqlite3

#Inputs to fetch desired data
ticker = 'AAPL'
intervals = '1wk'
start_date = '2012-5-14'
end_date = '2022-5-13'

#save data as a pandas dataframe
data = yf.download(tickers=ticker,
                   interval=intervals,
                   start=start_date,
                   end=end_date)

#Connect to DB (and create it if it doesn't already exist)
con = sqlite3.connect('AAPL_10y.db')
cur = con.cursor()

#Create a table
# cur.execute('''CREATE TABLE AAPL_10Y
#             (Open real, High real, Close real, Low real, Volume real)''')

#Add data from pandas dataframe to sqlite db
# data.to_sql(name='AAPL_10Y', con=con, if_exists='replace', index=False)
# con.commit()

# #Add weekly_change column
# cur.execute('''ALTER TABLE AAPL_10Y ADD weekly_change real''')
# con.commit()

#Add data to weekly_change column
# cur.execute('''UPDATE AAPL_10Y SET weekly_change = Open - Close''')
# con.commit()

# Add weekly_change_percent column
# cur.execute('''ALTER TABLE AAPL_10Y ADD weekly_change_percent real''')
# con.commit()

#Add data to weekly_change_percent column
# cur.execute('''UPDATE AAPL_10Y SET weekly_change_percent = weekly_change / Open * 100''')
# con.commit()

#Remove NULL rows
# cur.execute('''DELETE FROM AAPL_10Y WHERE Open IS NULL''')
# con.commit()

#Clean up Date (remove time aspect)
# cur.execute('''UPDATE AAPL_10Y SET Date = substr(Date, 1, 10)''')
# con.commit()

#Find dates of greater than 10% weekly advance or decline and how often it happened and save as .csv
# t = pd.read_sql_query('''SELECT Date, weekly_change_percent FROM AAPL_10Y AS ten_percent WHERE weekly_change_percent > 10 OR weekly_change_percent < -10''', con)
# t.to_csv('10%_weekly_move.csv', index=False)

#Find the largest weekly increase
# cur.execute('''SELECT MAX(weekly_change_percent) FROM AAPL_10Y ''')
# t = cur.fetchall()
# print(t)

#Find the largest weekly decrease
# cur.execute('''SELECT MIN(weekly_change_percent) FROM AAPL_10Y ''')
# t = cur.fetchall()
# print(t)

#Save Close in .csv
# t = pd.read_sql_query('''SELECT Date, Close FROM AAPL_10Y ''', con)
# t.to_csv('close.csv', index=False)

#Count number of positive and negative weeks
# t = pd.read_sql_query('''SELECT COUNT(weekly_change_percent) AS positive_weeks FROM AAPL_10Y WHERE weekly_change_percent > 0 ''', con)
# d = pd.read_sql_query('''SELECT COUNT(weekly_change_percent) AS negative_weeks FROM AAPL_10Y WHERE weekly_change_percent < 0 ''', con)
# z = pd.concat([t, d], axis = 1)
# z.to_csv('pos_neg_weeks.csv', index=False)
