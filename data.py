import functions
from lib import *


#passing desired market ticker (can be switched to user input string)
ticker_df = functions.data('NFLX')

#adding FE columns
ticker_df['SMA10']=functions.SMA(ticker_df,10)
ticker_df['SMA30']=functions.SMA(ticker_df,30)
ticker_df['EMA20']=functions.EMA(ticker_df,20)
ticker_df['EMA30']=functions.EMA(ticker_df,30)
ticker_df['EMA200']=functions.EMA(ticker_df,200)
ticker_df['ROC10']=functions.ROC(ticker_df,10)
ticker_df['ROC30']=functions.ROC(ticker_df,30)
ticker_df['VROC10']=functions.VROC(ticker_df,10)
ticker_df['VROC30']=functions.VROC(ticker_df,30)
ticker_df['RSI14']=functions.RSI(ticker_df)
ticker_df['RSI14_IND']=functions.RSI_Ind(ticker_df)
ticker_df['STOK14']=functions.STOK(ticker_df.Adj_Close, ticker_df.Low, ticker_df.High, 14)
ticker_df['STOK200']=functions.STOK(ticker_df.Adj_Close, ticker_df.Low, ticker_df.High, 200)
ticker_df['BBandUpper']=functions.BBandsUp(ticker_df.Adj_Close,20,2)
ticker_df['BBandLower']=functions.BBandsLow(ticker_df.Adj_Close,20,2)
ticker_df['signal']=functions.BuySellSignal(ticker_df.SMA10, ticker_df.SMA30)

#filling NaNs of feature engineered columns at the end not to alter calculations
ticker_df.fillna(method='bfill', inplace=True)

#check the ticker_df
#print(ticker_df.head(3))

#train/test split
y=ticker_df['signal']
X=ticker_df.iloc[:,1:-1]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=10)