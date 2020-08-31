git init

git clone url

위 두가지 방법으로 로컬 repository를 만든다.

repository를 만들면 .git 이라는 폴더를 발견할 수 있는데, 이것은 commit에 대한 정보를 가지고있는 공간이다. 계속 쓰다보면 용량이 커지고, 이것이 없으면 깃이 제대로 동작하지 않는다.

.git이 있다는 것이, repository로 동작한다는 의미이다.



#### window bash에서 conda환경 사용하기

git bash에서는 conda 환경을 설정하기 위해 추가적인 설치가 필요하다.

anaconda powershell을 통해서 별다른 설정없이 conda 환경을 사용할 수 있다.



working directory - staging index - repository

- git add 를 통해서 staging index로 옮긴다.
- git restore --staged <파일> 을 통해서 staging index에 있던 것을 다시 working directory로 옮긴다.
- commit을 통해서 repository로 보낸다.



git log

git log --oneline 을 통해서 커밋 내역을 살펴볼 수 있다.



git log --stat을 통해 조금 더 자세한 내용을 살펴볼 수 있다(몇 라인이 추가/제거 되었는지)



git log --patch를 통해 커밋 전/후를 비교할 수 있다.