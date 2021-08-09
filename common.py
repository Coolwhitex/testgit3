# 格式化headers字符串
def forma_theaders(s_headers):
    # 去除参数头尾的空格并按换行符分割
    s_headers = s_headers.strip().split('\n')

    # 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
    s_headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in
                 s_headers}

    return s_headers

print(forma_theaders("""accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
content-length: 28
content-type: application/json; charset=utf-8
origin: https://mms.pinduoduo.com
referer: https://mms.pinduoduo.com/
sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: cross-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"""))