# Titanic Tutorial(EDA)

이 문서는 이 [링크](https://kaggle-kr.tistory.com/32)에서 학습한 내용입니다.



## 1. Dataset 확인

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
%matplotlib inline

df_train = pd.read_csv('../input/titanit/train.csv')
df_test = pd.read_csv('../input/titanit/test.csv')

df_train.head()
```

![image-20200715213237749](C:\Users\moon\AppData\Roaming\Typora\typora-user-images\image-20200715213237749.png)

```python
df_train.info()
```

![image-20200715213333583](C:\Users\moon\AppData\Roaming\Typora\typora-user-images\image-20200715213333583.png)

```python
for col in df_train.columns:
  msg = 'column: {:<10}\t Percent of NaN value: {:.2f}%'.format(col,100*(df_train[col].isnull().sum()/df_train[col].shape[0]))
  print(msg)
```

- {:>10} -> '{인덱스:<길이}'.format(값) - 정렬할 방향과 길이. 예) {:<n} 은 n만큼의 공백을 왼쪽 정렬하라는 의미.

- '{인덱스:0개수.자릿수f}'.format(숫자)/ 인덱스를 지정하지 않는다면 생략할 수 있다.

- {:.2f}의 .앞에 0과 숫자(05 등)를 붙여주면 해당 숫자만큼의 길이로 표현된다.

```python
msno.matrix(df=df_train, figsize=(8, 8), color=(0.1,0.7,0.2))
```

<img src="C:\Users\moon\AppData\Roaming\Typora\typora-user-images\image-20200715214539472.png" alt="image-20200715214539472" style="zoom:67%;" />

- missingno 라이브러리를 통해 missing value를 시각적으로 표현할 수 있다.
- matrix외에 bar, heatmap도 있으나 지금 데이터에서는 matrix가 적합하다.
- 이는 sns.heatmap(data, cbar)와 같은 결과를 출력한다.

```python
sns.heatmap(df_train.isnull())
```

![image-20200715215043045](C:\Users\moon\AppData\Roaming\Typora\typora-user-images\image-20200715215043045.png)

```python
f, ax = plt.subplots(1, 2, figsize=(18,8))

df_train['Survived'].value_counts().plot.pie(explode = [0, 0.1], autopct = '%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Pie plot - Survived')
ax[0].set_ylabel('')

sns.countplot('Survived', data=df_train, ax=ax[1])
ax[1].set_title('Count plot - Survived')
plt.show()
```

![image-20200715215503782](C:\Users\moon\AppData\Roaming\Typora\typora-user-images\image-20200715215503782.png)

- value_counts() 메서드는 범주형 자료의 분포를 확인하는데 유용하다. 이것을 .plot.pie 메서드를 활용해서 파이차트로 만들었다.

- plot.pie의 arguments로, explode는 파이차트에서 얼마나 분리될 것인지를 설정한다.

- autopct는 각 파이 조각에 대한 비율값의 형식을 지정하는 인자이다.

- countplot 역시 범주형 자료에 대해 분포를 시각적으로 나타내는데 용이하다. 위의 예에서 Survived의 분포를 각 클래스별로 나타냈다. 

```python
df_train[['Pclass','Survived']].groupby(['Pclass'], as_index = True).count()
```

- groupby의 as_index옵션은 그룹으로 설정한 컬럼을 인덱스로 설정할 것인지에 대해 묻는 옵션이다.
- 이것을 False로 한다면, 새로운 인덱스가 새로운 열에 생성될 것이다.