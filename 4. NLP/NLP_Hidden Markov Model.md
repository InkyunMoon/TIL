# Hidden Markov Model

출처: [ratsgo's speech book](https://ratsgo.github.io/speechbook/docs/am/hmm)

## 마코프 체인

> 마코프 성질을 지닌 이산확률과정

##### 마코프 성질

> 현 상태 q~i~가 나타날 확률은 단지 그 이전 상태 q~i-1~에만 의존한다.

- 마코프 체인은 시간 변화에 따른 상태들의 분포 추적에 관심.

- 한 상태에서 다른 상태로 transition은 그동안 상태 전이에 대한 긴 history가 필요한 것이 아니라, 바로 직전 상태에서의 transition으로 추정할 수 있다는 것

###### **수식1** MARKOV PROPERTY

$$
P(qi|q1,...,qi−1)=P(qi|qi−1)
$$

- 마코프 체인은 모델링을 간소화하기 위해 전이 **확률 값**이 전이 시점에 관계없이 **상태에만 의존** 한다고 가정한다.

## 히든 마코프 모델

- 각 상태가 마코프 체인을 따르되, 상태는 은닉되어있다고 가정.
  - 100년 전 아이스크림 소비 기록(observation)으로 당시 날씨(state)를 파악할 때, 날씨는 직접적으로 관측하기 어렵다.

![그림1](markdown-images/nZi5O1B.png)

- 전이확률(transition prob)과 방출확률(emission prob), 그리고 초기상태분포(π, initial prob dist)로 구성됨
  - 전이확률: 각 상태에서 다른 상태로 바뀔 확률
  - 방출확률: 은닉 상태로부터 관측치가 튀어나올(방출) 확률



## 우도

> 모델 λ가 주어졌을 때 관측치 시퀀스O가 나타날 확률. 즉, P(O|λ)



## 1. Forward

## 2. Viterbi



## 3. Baum-Welch

##### **기댓값 최대화 알고리즘**(expectation-maximization algorithm, 약자 EM 알고리즘)은 관측되지 않는 잠재변수에 의존하는 확률 

모델에서 [최대가능도](https://ko.wikipedia.org/wiki/최대가능도)(maximum likelihood)나 [최대사후확률](https://ko.wikipedia.org/wiki/최대사후확률)(maximum a posteriori, 약자 MAP)을 갖는 모수의 추정값을 찾는 반복적인 알고리즘이다. EM 알고리즘은 모수에 관한 추정값으로 [로그가능도](https://ko.wikipedia.org/wiki/가능도#정의)(log likelihood)의 기댓값을 계산하는 기댓값 (E) 단계와 이 기댓값을 최대화하는 모수 추정값들을 구하는 최대화 (M) 단계를 번갈아가면서 적용한다. 최대화 단계에서 계산한 변수값은 다음 기댓값 단계의 추정값으로 쓰인다.



