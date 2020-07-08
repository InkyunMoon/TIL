# Git

> Git은 분산형 버전관리 시스템(DVCS) 중 하나이다.

## 0. Git 기초 설정

- windows 환경에서는 `git for windows`로  검색하여 `git bash`를 설치한다. [다운로드 링크](https://github.com/git-for-windows/git/releases/download/v2.27.0.windows.1/Git-2.27.0-64-bit.exe)

- 최초에 컴퓨터에서 git을 사용하는 경우 아래의 설정을 진행한다.

```bash
$ git config --global user.email 이메일주소
$ git config --global user.name 유저네임
# 확인
$ git config --global -l
```

- 이메일주소를 설정할 때, github에 가입된 이메일로 설정을 해야 커밋 이력이 github에 기록된다.



## 1. Git을 통한 버전관리 기본 흐름

### 1.1. Git 저장소 초기화 

> 특정 폴더를 git 저장소로 활용하기 위해서 최초에 입력하는 명령어

```bash
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/TIL/.git/
```

- `.git`폴더가 숨긴 폴더로 생성되며, git bash에서는 (master) 라고 표기된다.
- 반드시 git으로 활용되고 있는 폴더 아래에서 저장소를 선언하지 말자.



### 1.2 `add` 

> 커밋 대상 파일들을 추가한다.

- `add `전 상황

```bash
$ git status 
On branch master

No commits yet
# 트래킹 되지 않는 파일들
# -> 새로 생성된 파일이고, git으로 관리 중이지 않은 파일
Untracked files:
	# git add 파일
	# 커밋이 될 것들을 포함시키기 위해서 위의 명령어를 써라!
  (use "git add <file>..." to include in what will be committed)
        First.md
        Git.md
        markdown-images/

nothing added to commit but untracked files present (use "git add" to track)
```

```bash
$ git add .
$ git status
On branch master

No commits yet
# 커밋될 변경사항들
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   First.md
        new file:   Git.md
        new file:   markdown-images/800px-Lower_Manhattan_skyline_-_June_2017.jpg
        new file:   markdown-images/image-20200708141136955.png
```

- add 명령어는 아래와 같이 활용된다.

```bash
$ git add . # 현재 디렉토리 전부
$ git add git.md Git.md # 특정 파일
$ git add markdown-images/ # 특정 디렉토리
```



### 1.3. `commit`

> 이력을 확정 짓는 명령어

```bash
$ git commit -m '커밋 메시지'
[master (root-commit) d8acb14] Init
 4 files changed, 124 insertions(+)
 create mode 100644 First.md
 create mode 100644 Git.md
 create mode 100644 markdown-images/800px-Lower_Manhattan_skyline_-_June_2017.jpg
 create mode 100644 markdown-images/image-20200708141136955.png
```

### `log`

> 커밋 내역들을 확인할 수 있는 명령어

```bash
$ git log # 최근 n개 이력(현재는 1개)
commit d8acb14d4702885ddcaa0eeff05bfcaefd477631 (HEAD -> master)
Author: InkyunMoon <ik.moon23@gmail.com>
Date:   Wed Jul 8 14:39:54 2020 +0900

    Init

$ git log -1 # 간략한 표현
commit d8acb14d4702885ddcaa0eeff05bfcaefd477631 (HEAD -> master)
Author: InkyunMoon <ik.moon23@gmail.com>
Date:   Wed Jul 8 14:39:54 2020 +0900

    Init

$ git log --oneline # 최근 n개 이력을 간략하게
d8acb14 (HEAD -> master) Init

$ git log --oneline -1
d8acb14 (HEAD -> master) Init
```

## 2. 원격 저장소 활용

> 원격 저장소를 제공하는 서빗는 많다. (gitlab, bitbucket)
>
> 그중에서 github을 기준으로 설명한다.

### 2.1. 원격 저장소 등록

> git아! 원격저장소(remote)로 등록해줘(add) origin 이라는 이름으로 URL을!

```bash
$ git remote add origin 저장소 url
```

- 저장소 확인

  ``` bash
  $ git remote -v
  origin  git@github.com:InkyunMoon/TIL.git (fetch)
  origin  git@github.com:InkyunMoon/TIL.git (push)
  ```

- 저장소 삭제

  origin으로 지정된 저장소를 rm(remove)한다.

  ```bash
  $ git remote rm origin
  ```

### 2.2. `push`

origin으로 설정된 원격 저장소의 mater브랜치로 push한다.

```bash
$ git push origin master
```

