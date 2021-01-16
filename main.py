# def get_web(url):
#     import urllib.request
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     decoded = data.decode('utf-8')
#     return decoded
#
# url = input ('웹 페이지 주소? ')
# content = get_web(url)
# print(content)
#

ages ={'Tod':35, 'Jane':23, 'Paul':62}

# for key in ages.keys():
#     print(key)
#
# for value in ages.values():
#     print(value)
#
# for key in ages:
#     print('{}의 나이는 {}입니다.'.format(key,ages[key]))
#
# for key in ages.keys():
#     print('{}의 나이는 {}입니다.'.format(key,ages[key]))

for key,value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key,value))

#딕셔너리에서는 순서가 보장이 되지 않는다. 순서가 중요할 때는 리스트를 써야 함
