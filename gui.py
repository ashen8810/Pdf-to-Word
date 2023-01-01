def wik(data):
    import wikipedia
    try:
        res = wikipedia.summary(data)
    except Exception as resu:
        res = resu

    if not str(res).lower().startswith("page"):
      return 0
    return res
def google(resultlo):
    resultlo = resultlo.replace(" ", "+")
    import requests
    import bs4
    b = "https://www.google.com/search?&q=" + resultlo
    r = requests.get(b).text
    soup = bs4.BeautifulSoup(r, "lxml")
    j = []

    try:
        re = soup.find("div", "BNeawe").text
        re2 = soup.findAll("div", "BNeawe s3v9rd AP7Wnd")
        k = 0
        for i in re2:
            i = i.text + "\n"
            if i not in j:
                j.append(i)

            k = k + 1
            if k > 5:
                break






    except:
        re = "Server is busy"
    # print(re)
    re2 = "".join(j)
    if re2 == re:
        return re,0
    return re,re2
    # try:
    #     re3 = soup.find("span", "MUxGbd wuQ4Ob WZ8Tjf").text
    # except AttributeError as e:
    #     re3 = ""
    #
    # print(re3)