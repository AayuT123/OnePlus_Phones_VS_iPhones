import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.mysmartprice.com/mobile/pricelist/oneplus-mobile-price-list-in-india.html"
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, "html.parser")

product_name = []
cost = []
rating = []
stars = []
Rating = []
Snapdragon = []
Camera = []
Frontcam = []
Display = []
Storage = []
Charge = []
Os = []
image_links = []

products = soup.find_all("a", class_="prdct-item__name ga_event_cls")

for product in products:
    name = product.find("h2").text
    product_name.append(name)

prices = soup.find_all("div", class_="prdct-item__prc-val")

for price in prices:
    price_value = price.get_text(strip=True)
    # Remove additional text
    price_value = price_value.split()[0]
    cost.append(price_value)

star = soup.find_all("div", class_="specs_rate algn-left")

for s in star:
    st = s.find("span")
    starss = st.text.strip()
    stars.append(starss)

rate = soup.find_all("label", class_="algn-left")
for r in rate:
    rt = r.text
    Rating.append(rt)

desc = soup.find_all("li", class_="prdct-item__spcftn kyspc__item--cpu")

for i in desc:
    d = i.text
    Snapdragon.append(d)

desc1 = soup.find_all("li", class_="prdct-item__spcftn kyspc__item--cmra")

for i in desc1:
    title = i.get("title")
    if title and title.endswith("Rear Camera"):
        d1 = i.text.strip()
        Camera.append(d1)

desc2 = soup.find_all("li", class_="prdct-item__spcftn kyspc__item--cmra")

for i in desc2:
    title = i.get("title")
    if title and title.endswith("Front Camera"):
        d2 = i.text.strip()
        Frontcam.append(d2)

desc3 = soup.find_all("li", class_="prdct-item__spcftn kyspc__item--aspct")

for i in desc3:
    d3 = i.text
    Display.append(d3)

desc4 = soup.find_all("li", class_="prdct-item__spcftn kyspc__item--ram")
for i in desc4:
    d4 = i.text
    Storage.append(d4)

desc5 = soup.find_all("li", class_="prdct-item__spcftn kyspc__item--bttry")
for i in desc5:
    d5 = i.text
    Charge.append(d5)

desc6 = soup.find_all("li", class_="prdct-item__spcftn kyspc__item--os")
for i in desc6:
    d6 = i.text
    Os.append(d6)

image_elements = soup.find_all("img", class_="prdct-item__img")

for image_element in image_elements:
    image_link = image_element.get("src")
    image_links.append(image_link)

df = pd.DataFrame({
    "Product Name": product_name,
    "Price": cost,
    "Rating": Rating,
    "Stars": stars,
    "Snapdragon": Snapdragon,
    "Camera": Camera,
    "FrontCamera": Frontcam,
    "Display": Display,
    "Storage": Storage,
    "Charge": Charge,
    "Os": Os,
    "Image": image_links
})

# print(df)

# df.to_csv("C:/Users/Aayushi/OneDrive/Documents/Mobile.csv")
df.to_csv("C:/Users/Aayushi/OneDrive/Documents/OnePlus.csv")



