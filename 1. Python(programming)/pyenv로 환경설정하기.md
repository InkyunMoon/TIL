### pyenv 라이브러리의 버전 확인
pyenv --version

### pyenv로 생성한 파이썬 버전들 확인
pyenv versions

### 가상환경 생성하기
$ pyenv virtualenv <version> <가상환경 이름>
예) pyenv virtualenv 3.7.7 lm_pfld

### 가상환경 삭제하기
$ pyenv uninstall <가상환경 이름>

### 특정 디렉토리를 가상환경으로 지정하기
- 가상환경으로 지정할 디렉토리로 이동하여 아래의 명령어를 입력한다.
$ pyenv local <가상환경 이름>
예) pyenv local Decuments

### 가상환경내에 설치된 패키지 확인하기
$ pip list