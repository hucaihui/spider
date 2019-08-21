
import os

def read_cookie(path):
	if not os.path.isfile(path):
		print(path+' file not exist')

	with open('./cookie.txt') as f:
		cookie = f.read()

	return cookie


def get_header(path = './cookie.txt'):
	cookie = read_cookie(path)
	referer = 'https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_12c2fdb131424f2aa6f4b740d31c0f0e'
	user_agent =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

	headers = {
		'cookie': cookie,
		'referer': referer,
		'upgrade-insecure-requests': '1',
		'user-agent':user_agent
	}

	return  headers





if __name__ == '__main__':

	headers = get_header()
	print(headers)