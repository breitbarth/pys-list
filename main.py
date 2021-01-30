import requests
from bs4 import BeautifulSoup

html_link = input("Please enter a CraigsList page: ")
page = requests.get(html_link)

soup = BeautifulSoup(page.text, 'html.parser')

class_list = set()
# First we need to get the span tags
spanTag = {tag.name for tag in soup.find_all('span')}
listOfResults = set()
sum = 0
spanList = soup.findAll('span', {'class': 'result-price'})
for span in spanList:
    listOfResults.add(" ".join(span))
    price = span.get_text().replace('$', '').replace(',', '')
    print(price)
    sum += (int(price))
    # class_list.add(" ".join(span))
    # if "result-price" in span.attrs.get("class"):
    #     class_list.add(" ".join(span))
print(listOfResults)
print(sum / len(listOfResults))
print("This is the amount of results we found:", len(listOfResults))
# print(class_list)
#
# price_classes = soup.find(class_='result-row')
#
# all_price_classes = price_classes.find_all('span')
#
# print(all_price_classes)
# splinter
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
