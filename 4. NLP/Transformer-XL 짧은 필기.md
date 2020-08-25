# Transformer-XL

- 긴 문장을 처리하기 위함

Ex)

I like you | you are a good person

(seg 1)	| (seg 2)

- 인코더는 RNN으로 구성한다.

- 타임스탬프을 지나며 메모리가 전달된다. 메모리에 의해 you와 person의 관계가 형성된다.



# XLNet

- AR(Autoregressive) : 현재는 과거에만 종속

- AE(Auto Encoder) : 양방향. 주위 단어로 가운데 단어를 예측



##### AE의 단점

1. 버트는 LM의 근사치를 사용하고 있다. 

(예측하고자 하는 단어를 독립으로 놓는다.)

XLNet은 이것을 보완한 것

2. pre-training할 때는 mask token이 입력으로 사용되지만, fine-tunining 할 때는 사용되지 않는다.

XLNet은 mask token 대신 permutation LM을 사용한다.

문장을 뒤섞어 예측하므로 양방향이 된다.

Ex)

New York is a city

1	2	3	4	5

몇개의 조합을 구성하여 추정을 한다.

cutting point를 두어 자르기 이전의 부분만 추정한다.



전체 조합에 대한 퍼뮤테이션을 계산해서 인코더의 출력을 계산한다.

-> Permutation LM

(마스킹을 쓰지 않고 양방향으로 언어를 배울 수 있는 시스템)