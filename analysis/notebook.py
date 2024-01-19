def get_valute_valute(charcode, date):
    if (date in date_dict.keys()):
        BASE_URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
        response = requests.get(f"{BASE_URL}01/{date}")
        tree = xmltodict.parse(response.content)
        tree = tree['ValCurs'];
        tree = tree['Valute'];
        date_dict[date] = tree
    tree = [x for x in tree if x['CharCode'] == charcode]
    valute = tree[0]['Value']
    return float(valute.replace(',', '.'))

date_dict = {}