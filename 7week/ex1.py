import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("2024_seoul_data.csv", encoding='utf-8')
df2 = df.fillna(method='ffill') # 위 record 값으로 채우기
df2.info()

df2.rename(columns={'최저기온':'min_temp'}, inplace=True) # rename: 이름 변경 / 이름이 최저기온인 컬럼의 이름을 min_temp로 바꾼다. / inplace: 원본 데이터도 변경할 건지
df2.rename(columns={'평균기온':'avg_temp'}, inplace=True)
df2.rename(columns={'최고기온':'max_temp'}, inplace=True)
df2.head(3)

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 기온 변화')
plt.plot(range(1,len(df2)+1), df2['max_temp'], label='최고기온', c='r') #여러 그래프가 한 그래프화면에 보이게 하는 방법(여러줄 입력)
plt.plot(range(1,len(df2)+1), df2['avg_temp'], label='평균기온', c='y')
plt.plot(range(1,len(df2)+1), df2['min_temp'], label='최저기온', c='b')
plt.xlabel('일')
plt.ylabel('기온')
plt.legend() # 그래프의 범례표시
plt.show()