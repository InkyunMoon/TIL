# Hidden Markov Model

## 1. Forward(backword생략)



## 2. Viterbi



## 3. Baum-Welch

##### **기댓값 최대화 알고리즘**(expectation-maximization algorithm, 약자 EM 알고리즘)은 관측되지 않는 잠재변수에 의존하는 확률 

모델에서 [최대가능도](https://ko.wikipedia.org/wiki/최대가능도)(maximum likelihood)나 [최대사후확률](https://ko.wikipedia.org/wiki/최대사후확률)(maximum a posteriori, 약자 MAP)을 갖는 모수의 추정값을 찾는 반복적인 알고리즘이다. EM 알고리즘은 모수에 관한 추정값으로 [로그가능도](https://ko.wikipedia.org/wiki/가능도#정의)(log likelihood)의 기댓값을 계산하는 기댓값 (E) 단계와 이 기댓값을 최대화하는 모수 추정값들을 구하는 최대화 (M) 단계를 번갈아가면서 적용한다. 최대화 단계에서 계산한 변수값은 다음 기댓값 단계의 추정값으로 쓰인다.



