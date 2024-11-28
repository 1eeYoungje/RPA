import pandas as pd

w = pd.read_csv("ch5-1.csv")

from sklearn.model_selection import train_test_split

x_data = w.iloc[:,2:5].values #독립변수(원인변수)
y_data = w.iloc[:,1].values #종속변수(결과변수)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2) #train에는 학습데이터 test에는 비교데이터 /x_test와 y_test를 지속적으로 비교한다.

# 모델 구축
from sklearn.neural_network import MLPRegressor
model_mlp = MLPRegressor().fit(x_train, y_train) #x, y train 모델 학습 

# 예측값 생성(검증단계)
y_pred_mlp = model_mlp.predict(x_test) 

# 데이터 비교 확인
df_x_test = pd.DataFrame(x_test, columns=['egg_weight','movement','food'])
df_y_pred = pd.DataFrame(y_pred_mlp, columns=['predict'])
df_y_test = pd.DataFrame(y_test, columns=['real'])
df = pd.concat([df_x_test, df_y_test, df_y_pred], axis=1)
print(df, end='\n\n')

# 모델 성능 확인 : 회귀성능 지표 계산
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
R2 = r2_score(y_test, y_pred_mlp) #검증은 r2_score 통해 진행
print("R2 = ", R2, end='\n\n')
