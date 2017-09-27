import requests

def getWebSite(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encodeing = r.apparent_encoding
        print(r.apparent_encoding)
        return r.text
    except:
        print(r.text)
        return "产生异常"
def main():
	urlJD = "https://item.jd.com/5007528.html?cpdad=1DLSUE"
	urlAmazon = "https://www.amazon.cn/b/ref=lp_1905765071_gbph_img_s-3_547a_0d9b9e37?rh=i%3Adigital-text%2Cn%3A1905765071&ie=UTF8&smid=A1RWPW48FETZZ4&node=1905765071&shpo=1"
	text = getWebSite(urlAmazon);
	print(text[:1000])

if  __name__ == '__main__':
	main()
