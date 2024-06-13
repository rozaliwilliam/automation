from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import csv
service = ChromeService( excecutable_path = "chromedriver-linux64/chromedriver")
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service,  options=options)

csvwritter = csv.writer(open("data.csv", "w"))
csvwritter.writerow(["search key","video title"])

search_list = [
    'mama', 'baba', 'kaka', 'pacome', 'chama', 'magufuli'
]

for search_key in search_list:
    driver.get("https://www.youtube.com")

    search_box = driver.find_element(By.TAG_NAME, "input")

    search_box.send_keys(search_key)
    search_box.submit()
    driver.implicitly_wait(10)

    results = driver.find_elements(By.ID, "video-title")

    for result in results:
    # write the video title to the CSV file
        csvwritter.writerow(["", result.text])


    for result in results:
        print(result.text + "\n")
    csvwritter.writerow([search_key,""])


print ("Nimemaliza Kazi Baba")

driver.close()

driver.quit()
