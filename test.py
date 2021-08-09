import json
import execjs
import requests


def get_web_spider_rule():
    """
    获取加密参数webspiderrule
    :return:
    """
    rule_url = "https://api.yangkeduo.com/api/phantom/web/en/ft"
    rule_headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'content-length': '28',
                    'content-type': 'application/json; charset=utf-8', 'origin': 'https://mms.pinduoduo.com',
                    'referer': 'https://mms.pinduoduo.com/',
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    rule_data = {
        "scene": "cp_b_data_center"
    }

    res = requests.post(url=rule_url, headers=rule_headers, data=rule_data)
    if res.status_code == 200:
        rule_res = res.text
        web_spider_rule = json.loads(rule_res)
        return web_spider_rule.get('web_spider_rule')

# js_data = open("E:\Python项目\拼多多\拼多多ANTI\\anti.js", 'rb').read()
# new_js = execjs.compile(js_data)
# anti = new_js.call("anti")

# print(anti)

url = "https://mms.pinduoduo.com/sydney/api/goodsDataShow/queryGoodsDetailVOListForMMS"
webspiderrule = get_web_spider_rule()
print(f"webspiderrule参数：{webspiderrule}")
data = {"goodsId": "",
        "cate1Id": "",
        "cate2Id": "",
        "cate3Id": "",
        "startDate": "2021-08-09",
        "endDate": "2021-08-09",
        "queryType": 6,
        "sortCol": 0,
        "sortType": 1,
        "pageNum": 1,
        "pageSize": 10,
        "crawlerInfo": "0aoAfxndmOcYY9dMdakzlTpUn9PUpkwBOHqJRB5vET1SgBU1k4gnI4aRf5gv-xQJJWZ22Dr9ahzZPi46vHjW9g_p9Kss2dfk7pcyeFqqKy69o99QJX-7Qc9oBdfo7HPuFOvoWnAPIoSbFhCTR-y4wKu4gbDhCVJq3htd1__WRXz8PGf9HZjfVWJeElhh-8oNpce31NFkc2u-yIORZQydjXGq1WWoLGXNF7yKybecAFHqSnttGbPys5XSFTfxx_inrysYONSjR_opELUcHJV3EqMVd5uiXGzKUmbMRGmxuoeuyP8Jz83PgS07IAfrmulsgCAkbKB6XaXEV-jw-yXDlWVonuQ7lRa17Lvdt_7VKjR2hTh0L2qfDiRgAQW3DI20nYfqqo9z59l-o2iDPGOX896whojeVwpY3t3Cpz1z7EQBrwZwnmfn-oBDH0TCoY9LHPUwK3s1dvOlN9bEvK90mxfee-2Dh1dzwJ0j80VnykxIsyeDHf3PTuVHPTFGYeZ6mza1qfsTbyqi_bZzk4pXmtkSVYC_w539kSnhEHlHxq-bNoDw17t1tFT98zB5rk5JqYdw8ll2OxWZx336rKhJ1KfsdytGtIP432MLOpnSyrjH9u7wzA_2ukgQ7upnMcwkSg8gTbQjQPKBDom6xNsQkitiHFonKG11hahNTikOT9T"}

headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
           'anti-content': '0aoAfxndmOcYY9dMdakzlTpUn9PUpkwBOHqJRB5vET1SgBU1k4gnI4aRf5gv-xQJJWZ22Dr9ahzZPi46vHjW9g_p9Kss2dfk7pcyeFqqKy69o99QJX-7Qc9oBdfo7HPuFOvoWnAPIoSbFhCTR-y4wKu4gbDhCVJq3htd1__WRXz8PGf9HZjfVWJeElhh-8oNpce31NFkc2u-yIORZQydjXGq1WWoLGXNF7yKybecAFHqSnttGbPys5XSFTfxx_inrysYONSjR_opELUcHJV3EqMVd5uiXGzKUmbMRGmxuoeuyP8Jz83PgS07IAfrmulsgCAkbKB6XaXEV-jw-yXDlWVonuQ7lRa17Lvdt_7VKjR2hTh0L2qfDiRgAQW3DI20nYfqqo9z59l-o2iDPGOX896whojeVwpY3t3Cpz1z7EQBrwZwnmfn-oBDH0TCoY9LHPUwK3s1dvOlN9bEvK90mxfee-2Dh1dzwJ0j80VnykxIsyeDHf3PTuVHPTFGYeZ6mza1qfsTbyqi_bZzk4pXmtkSVYC_w539kSnhEHlHxq-bNoDw17t1tFT98zB5rk5JqYdw8ll2OxWZx336rKhJ1KfsdytGtIP432MLOpnSyrjH9u7wzA_2ukgQ7upnMcwkSg8gTbQjQPKBDom6xNsQkitiHFonKG11hahNTikOT9T',
           'cache-control': 'max-age=0', 'content-length': '618', 'content-type': 'application/json',
           'cookie': 'api_uid=ChDFimERKQW8onxbSQXFAg==; _nano_fp=XpExl0dan0djn5dqXo_PnHSmIqQ1S52KvxuKxdyp; _crr=20GFlEcoGcvh7lVVIgWdfrC00toPnHJ2; _bee=20GFlEcoGcvh7lVVIgWdfrC00toPnHJ2; _f77=d7e7033f-4e94-4fd8-b307-646363612e45; _a42=6750d0af-5ff2-4a14-a7fb-a3e5fc7ca38a; rcgk=20GFlEcoGcvh7lVVIgWdfrC00toPnHJ2; rckk=20GFlEcoGcvh7lVVIgWdfrC00toPnHJ2; ru1k=d7e7033f-4e94-4fd8-b307-646363612e45; ru2k=6750d0af-5ff2-4a14-a7fb-a3e5fc7ca38a; PASS_ID=1-FlE1xjo3sguwO2SlfS6/UbpTw8YSLhFHcdp/0NJL0lutz+qbIFTh+ORpykJBKwQUl8Z5aIkCS3ZulMifAYuS5g_663360013_60310440; mms_b84d1838=3414,120,150,3397,3434,410,3432,1202,1203,1204,1205,3417,1304; x-visit-time=1628520161035; JSESSIONID=98DC7BF22BD597855887EDF446D7964A',
           'origin': 'https://mms.pinduoduo.com', 'referer': 'https://mms.pinduoduo.com/sycm/goods_effect/detail',
           'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0',
           'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
           'webspiderrule': webspiderrule
           }

res = requests.post(url=url, headers=headers, data=data)
print(res.text)
