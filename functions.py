from lib import *

#fetching data
def data(x): 
    fyf.pdr_override()
    today_date=datetime.today().strftime('%Y-%m-%d')
    yf_data=web.get_data_yahoo(x, start = '2013-01-01', end = today_date)
    #dataframe
    df=pd.DataFrame(yf_data)
    df.reset_index(inplace=True)
    df.rename(columns={"Adj Close": "Adj_Close"}, inplace=True)

    return df

#simple moving average 10,30 days
def SMA(df, x):
    SMA_calc=df.Adj_Close.rolling(window=x, min_periods=x).mean()

    return SMA_calc

#exponential moving average 20,30,200 days
def EMA(df, x):
    EMA_calc=df.Adj_Close.ewm(span=x, min_periods=x, adjust=False).mean()

    return EMA_calc

 #rate of change ROC 10,30 days
def ROC(df, n):
    ROC_diff=df.Adj_Close.diff(n)
    ROC_shift=df.Adj_Close.shift(n)
    #roc formula
    ROC_calc=((ROC_diff/ROC_shift)*100)

    return ROC_calc 

#volume rate of change 10,30 days
def VROC(df, n):
    VROC_diff=df.Volume.diff(n)
    VROC_shift=df.Volume.shift(n)
    #roc formula
    VROC_calc=((VROC_diff/VROC_shift)*100)

    return VROC_calc

#relative strength index RSI 14 days
def RSI(df, n=14):
    delta=df.Adj_Close.diff()
    dup, ddown=delta.copy(), delta.copy()
    #average gains and losses
    dup[dup<0]=0
    ddown[ddown>0]=0
    rolup=dup.rolling(window=n, min_periods=n).mean()
    roldown=ddown.rolling(window=n, min_periods=n).mean().abs()
    #relative strength
    RS_calc=rolup/roldown
    #rsi formula
    RSI_calc=(100-(100/(1+RS_calc)))

    return RSI_calc

#RSI indicators %30 %70
def RSI_Ind(df):
    rsi_vals=[]
    for i in df['RSI14'].iloc[:]:
        if i <= 30:
            rsi_vals.append(0)
        elif i >= 70:
            rsi_vals.append(1)
        else:
            rsi_vals.append(2)

    return rsi_vals

#STO%K%D Stochastic oscillator 14,200 days
def STOK(close, low, high, n):
    STOK_calc=((close-low.rolling(n).min())/(high.rolling(n).max()-low.rolling(n).min()))*100

    return STOK_calc


#bollinger bands upper
def BBandsUp(close, n, mult):
    BBandsUp_calc=close.rolling(window=n, min_periods=n).mean() + close.rolling(window=n, min_periods=n).std() * mult
  
    return BBandsUp_calc

#bollinger bands lower
def BBandsLow(close, n, mult):
    BBandsLow_calc=close.rolling(window=n, min_periods=n).mean() - close.rolling(window=n, min_periods=n).std() * mult
  
    return BBandsLow_calc

#creating a signal; 1 if the short term price is higher than long terms
#1 for buy and 0 for sell
def BuySellSignal(low, high):
    
    return np.where(low>high, 1, 0)

