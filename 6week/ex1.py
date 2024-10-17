import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_mananger
import seaborn as sns

hat = pd.read_csv('ch4-2.csv')
print(hat.describe(), end="\n\n") # 실습 2 

font_path = "malgun.ttf"
font_name = font_mananger.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

#히스토그램 그리기
plt.figure(figsize=(10, 17))
plt.subplot(1,2,1)
plt.hist(hat.weight, bins=7)
plt.title('B 부화장 병아리 무게 분포 현황', fontsize= 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')
#plt.show()

# sns.distplot(hat.weight) # 라인 히스토그램 보기

# 실습 2

#plt.figure(figsize=(8, 10))
plt.subplot(1,2,2) # .subplot(행, 열, 순서) -> 차트 여러개를 한 화면에 출력하는 방법
plt.boxplot(hat.weight)
#plt.title('B hatchety chick weight box', fontsize = 17)
#plt.ylabel('weight(g)')
plt.show()