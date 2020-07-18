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

```python
df_train[['Pclass','Survived']].groupby(['Pclass'],as_index=True).sum()
```

- sum을 통해 생존자의 수를 출력한다. Survived열에서 생존자는 1로 기록되었기 때문에 이를 더하면 생존자의 수가 된다.
- count는 0, 1을 산술적으로 계산하는 개념이 아닌, 지정된 조건에서 row의 개수를 출력한다.
- grouped객체에 mean을 하게 되면, 각 클래스별 생존율을 얻을 수 있다.

```python
pd.crosstab(df_train['Plcass'],df_train['Survived'], margins=True)
```

- 앞서 진행한 두가지 작업을 한 번에 출력하는 도구가 pandas의 crosstab이다.

```python
y_position = 1.02
f, ax = plt.subplots(1, 2, figsize = (18,8))
df_train['Pclass'].value_counts().plot.bar(color=['#CD7F32','#FFDF00','#D3D3D3'], ax = ax[0])
ax[0].set_title('Number of Passengers By Pclass', y=y_position)
#df의 set_title메서드에서 y인자를 통해 타이틀의 위치를 지정해줄 수 있다.
ax[0].set_ylabel('Count')

sns.countplot('Pclass', hue='Survived', data=df_train, ax=ax[1])
ax[1].set_title('Pclass: Survived vs Dead', y=y_position)
plt.show()
```

```python
f, ax = plt.subplots(1,2, figsize=(18,8))
df_train[['Sex','Survived']].groupby(['Sex'],as_index=True).mean().plot.bar(ax=ax[0])
ax[0].set_title('Survived vs Sex')

sns.countplot('Sex', hue='Survived',data=df_train,ax=ax[1])
ax[1].set_title('Sex: Survived vs Dead')
plt.show()
```

```python
pd.crosstab(df_train['Sex'], df_train['Survived'], margins=True)
```

```python
# sns.factorplot :  3개의 차원으로 이루어진 그래프를 그릴 수 있다.
# 예를 들어, hue='Sex' 옵션을 사용하여 Pclass별 Survived의 분포를 Sex별로 볼 수 있다.

sns.factorplot('Pclass','Survived',hue='Sex', data=df_train,size=3, aspect=1.5)
## aspect는 subplot의 세로 대비 가로의 비율이다.
## hue 대신 col로 설정하면 각각의 그래프를 산출한다.
```

```python
sns.factorplot(x='Sex', y='Survived', hue='Pclass', data=df_train, satureation=.5, size=3, aspect = 1)
```

```python
## kdeplot은 분포를 확인하는데 유용한 도구이다.
## 보통 히스토그램을 많이 활용하지만, 구간을 어떻게 설정하느냐에 따라 결과가 천차만별이므로 조심해야한다.
## 따라서 그 대안으로 kdeplot을 사용하도록 하자.

fig, ax = plt.subplots(1, 1, figsize=(9,5))
sns.kdeplot(df_train[df_train['Survived'] == 1]['Age'], ax=ax)
sns.kdeplot(df_train[df_train['Survived'] == 0]['Age'], ax=ax)
plt.legend(['Survived ==1', 'Survived == 0'])
plt.show()
```

```python
## df의 plot메소드로도 kdeplot을 출력할 수 있다.
## 주어진 데이터에서 Pclass별 Age의 분포를 살펴볼 수 있다.
plt.figure(figsize=(8,6))
df_train['Age'][df_train['Pclass']==1].plot(kind='kde')
df_train['Age'][df_train['Pclass']==2].plot(kind='kde')
df_train['Age'][df_train['Pclass']==3].plot(kind='kde')

plt.xlabel('Age')
plt.title('Age Distribution within classes')
plt.legend(['1st Class','2nd Class','3rd Class'])

## Class가 낮아질수록, 나이 어린 사람의 비중이 커짐을 확인할 수 있다.
```

```python
## 전체적인 나이 변화에 따라 생존률이 어떻게 달라지는지 살펴보자.
## i살보다 어린 사람들의 'Survived'값을 더한다. 이는 생존자 수를 나타낸다.
## 위의 계산값에 i살보다 어린 사람들의 'Survived'열의 길이를 구한다. 이는 조건을 만족하는 인원수를 나타낸다.
## -> i보다 어린 사람들의 생존율을 나타낸다.
cumulate_survival_ratio = []
for i in range(1, 80):
    cumulate_survival_ratio.append(df_train[df_train['Age'] < i]['Survived'].sum()/len(df_train[df_train['Age'] < i]['Survived']))
    
plt.figure(figsize=(12,6))
plt.plot(cumulate_survival_ratio)
plt.title('Survival rate change depending on range of Age', y=1.02)
plt.ylabel('Survival rage')
plt.xlabel('range of age(0~79)')
plt.show()
```

```python
## 앞서 여러 피쳐들에 대해서 생존여부를 각각 알아보았는데, 이를 한번에 알아보도록 하자.
## violinplot은 여러 피쳐들과, 비교하고자 하는 범주에 대해서 손쉽게 시각화할 수 있다.
## 위에서 살펴본 countplot은 주 피쳐에 대해서 count값을 간편하게 시각화해주었지만, violinplot은 그 분포를 시각화해준다.
## kdeplot은 두 변수(범주형과 연속형)에 대해서 시각화해주었지만, violinplot은 세 변수에 대해 시각화할 수 있다.

f, ax =plt.subplots(1,2,figsize=(18,8))
sns.violinplot('Pclass','Age', hue = 'Survived', data = df_train, scale='count',split=True ,ax=ax[0])
## split옵션은 하나의 그래프를 반으로 나누어 범주별로 시각화한다.
ax[0].set_title('Pclass and Age vs Survived')
ax[0].set_yticks(range(0,110,10))

sns.violinplot('Sex','Age', hue = 'Survived', data = df_train, scale='count', split=True, ax=ax[1])
ax[1].set_title('Sex and Age vs Survived')
ax[1].set_yticks(range(0,110,10))
plt.show()

## scale옵션은 바이바이올린의 넓폭을 스케일링하기 위한 옵션이다.
## If area, each violin will have the same area. 
## If count, the width of the violins will be scaled by the number of observations in that bin. 
## If width, each violin will have the same width.
```

```python
f, ax = plt.subplots(1,1,figsize=(7,7))
df_train[['Embarked','Survived']].groupby('Embarked', as_index=True).mean().plot(kind='bar', ax=ax)
```

```python
f, ax = plt.subplots(1,1,figsize=(7,7))
df_train[['Embarked','Survived']].groupby('Embarked', as_index=True).mean().plot.bar(ax=ax)
```

```python
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
g = sns.distplot(df_train['Fare'], color='g', label='Skewness : {:.2f}'.format(df_train['Fare'].skew()), ax=ax)
g = g.legend(loc='best')

## distplot은 kdeplot과 histogram을 함께 그려주는 함수이다.
## df의 skew()메서드로 왜도를 구한다.

## 위의 그래프로부터 Fare 피쳐는 이상값을 가지고 있음을 알 수 있다. 또한, 분포가 매우 비대칭이므로 학습이 제대로 이루어지지 않을 수 있다.
## 이에 대하여 log를 취한다.

df_test.loc[df_test.Fare.isnull(), 'Fare'] = df_test['Fare'].mean()
# df_test의 Fare열의 null값인 행을 평균값으로 대치해준다.

df_train['Fare'] = df_train['Fare'].map(lambda i: np.log(i) if i > 0 else 0)
df_test['Fare'] = df_test['Fare'].map(lambda i: np.log(i) if i > 0 else 0)

fig, ax = plt.subplots(1,1,figsize = (8,8))
sns.distplot(df_train['Fare'], color = 'b', label = 'Skewness : {:.2f}'.format(df_train['Fare'].skew()),ax=ax)
plt.legend(loc='upper right')
plt.grid()
plt.show()
```



# Tutorial2 - visualization & machine learning



