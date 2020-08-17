# BPE, WPM, SPM

- 언어의 특성에 구애받지 않는다. 아무 언어나 사용이 가능하다.
- 형태소 분석 등을 할 필요가 없다.







출처 : https://wikidocs.net/22592

## 1. BPE(Byte Pair Encoding)

> 빈도가 높은 문자열들은 하나의 unit으로 사전에 등록하자.



- 데이터 압축 알고리즘으로, 연속적으로 가장 많이 등장한 글자의 쌍을 찾아서 하나의 글자로 병합하는 방식

#### 자연어 처리에서의 BPE

- 기존의 카운트 기반 단어사전은 OOV문제가 발생.

초기 구성은 글자 단위로 분리된 상태

```python
# dictionary
l o w : 5,  
l o w e r : 2,  
n e w e s t : 6,  
w i d e s t : 3
```

```python
# vocabulary
l, o, w, e, r, n, w, s, t, i, d
```

BPE의 특징은 알고리즘의 동작을 몇 회 반복할 것인지를 사용자가 정한다는 점이다. 총 10회를 수행한다고 가정하면(가장 빈도수가 높은 유니그램의 쌍을 하나의 유니그램으로 통합하는 과정을 10회 반복) 빈도수가 가장 높은 유니그램 쌍은 (e, s)이다.

1회 - 딕셔너리 참고시, 빈도수 가장 높은(9) (e, s)의 쌍을 es로 통합

```
# dictionary update!
l o w : 5,
l o w e r : 2,
n e w est : 6,
w i d est : 3
```

```
# vocabulary update!
l, o, w, e, r, n, w, s, t, i, d, es
```

2회 - 빈도수 9로 가장 높은 (es, t)의 쌍을 est로 통합

```
# dictionary update!
l o w : 5,
l o w e r : 2,
n e w est : 6,
w i d est : 3
```

```
# vocabulary update!
l, o, w, e, r, n, w, s, t, i, d, es, est
```

3회 - 빈도수 7로 가장 높은 (l, o)의 쌍을 lo로 통합

```
# dictionary update!
lo w : 5,
lo w e r : 2,
n e w est : 6,
w i d est : 3
```

```
# vocabulary update!
l, o, w, e, r, n, w, s, t, i, d, es, est, lo
```

이와 같은 방식으로 총 10회 반복했을 때 얻은 딕셔너리와 단어 집합은 다음과 같다.

```
# dictionary update!
low : 5,
low e r : 2,
newest : 6,
widest : 3
```

```
# vocabulary update!
l, o, w, e, r, n, w, s, t, i, d, es, est, lo, low, ne, new, newest, wi, wid, widest
```

이 경우 lowest라는 단어가 등장한다면 기존에는 OOV문제를 일으켰지만, BPE알고리즘을 사용한 단어 집합에서는 더 이상 OOV가 아니다.

기계는 우선 lowest를 전부 글자 단위로 분할한 뒤(l,o,w,e,s,t), 위의 단어 집합을 참고하여 low와 est를 찾아낸다.

즉, lowest는 low와 est의 두 단어로 인코딩한다. 이 두 단어는 모두 단어집합에 있는 단어이므로 OOV가 아니다.



## 2. Wordpiece Model

- Wordpiece Model은 BPE의 변형 알고리즘이다. WPM으로 명명한다.

- BPE가 빈도수에 기반하여 많이 등장한 쌍을 병합하는 것과 달리 병합되었을 때 코퍼스의 우도를 가장 높이는 쌍을 병합한다.

> **WPM을 수행하기 이전의 문장:** Jet makers feud over seat width with big orders at stake
> **WPM을 수행한 결과(wordpieces):** _J et _makers _fe ud _over _seat _width _with _big _orders _at _stake

- _는 문장 복원을 위한 장치