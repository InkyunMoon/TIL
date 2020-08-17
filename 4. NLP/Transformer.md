[NLP in Korean](https://nlpinkorean.github.io/illustrated-transformer/)

# Transformer

> Multi-head self-attention을 이용해 sequential computation을 줄였다.
>
> - 더 많은 부분을 병렬처리가 가능하다.
> - 더 많은 단어들 간 dependency를 모델링한다.



## 개괄적 설명

![image](https://nlpinkorean.github.io/images/transformer/The_transformer_encoders_decoders.png)

트랜스포머는 encoding & decoding 부분으로 나뉘어져 있다.

### encoding

![](
https://nlpinkorean.github.io/images/transformer/The_transformer_encoder_decoder_stack.png)

- 같은 구조를 가지지만, weight는 다른 여러개의 encoder 부분을 쌓아 올려 구성되어있다.
- 하나의 인코더는 두개의 서브 레이어로 구성되어있다.

![](https://nlpinkorean.github.io/images/transformer/Transformer_encoder.png)

- 인코더로 들어온 입력은 먼저 self-attention 레이어를 지나가게 된다.
- 이 레이어는 인코더가 하나의 특정한 단어를 인코드하기 위해서 입력 내의 다른 모든 단어들과의 관계를 살펴본다.
- 이 층을 통과하여 나온 출력은 다시 feed-forward신경망으로 들어가게 된다.

## decoder

![](https://nlpinkorean.github.io/images/transformer/Transformer_decoder.png)

- 디코더 또한 인코더에 있는 레이어를 모두 가지고 있다. 하지만 두 층 사이에 encoder-decoder attention이 포함되어있다.(Seq2Seq의 attention과 비슷함)
- 이는 decoder가 입력 문장 중에서 각 타임스텝에 가장 관련있는 부분에 집중할 수 있도록 해준다.

# 조금 더 자세한 설명

### Self attention 계산의 steps

![](https://nlpinkorean.github.io/images/transformer/transformer_self_attention_vectors.png)

1. Encoder에 입력된 벡터들(각 단어의 embedding 벡터)로부터 3개의 벡터(Q, K, V)를 만들어낸다.
   - 기존의 벡터들보다 더 작은 사이즈를 가진다. 반드시 작아야하는 것은 아니지만 multi-head attention의 계산 복잡도를 일정하게 만들기 위함이다.

![](https://nlpinkorean.github.io/images/transformer/transformer_self_attention_score.png)

2. 점수를 계산한다.

- 예를들어 Thinking에 대해서 self-attention을 계산한다고 하자. 현재 위치의 단어를 encode할 때 다른 단어들에 대해서 얼마나 집중을 해야하는지를 결정한다.

- 점수는 현재 단어의 key vector의 내적으로 계산된다.
  - 위치1에 있는 단어에 대해서 점수를 계산하려고 한다면 q1와 k1의 내적일 것이다.
  - 두번째 점수는 q1와 k2의 내적이다.
    - 쿼리는 우리가 

3. 이 점수들을 key 벡터의 제곱근으로 나눈다.
   - 안정적인 gradient를 가지게 된다.
4. 이 값을 softmax 계산을 통과시켜 모든 점수들을 양수로 만들고 합을 1로 만들어준다.
   - 이 점수는 현재 위치 단어의 encoding에 있어서 얼마나 각 단어들의 표현이 들어갈 것인지를 결정한다.

5. 입력의 각 단어들의 value벡터에 이 점수를 곱한다.
   - 집중하고 싶은 관련 단어들은 그대로 남겨두고 관련이 없는 단어들은 0.001과 같은 작은 숫자를 곱해 없애버리기 위함이다.

이렇게 나온 결과로 나온 벡터를 feed-forward 신경망으로 보내게된다.



