import requests

from cookiespool.db import RedisClient

# 这里需要动态的变一变，输入哪个用哪个
# conn = RedisClient('accounts', 'weibo')
conn = RedisClient('accounts', 'zhihu')


def set(account, sep='----'):
    username, password = account.split(sep)
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入账号密码组, 输入exit退出读入')
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)


if __name__ == '__main__':
    scan()