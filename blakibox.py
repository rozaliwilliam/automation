# from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
service = ChromeService( excecutable_path = "chromedriver-linux64/chromedriver")
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service,  options=options)

# Create your views here.

def convert_number(number_str):
    if 'K' in number_str:
        return int(float(number_str.replace('K', '')) * 1000)
    elif 'M' in number_str:
        return int(float(number_str.replace('M', '')) * 1000000)
    else:
        return int(number_str)


def index(request):
    search = 'kimath'
    driver.implicitly_wait(10)
    search = request.POST.get('search')
    driver.get('https://www.youtube.com')
    search_box = driver.find_element(By.TAG_NAME, 'input')
    search_box.send_keys(search)
    search_box.submit()

    try:
        title = driver.find_element(By.CLASS_NAME, 'video-tittle')
        print("Title found:", title.text)
    except:
        print("Title not found")

    try:
        verified = driver.find_element(By.CLASS_NAME, 'style-scope yt-icon')
        print("Verified found:", verified.is_displayed())
    except:
        print("Verified not found")

    try:
        subscribers_element = driver.find_element(By.ID, 'owner-sub-count')
        subscribers_text = subscribers_element.text
        subscribers = convert_number(subscribers_text)
        print("Subscribers found:", subscribers_text, "=>", subscribers)
    except:
        print("Subscribers not found")

    try:
        likes_element = driver.find_element(By.CLASS_NAME, "yt-spec-button-shape-next__button-text-content")
        likes_text = likes_element.text
        likes = convert_number(likes_text)
        print("Likes found:", likes_text, "=>", likes)
    except:
        print("Likes not found")

    try:
        viewers_element = driver.find_element(By.CLASS_NAME, 'style-scope yt-formatted-string bold')
        viewers_text = viewers_element.text
        viewers = convert_number(viewers_text)
        print("Viewers found:", viewers_text, "=>", viewers)
    except:
        print("Viewers not found")