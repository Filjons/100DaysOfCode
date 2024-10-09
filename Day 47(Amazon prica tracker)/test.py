import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
HEADER = {"User-Agent": "Edg/129.0.0.0",
          "Accept-Language": "en-US,en;q=0.9,sv;q=0.8,en-GB;q=0.7", }
PRICE_LIMIT = 100.0

def get_price(user_input=""):
    print('Getting price info...')
    responese = requests.get(url=f"{URL}{user_input}", headers=HEADER)

    web_page = responese.text
    soup = BeautifulSoup(web_page, "html.parser")
    #print(soup.prettify())

    # extract data (songs)
    # CSS selectors to drill down in the tag tre
    price_whole = soup.find(class_="a-price-whole").get_text()
    price_fraction = soup.find(class_="a-price-fraction").get_text()
    price = float(f"{price_whole}{price_fraction}")
    #print(price)
    # Save data to file
    #file_name = f"web_search_{user_input}.txt"
    #with open(file_name, "w", encoding="utf-8") as file:
    #    file.write(soup.prettify())
    return price

def send_notification(msg=""):
    print(msg)


def main():
    price = get_price("instant_pot")

    if price < PRICE_LIMIT:
        send_notification('Ding!')
    else:
        print('Not Ding!')

if __name__ == '__main__':
    main()
