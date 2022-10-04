import os
import requests

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
}
the_folder = os.path.dirname(os.path.abspath(__file__))
input_data = os.path.join(the_folder, "no_list.txt")
output_data = os.path.join(the_folder, "names.txt")
with open(input_data, "r", encoding="utf-8") as ff:
    no_list = ff.read().split(", ")

for sno in no_list:
    sno = str(sno)
    try:
        with requests.get(
                "https://www.shutterstock.com/_next/data/NZRov-ntnEVhE7744I6Xk/en/_shutterstock/search/"
                + sno + ".json?term=" + sno,
                headers=headers,
        ) as url:
            data = url.json()
        new_url = data["pageProps"]["__N_REDIRECT"]
    except:
        with open(output_data, "a", encoding="utf-8") as ff:
            print(sno + ", contributor yok", file=ff)
        continue
    new_full_url = "https://www.shutterstock.com" + new_url
    with requests.get(
            "https://www.shutterstock.com/_next/data/NZRov-ntnEVhE7744I6Xk/en/_shutterstock"
            + new_url + ".json?title=" + new_url.strip("/image-photo/"),
            headers=headers,
    ) as url:
        data = url.json()
    contributor_name = data["pageProps"]["asset"]["contributor"]["displayName"]
    with open(output_data, "a", encoding="utf-8") as ff:
        print(sno + ", " + contributor_name + ", " + new_full_url, file=ff)
