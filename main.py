#== <과거 시세로 이동평균 구하기> ==#
import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']  #종가 DataFrame
window = close.rolling(5) #5일씩 모든 데이터를 그룹화함
ma5 = window.mean()  #그룹화한 데이터의 평균을 냄
print(ma5)