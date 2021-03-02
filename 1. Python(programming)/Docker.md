# Docker

docker ps : 실행중인 컨테이너만 출력

docker ps -a : (어떤 이미지를 사용해서) 컨테이너 실행한 결과 확인

- docker container ps -a와 같은 명령어

docker system df : 시스템 사용량 표시

docker image ls : 이미지 리스트 표시

## Docker contatiner 생성하기

```dockerfile
docker container run <docker-image-name> <command>
```



## image 다운 & 실행

- 다운받지 않은 이미지라도 일단 실행시키면 자동으로 다운을 받지만, 직접 다운받아보도록 한다.



1. [도커허브](https://hub.docker.com/)로 이동
2. nginx(예시) 검색 - docker pull nginx명령어 확인, 입력

3. docker image ls 입력 후 다운받은 이미지 리스트 확인

4. docker container run --name webserver -d -p 80:80 nginx

   - webserver라는 이름으로 실행
   - -d는 detach의 약자로, fore&back ground를 분리한다는 의미. 즉, background로 실행을 의미.
     - background로 실행은 실행을 시키면 계속해서 실행되고 있다는 의미(?)

   - -p는 포트. nginx는 기본적으로 80포트를 사용(웹 서버이기 때문에).
     - 80포트를 내 pc의 80포트와 연결시킨다는 의미

-----

### container 삭제

```dockerfile
docker container rm webserver
docker container prune # 실행되지 않는 모든 컨테이너 삭제
```



## 우분투 실행하기

- docker search ubuntu # 입력 후 우분투 목록 확인

```
docker container run -it --name 'test1' centos /bin/cal
```

- it는 input tty(standard out:표준출력) it를 걸게되면 대화형(Interactive)으로 서버를 실행가능
- --name 이후 컨테이너 이름 지정(지정하지 않으면 랜덤으로 할당)
- centos 는 이미지 이름이 위치하는 자리
- 마지막(bin/cal)은 명령어

```
docker container run -it --name "test1" centos /bin/cal
```

- 달력이 출력된다. 이후 docker ps입력시, 아무것도 출력되지 않는다. 달력이 출력되고 동작이 종료(eixt)되었기 때문.

### 우분투 접속하기

```
docker container run -it --name 'cosh' centos /bin/bash
# 이름에 띄어쓰기가 없다면 따옴표를 굳이 넣지 않아도 됨
```

- bash는 shell script

### 관련 명령어

```
1. docker contariner run -it --restart=always --name 'centsh' centos /bin/bash
2. docer container run -itd --name ubsh ubuntu
3. docker container attach ubsh
4. docker container [stop | start] <container-name>
5. docker container exec -it ub /bin/cat /etc/hosts
6. docker container port ubuntush
7. docker container rename ubuntush ub
8. (컨테이너 접속 후)cat /etc/issue
9. docker ps -q
```

1. --restart=always는 run할때마다 해당 이미지 기반으로 컨테이너를 재시작하라는 것.
2. --itd는 detach.

3. attach는 실제로 들어가는 것.

### 3. attach 관련 설명

- container속으로 접속: run
- 도커를 실행시킨 상태에서 컨테이너 밖으로 나가기(detach): ctrl+p q, ctrl+c
- 실행중인 컨테이너로 다시 들어가기: attach
- 컨테이너를 끝내고 나오기: exit, ctrl+d(컨테이너를 stop하고 나오는 것)
- 컨테이너 끝내기: stop

4. 컨테이너 끝내기 & 살리기
5. 실행중인 컨테이너에 명령하기
6. 사용중인 포트 확인하기
7. 컨테이너 이름 변경하기

8. 어느 컨테이너에 접속했는지 확인하기
9. 실행중인 컨테이너의 아이디 리턴

# 컨테이너간 파일 공유하기

```
1. docker container cp <container-name>:<path> <client-path>
2. docker container cp <client-file> <container-name>:<path>
3. docker run -v <localpath>:<container-path>
```

1. 컨테이너의 파일을 나(클라이언트)에게
2. 나의 파일을 컨테이너에

3. 공유 디렉토리 생성. 로컬과 컨테이너간 연결된 폴더가 생김.