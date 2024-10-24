import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("2024_seoul_data.csv", encoding='utf-8')
df2 = df.fillna(method='ffill') # 위 record 값으로 채우기
df2.info()

df2.rename(columns={'일강수량':'rain'}, inplace=True) # rename: 이름 변경 / 이름이 최저기온인 컬럼의 이름을 min_temp로 바꾼다. / inplace: 원본 데이터도 변경할 건지
#df2.head()

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 강수량 변화')
plt.plot(df2['일시'], df2['rain'], label='강수량') #여러 그래프가 한 그래프화면에 보이게 하는 방법(여러줄 입력)
plt.xlabel('일')
plt.ylabel('강수량')
plt.legend() # 그래프의 범례표시
plt.show()