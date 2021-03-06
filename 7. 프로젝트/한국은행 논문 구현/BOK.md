#### 3. Feature selection

- 모든 단어가 감정을 나타내지 않으므로 feature selection이 중요하다. 이는 단어벡터의 차원을 줄임으로써 처리속도를 개선시킨다.

  또한, 단일어(single word)는 문맥을 잃어버리므로 (ex. 성장/긍정 <-> 느린 성장/부정) 이 문제를 해결하기 위해서 n-gram을 도입하였다.

  n-gram의 길이를 늘리는것은 트레이드 오프가 있다.

  1. 너무 긴 n-gram은 오버피팅 문제가 발생한다.(훈련 데이터에만 너무 구체적인 단어는 다른 데이터에 적용하기가 힘들다.)
  2. 차원의 저주가 발생한다. 1과 비슷한 이유로, 길이가 긴 n-gram은 발생할 확률이 낮아지며  차원의 증가로 인해 computational problem이 일어난다.

- 이를 해결하기 위해서 n-gram의 n을 5로 지정하는 등의 규칙을 정하였다.(1~5-gram을 사용한다.)

  - n-gram을 형성하는 단어집합을 특정 품사로 제한하였다.
  - 15회 이하로 나타나는 n-gram은 사용하지 않는다.

#### 4. Polarity Classification

- 극성 분석에 여러 범주가 있다.

  1. Supervised vs Unsupervised <- 인간의 개입이 있느냐에 따라(라벨링 유무)
  2. machine-learning-based vs lexical-based methods <- opinion words를 사용하느냐에 따라

  - lexical-based approach에는 3가지 방법의 polarity word list를 얻는 방법이 있다.
    - manual : 오래걸림, 휴먼 에러에 취약

    - dictionary-based : 유의어, 반의어 찾기 위해 seed word로부터 출발. 잘 구축된 lexical DB 필요, 특정 분야에 대한 polarity word를 잘 못찾음.

    - corpus-based : 대형 코퍼스에서 함께 발생하는 패턴을 서치하며 polarity word를 찾는다. 특정 분야의 코퍼스를 사용하여 그 분야와 문맥에 맞는 감성 단어와 polarity를 찾을 수 있다.

      -> 현재 분석에 가장 적합

- n-gram의 polarity를 두 가지 방법으로 분류한다.

  1. market approach : 머신러닝으로 시장 정보를 이용하여 극성 분석
  2. corpus-based(lexical) approach : 워드 임베딩(n-gram)과 seed words를 이용하여 분류

#### 4.1 market approach

- 자산 가격으로 부터 시장 기대에 대한 정보를 뽑아내려는 많은 시도들이 있다.(자산 가격은 금융시장 정보를 반영한다.) -> 텍스트도 역시 마찬가지이다.

- 예시) 단어들의 상대적 가중치를 결정하기 위해서 단어를 종속변수로, 배당수익을 설명변수로 두었다. (Jegadeesh and Wu)

  이는 주관적 판단에 의존하지 않고, 알고있는 단어리스트로부터 상대적 가중치를 결정하기 위해서 회귀적 접근법과 유니그램을 사용했다.

- OUR MARKET APPROACH,

  Naive bayes classifier를 사용하였다. 이는 모든 피쳐들이 독립이라고 가정한다. NBC는 차원축소기법이 아니지만, 독립가정은 각 피쳐에 대해서 조건부 확률을 이용할 수 있게 해준다.

- NBC는 supervised 학습으로 라벨링된 데이터가 필요하다. 이는 가능하다면 대중의 review로 부터 얻어지거나 전문가들이 수기로 작성하는 방법이 있다. 통화정책의 경우 전자는 사용이 불가능하고, 후자는 비용이 많이들고 전문가의 판단에 종속될 수 있다. 이 문제를 피하기 위해서 문서가 출간될 시점에서 콜금리의 1달 변화를 기준으로 매파인지 비둘기파인지 구분한다.

- 9:1의 비율로 라벨링된 문장을 트레이닝과 테스트셋으로 나누고, 1-5그램을 사용하여 학습하고 정확도를 측정하였다.

  학습된 NBC는 각 피쳐에 대해서 조건부 확률을 만들어내고, 이것을 해당 feature의 극성 점수를 계산하는데 사용할 것이다.

- 랜덤 샘플링기법을 사용하기 때문에 더 나은 예측력을 위해 이 과정을 30번 반복하고 그 평균값을 최종 스코어로 사용한다.

- `극성점수가 1을 넘으면 매파로, 1보다 작으면 비둘기파로 분류하고 1.3을 임계치로 사용하여 애매한 lexicon은 제외한다.`



#### 4.2 Lexical Approach

- market approach에서 콜금리의 변화를 release date를 기준으로 사용했지만, 이 외에도 다양한 기준이 있을 수 있다. 따라서 모든 가능성을 고려하기 보다는 시장 정보를 사용하지 않는 seed words를 사용하여 접근하도록 한다.(lexical approach)

- 같은 문맥에 대해서 두 단어가 함께 자주 등장한다면, 같은 극성을 가질 확률이 높다고 가정한다. unknown word에 대한 극성도 함께 등장하는 다른 단어의 상대적 빈도를 통해 계산할 수 있다.(PMI개념 이용 - 확률이론에 근거하여 두 변수간의 유사성을 정량화하는 기법)

- 하지만 두가지 문제점이 존재한다.

  1. 공통 발생 기반이기 때문에 반의어를 탐지하지 못함.

     -> ngram2vec으로 해결

  2. seed word에 따라 결과가 달라진다.

     -> SentProb 프레임워크 도입으로 해결

- `n-gram의 seed set을 벡터스페이스에 표상하고 이 seed로의 n-gram 근접성을 측정한다. n-gram의 극성은 해당 n-gram에 닿는(?) seed set의 random walk의 확률에 비례한다.` 각 피쳐는 매파 혹은 비둘기파가 될 확률을 가지며 최종 극성 점수는 이 둘의 상대적 비율이다.

- `market apprach와 같이, 극성 점수가 1보다 높으면 매파로, 낮으면 비둘기파로 분류하고 1.1을 임계치로 애매한 지역의 lexicon은 제외하였다.`
- 두 접근 방법에서, 69% n-gram(9,791개)이 같은 극성을 가졌다.



#### 4.3 Evaluation

- lexicon을 만드는데 사용되지 않은 문서들을 이용하여 정확도를 계산하였다.
- 평가를 위한 문서는, 한국은행 총재의 통화정책결정에 대한 기자회견의 도입문장을 사용하였고, 09년 5월부터 18년 1월까지의 문서 2341개의 문서를 일일이 매파, 비둘기파, 중립파로 라벨링하였다.
- market approach로 생성된 lexicon은 68%의 정확도를, lexical approach로 생성된 loxicon은 67%의 정확도를 보였다. 통화 정책에 대해서는 전자보다 후자가 알맞지만 비용이 많이들며 전문가의 판단에 종속될 수 있다. 이 문제를 해결하고 금융시장의 정보를 이용하기 위해서, 기사나 보고서가 출간된 날의 1달 콜금리 변동을 이용하여 hawkish or dovish로 라벨링 하였다.



#### 5. Measuring Sentiments

- 이렇게 구한 lexicons들을 이용한 마지막 단계는 타겟 문서의 tone을 측정하는 것이다. 문서의 어조(tone)을 측정하기 위해 2단계로 구성된 방법을 사용하였다.

  - 첫 번째, 매파, 비둘기파 피쳐의 개수를 기반으로 어조를 측정한다. 문장s의 톤은 다음의 공식과 같다.
    $$
    tone_s = \frac{매파 피쳐의 수 - 비둘기파 피쳐의 수}{매파 피쳐의 수 + 비둘기파 피쳐의 수}
    $$

  - 두 번째, 문서i의 톤은 다음과 같다.

  $$
  tone_i = \frac{매파 tone_{s,i}의 수 - 비둘기파 tone_{s,i}의 수}{매파 tone_{s,i}의 수 + 비둘기파 tone_{s,i}의 수}
  $$

- 각 문서에 대해 -1부터 +1의 범위를 갖는 연속형 변수 tone_i를 만든다. 통화정책의 감성을 정량화하는 지수이며, market approach에 대한 지수를 tone^mkt, lexical approach에 대한 지수를 tone^lex로 표기하기로 한다.



## IV. 경험적 분석

- 다음의 질문들에 대한 답을 제시할 것이다.

1. lexicon-based indicators(tone^mkt & tone^lex)가 한국은행의 현재와 미래 통화정책 결정을 설명할 수 있는가? 현존하는 거시경제 데이터에는 없는 추가적 정보를 가지고 있는가?
2. 분야에 특화된 단어 사전을 사용하는것이 중요할까?
3. 영-한 텍스트가 아니라 한국어 원문 텍스트를 사용하는 것이 중요할까?

1번 질문에 대한 답은 Yes이다. 우리가 만든 지표의 설명력을 측정하기 위해서 테일러 준칙을 비롯한 경제적 불확실성의 대용 지표를 비교해볼 것이다.

2번과 3번 질문에 대해서는, 한국어 원문을 사용하고 경제, 금융용어에 대한 사전을 사용하는 것이 핵심이라는 것을 보일 것이다.

#### 1. 통화정책 감성 측정 (Measuring of MP Sentiment)

- figure 4,

(a) tone^mkt & tone^lex : r=0.85

(b) tone^mkt & BOK policy rate : 통화정책을 잘 예측함.

(c) tone^mkt & EPU : r=0.06 -> 서로 반대 방향으로 움직이지 않는 것 같이 보인다.

일반적으로 경기 불확실 -> 양적 완화(비둘기파적 어조↑)

(d) tone^mkt & UI : r=-0.54

- figure 5, tone^mkt와 거시경제 변수들 비교
  
한은의 비전통적 통화정책을 고려하여, MPDt는 통화정책 스탠스에 변화가 없으면 0, 매파적 결정은 1, 비둘기파적 결정은 -1.
  
  - (a) - 비표준 통화정책을 고려한 통화정책 스탠스를 잘 따라간다.
  
- figure 6
  
  - BOK 정책과 IP는 강한 음의 상관관계, 물가상승률, tone^mkt와는 강한 양의 상관관계. 반면 EPU^korea와 음의 상관관계

#### 2.  한국은행의 통화정책 의사결정 설명하기

- 한은의 통화정책 이사회의 정책 금리결정과 의사록 정보의 관계를 평가하기 위해서 tone^mkt&lex의 현재와 미래 의사결정에 대한 설명력을 테스트했다. Picault and Renault의 설명대로 ordered probit model을 사용하여 forward looking taylor rule과 lexicon based indicators, 그리고 거시경제변수의 설명력을 비교해보도록 한다.

- 추정을 위해, 정상성을 확보하기 위해서 Xt를 더한, 차분된 방정식을 추정한다. Xt는 통화정책에 대한 상황변화를 설명하는데 도움을 주는 변수이며 tone^mkt, tone^lex이나 EPU, UI등을 고려한다. 

-  

- 통화정책이사회 회의록이 거시경제 데이터가 갖고있지 않는 추가적인 정보를 나타낸다면, tone 인디케이터는 유의미해야할 것이다.  Table 7에서, tone^mrk & tone^lex는 굉장히 유의미하지만, 나머지 경제 불확실성 등은 그렇지 않게 표현된다.

  회귀계수 또한 tone 변수가 있을때 눈에띄게 높아짐을 확인할 수 있다. -> lexicon-based indicators가 거시경제 데이터가 포착하지 못한 추가적 정보를 가지고 있음을 강하게 시사한다.

  

## 3. 다른 텍스트 기반 지표들과의 비교

- 꼭 한글 텍스트를 사용해야 하는가?(더 발전된 영어 텍스트 마이닝 기법이 있다면 영어로 번역해서 사용해도 되지 않을까)
- 특정 분야에 구체적인 사전을 사용해야 하는가?

위 질문에 대답하기 위해 4가지의 다른 지표와 비교한다.

1. 한국어 텍스트기반 지표
   - 한국어에 특화되고 범용 사전을 사용한 지표(tone^ksa)
2. 영어 기반 지표
   - google : Google Cloud Natural Language가 제공하는 감성분석 서비스 사용하여 회의록 tone 분석
   - HIV4 : 범용 하버드 IV-4 사전 사용
   - LM : 특정 분야에 구체적인 사전 사용

영어기반 텍스틍 분석을 위해 의사회 회의록을 영어로 번역하였다.

- figure7

  (a) : ksa는 mkt와 비교해서 움직임이 적다. 그러나 영어 기반 지표들은 ksa보다 변화가 크다.

- 계수의 통계적 유의성과 회귀계수를 이용하여 성능 측정 결과,

- figure 9

  - 1, 2열에서 ksa가 한은의 통화정책을 포착하지 못함을 알 수 있다.
  - google과 HIV4는 유의미하지 않고, LM은 유의수준 10%에서 유의미하다.

-> 특정 분야에 특화된 사전을 사용하는 것이 중요하다.

한국어 원문을 사용하는 것 또한 중요하다.
