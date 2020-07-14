# Conv2d_transpose

### 옵션에 따른 Feature Map의 크기?

> Keras의 Conv2DTranspose의 padding옵션
>
> - 'same'인 경우, 결과가 원본크기의 stride배가 되도록 Crop
> - 'valid'인 경우, Crop을 하지 않는다.

![conv2d](C:%5CUsers%5Cstudent%5CDesktop%5Cconv2d.png)

위의 그림에서 원본 이미지의 크기는 2x2, 필터의 크기는 3x3이다.

- stride=2, padding='same' 설정을 해 주었을 경우, 출력물의 중간결과는 5x5의 크기를 갖는데 이것을 원본사이즈(2x2)의 stride(2)배로 맞추어주기 위해서 Crop한다.

- 5x5의 크기를 갖는 중간 결과는 필터가 stride하면서 겹쳤던 부분을 더해준 결과이다.