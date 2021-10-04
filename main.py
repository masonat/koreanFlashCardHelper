import webbrowser as browser

word = input("Please enter the word in Korean and press enter")
search_sites = []  # creates empty list so we can add sites
hanja = f'https://hanja.dict.naver.com/#/search?query={word}'
english_dictionary = f'https://en.dict.naver.com/#/search?query={word}'
korean_dictionary = f'https://ko.dict.naver.com/#/searchs?query={word}'
news_articles = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={word}'
image = f'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q={word}'

# adds each of the above links to the list
# you can comment any of the following append() lines out if you don't wish to use them
search_sites.append(hanja)
search_sites.append(english_dictionary)
search_sites.append(korean_dictionary)
search_sites.append(news_articles)
search_sites.append(image) 

# Search for word in each site
for url in search_sites:
    browser.open(url)
