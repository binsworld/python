# patterns = ['가위','보','보','가위','가위']
# for pattern in patterns:
#     print(pattern)
#

#
# for i in range(5):
#     print(i)


names = ['reina','jeff','jinny','joy']

# for i in range(4):
#     name = names[i]
#     print('{}번: {}'.format(i+1, name))


# for i in range(len(names)):
#     name = names[i]
#     print('{}번: {}'.format(i+1, name))

#
# for i, name in enumerate(names):
#     print('{}번: {}'.format(i+1, name))

# for i in range(11172):
#     print(chr(44032+i), end='')


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


# wintable = {
#     '가위':'보',
#     '바위':'가위',
#     '보':'바위'
# }



# def rsp(mine,yours):
#     if mine == yours:
#         return 'draw'
#     elif wintable[mine] == yours:
#         return 'win'
#     else :
#         return 'lose'
#
# result = rsp('가위','바위')
# # print('your result : ',result)
#
# messages = {
#     'win' : '이겼다',
#     'draw':'비겼네.',
#     'lose':'졌어...'
# }
#
# print (messages[result])
