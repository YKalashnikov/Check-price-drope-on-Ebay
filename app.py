import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep
import time

URL = 'https://www.ebay.com/itm/Tello-Quadcopter-Drone-with-HD-camera-and-VR-powered-by-DJI-technology/382959043447?epid=23027545274&hash=item592a234377:g:P3IAAOSwiXhc3wD9'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.122 Safari/537.36"}


def price_drop():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='itemTitle').get_text()
    price = soup.find(id='prcIsum').get_text()
    formatted_price = float(price[4:8])

    if (formatted_price < 90):
        sendEmail()
    print(title)
    print(formatted_price)
   

def sendEmail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('uk2709@gmail.com', 'vsxdacpfykhltxqa')

    subject = 'Good news, the price has been dropped'

    body = 'Check this Ebay link https://www.ebay.com/itm/Tello-Quadcopter-Drone-with-HD-camera-and-VR-powered-by-DJI-technology/382959043447?epid=23027545274&hash=item592a234377:g:P3IAAOSwiXhc3wD9'

    msg = 'Good news, the price has been dropped\n\nCheck this Ebay link:https://www.ebay.com/itm/Tello-Quadcopter-Drone-with-HD-camera-and-VR-powered-by-DJI-technology/382959043447?epid=23027545274&hash=item592a234377:g:P3IAAOSwiXhc3wD9'

    server.sendmail(
        'pupsik@gmail.com', 
        'uk2709@gmail.com',
         msg)
    print("Email has been sent")

    server.quit()

while(True):
    price_drop()
    time.sleep(1440)
