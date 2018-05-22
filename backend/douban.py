import requests
from bs4 import BeautifulSoup


def getDoubanMovies():
  url = 'http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit=20&page_start=0'
  data = requests.get(url).json()
  # print(data)
  movies = {}
  for item in data['subjects']:
    # 最终的结构为类似{'泰坦尼克号':{'cover':'','source':''},}
    # movie = {
    #   item['title']:{
    #     'cover':item['cover']
    #   }
    # }
    movies[item['title']] = {'cover':item['cover']}
    # print(movie)
    # movies.append(movie)
  return movies
# print(movies)

def searchMovie(keyword):
  urls=getLinks(keyword)
  # print(links)
  
  for url in urls:
    # python不支持++的写法
    
    link = getLinksInfo(url)
    if link:
      return link

# 根据关键词得到在百度里 关键词+百度云 搜索后得到的当前页面的所有子页面的链接
def getLinks(keyword):
  url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='+keyword+'%20百度云&oq=scrapy&rsv_pq=c0e6813d00041eb4&rsv_t=2573vaLXDMCn1xq9GmwawoCtXpM1LTQoNsLxzx95ILLze3Cl53K9NeHuXzY&rqlang=cn&rsv_enter=1&inputT=5315&rsv_sug3=26&rsv_sug1=20&rsv_sug7=100&bs=scrapy'
  html = requests.get(url).text
  # 之前用了beautifulsoup之后,产生的内容比原始的html要少,这里是可以的
  soup = BeautifulSoup(html, 'html.parser')
  # 下面这两种获取result的方法都可以
  # result = soup.find_all(class_='result')
  resultLinks = soup.select('.result a')
  # print(resultLinks)
  # links保存当前结果页面所有进入子页面的链接
  links=[]
  count = 0
  for resultlink in resultLinks:
    count+=1
    # print(resultlink)
    # 使用这样的写法,如果没有对应的属性也不会报错
    link = resultlink.get('href','')
    # 如果10个页面都找不到,就先放弃
    if(count>10):
      break
    if(link):
      links.append(link)
  
  return links

# 根据得到的子页面的链接进一步获取子页面信息
# 现在的选择还有很大的问题,现在只是根据百度知道里的最佳答案,如果没有的话就找不到
def getLinksInfo(url):
  html = requests.get(url).text
  soup = BeautifulSoup(html,'html.parser')
  # 暂时只选择百度知道里的最佳答案,因为一般情况下这样都可以找到
  bestAnswers = soup.select('.best-text a')
  link = ''
  
  for bestAnswer in bestAnswers:

    link = bestAnswer['href']
    # print(link)
  return link or ''

def init():
  movies = getDoubanMovies()

  for title in movies:
    # for title in movie:
    source = searchMovie(title)
    
    movies[title]['source'] = source

    print(movies[title])
  # print(movies)
  return movies





# movies=init()




if __name__ == '__main__':
    movies=init()
    
