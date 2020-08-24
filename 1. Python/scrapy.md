# scrapy

### 1. creating a project

스크래피를 시작하기 전에 새로운 스크래피 프로젝트를 만든다.

```python
scrapy startproject tutorial
```

위의 코드를 입력하면 여러 py형식의 파일들과 함께 튜토리얼 디렉토리가 생성된다.



### 2. our firsr spider

```python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

- name : spider가 무엇인지 식별한다. 중복된 이름을 가질 수 없다.
- start_requests() : url을 입력해주면 spider가 크롤링을 할 리퀘스트들을 리턴한다.
  - 처음에는 start_requests가 자동으로 불려와서 리퀘스트를 보낸다.
  - 리스폰스를 받으면 parse가 호출된다.(콜백의 함수가 호출이 된다.)
- parse() : 각 리퀘스트를 처리한다. 리스폰스를 파싱하며 딕셔너리로 리턴한다.

- 왠만하면 클래스의 이름을 폴더 이름과 같게 만들어야 한다.

### 3. how to run our spider

```python
scrapy crawl quotes
```

- 위 명령어를 실행하면 스파이더에 name으로 지정한 것을 실행한다.
- scrapy를 run 할때는 최상위 폴더에서 한다.

- url를 여러개 동시에 보낼 수 있다. 처음 것을 보냈다가 기다리지 않고, 동시에 보내낸 뒤 리스폰스를 받아온다.(비동기적 작동)



---



### 4. 내부적 작동 원리

스파이더의 start_requests 메소드로부터 리턴된 scrapy.Request 오브젝트를 스케줄링한다.

리스폰스를 받자마자, response 오브젝트와 callback 메소드를 초기화한다.



### CSS selector

```python
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

>>> response.css('title::text').getall()
['Quotes to Scrape']

>>> response.css('title').getall()
['<title>Quotes to Scrape</title>']

>>> response.css('title::text').get()
'Quotes to Scrape'

>>> response.css('title::text')[0].get()
'Quotes to Scrape'

>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']

```



### XPath

- XPath를 사용하면 내용을 볼 수 있다.

```python
>>> response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
>>> response.xpath('//title/text()').get()
'Quotes to Scrape'
```





### items

- 비구조적 데이터를 구조적 데이터로 뽑아내는 것.

1. settings에서 item pipeline을 설정해야한다.
   - settings에서 configure item pipelines의 주석처리를 풀어준다.

2. items.py에서 item이 무엇인지 정의해준다.

   - parse할 때 item을 가져오면 된다.

   - return은 동기화가 안되므로 하나씩 파이프라인에 쌓이도록 yield(generator)로 작동.

3. parse에서 받는 아이템 값들을 지정해준다.

4. pipelines.py에서 받는 아이템을 지정해준다.



### 저장하기

- CSV

pipelines.py에서

from scrapy.exporters import CsvItemExporter 메소드를 사용한다.



윈도우에서는 CSV인코딩 문제가 발생한다. cp949로 기본적으로 인코딩되는데, csv파일을 엑셀로 열면 깨져서 보일 때가 있다. utf-8로 인코딩되어있기 때문.

판다스 등의 라이브러리는 utf-8l이다. 따라서 파일을 저장할 때는 항상 utf-8로 해야한다.



- JSON

