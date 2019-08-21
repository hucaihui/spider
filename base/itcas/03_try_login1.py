import requests
# 直接使用cookie
url = "http://www.renren.com/852690845/profile"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "Cookie":"nonymid=job9ei9z-wbjouj; depovince=HUB; _r01_=1; JSESSIONID=abcG92lwptqcp7PXFcBHw; ick_login=0c790651-0cac-44cc-a1f0-2e593df6e1ad; first_login_flag=1; ln_uact=13218343010; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; wp_fold=0; jebecookies=7efc848f-779a-484a-b6af-95cdfbda131e|||||; _de=5A2F6A3D8B50362BE42DFB8B1DDC10F2; p=db82dbb97512f70d244a85583abdc0ba5; t=fdcc58740398e31823102823f267c59c5; societyguester=fdcc58740398e31823102823f267c59c5; id=852690845; xnsid=a4f3e92e; ver=7.0; loginfrom=null"
}

response = requests.get(url, headers=headers)
with open("renren1.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())
