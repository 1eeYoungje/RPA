# 라이브러리 불러오기
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# 모델 불러 오기
model = tf.keras.models.load_model('xray_classification_model.h5') # X-ray 인식 모델 로딩 / 현재 모델은 폐렴만 인식
print(model.summary(), end='\n\n')

# 이미지 로딩 및 전처리
image_path = r'person1_virus_11.jpeg'

img = image.load_img(image_path, target_size=(150, 150)) # 인식 대상 이미지
img_array = image.img_to_array(img) # 배열 형식
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

# 분류 수행
predictions = model.predict(img_array) # predict = 모델 사용(인식)로 사용

# 결과 출력
print(predictions, end='\n\n')
if predictions[0][0] > 0.5:
    print("이 이미지는 PNEUMONIA에 속합니다.")
else:
    print("이 이미지는 NORMAL에 속합니다.")