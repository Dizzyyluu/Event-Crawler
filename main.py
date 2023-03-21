import requests
from bs4 import BeautifulSoup

def get_url(event, location):
    # generate a url from title and position
    site = 'https://www.eventbrite.ca/d/canada--location={}/event={}/?'
    url = site.format(event, location)
    return url

def get_record(card):
    event_title = card.find('div', class_='eds-event-card__formatted-name--is-clamped').text.strip()
    event_location = card.find('div', class_ ='card-text--truncated__one').text.strip()
    date = card.find('div', class_='eds-event-card-content__sub-title').text.strip()
    organizer_name = card.find('div', class_='eds-event-card__sub-content--organizer')
    price = card.find('div', class_='eds-event-card-content__sub').text.strip()

    record = event_title + "\n\n" + event_location + "\n\n" + date + "\n\n" + str(organizer_name) + "\n\n" + price

    return record

def main():
    """Run the main program routine"""
    event = input("Enter name of event: ")
    location = input("Enter job location: ")
    records = []

    url = get_url(event, location)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', class_='eds-event-card-content__content__principal')

    for card in cards:
        record = get_record(card)
        records.append(record)

    for record in records:
        print(record)
        print('\n\n')

if __name__ == '__main__':
    main()
