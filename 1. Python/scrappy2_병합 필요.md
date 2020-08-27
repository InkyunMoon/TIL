scrappy in VS



VS에서 conda환경 설정 후

- scrapy startproject naver_scrapper
- settings에서 ROBOTSTXT_OBEY = False

spiders 폴더 내에

- naver_scrapper.py를 생성한 뒤, 다음 코드 붙여넣기

```
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

- url을 보내면 동시에 보낸다. urls 루프 돌면서 리퀘스트 주고, 리스폰스를 받아오면 callback의 함수가 호출되어 parse함수가 비동기적으로 작동.(self와 response를 아규먼트로 받는다.)

- 돌릴 때 name이라는 것을 기준으로 작동한다. 이것을 py파일의 이름과 같게 만들어준다.(이왕이면 클래스 이름도 변경해주자.)

- 실제로 run 할때는 scrapy crawl naver를 최상위 디렉토리에서 실행한다.(spiders가 아닌 프로젝트 폴더에서.)
  - self.log는 데이터를 가져와서 print처럼 보여주는 것.



### 파이썬 버전 변경하기

- 최상위 폴더에서 conda create --name mulcam python=3.6 anaconda



### 스크래핑 한 것 저장하기

#### items

- 비구조적 데이터를 구조적 데이터로 변환하는 것.(추출한 것을 구조적으로 뽑아낸다.)



- settings에 가서 아이템 파이프라인을 설정해야한다.
  - configure 'item pipelines'를 언커맨드

- items.py에서 내가 받을 아이템을 선언해준다.
  - 리퀘스트해서 리스폰스 받아오면 아이템을 아이템 파이프라인스에 넘겨준다. 
  - 선언한 아이템을 parse할 때 가져오면 된다.(item =  NaverCrawlerItem()을 먼저 선언해준다.)





### yield

return을 하면 동기화가 안된다. yield를 통해서 하나씩 올 때마다 파이프라인에 하나씩 데이터가 쌓인다.(제너레이터로 작동)



### pipelines

- 아이템을 pipelines에 어떻게 세이브할 것인지 설정

- yield item 하면 파이프라인으로 들어간다.

두가지 방법으로 세이브할 수 있다. csv or json

가끔 csv는 데이터가 망가지는 경우가 있으므로 가급적이면 json으로 하자. 실습은 csv로 진행한다.

- from scrapy.exporters import CsvItemExporter





code news.csv : VS 내에서 파일이 열린다.

csv같은 경우 리스트를 넣으면 문자열로 들어가면 문제가 생긴다.





scrapy 자체가 리소스를 많이 잡아먹는다. 따라서 왠만하면 items를 쌓아두고, 추후에 전처리를 하는 것이 좋다.