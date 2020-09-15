import requests , sys
from bs4 import BeautifulSoup



def check_price(a):
    URL = a
    header={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    page = requests.get(URL,headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id= 'priceblock_ourprice').get_text()
    print(price)
    print(title.strip())
    #print(soup.prettify)



a = 'https://www.amazon.ca/Essie-Nail-Polish-Expressie-Milliliters/dp/B07Y8YCVPB?pf_rd_r=AXF7ED5GYAXAWXAG0SDF&pf_rd_p=d8679d60-6b09-436c-a1f8-13c7b89c380e&pd_rd_r=a1d8ff32-67ae-4827-8129-2f091b144c54&pd_rd_w=9KXxK&pd_rd_wg=zHt71&ref_=pd_gw_ci_mcx_mr_hp_d'
check_price(a)
#check_price(sys.argv[1])