##from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(event_title, location):
    # generate a url from title and position
    site = 'https://www.eventbrite.ca/d/canada--ottawa/all-events/?q={}&location={}'
    #'https://www.eventbrite.ca/d/canada--location = {}/event_title = {}'
    url = site.format(event_title, location)
    return url

def get_record(card):
    event_title = card.find('div', class_='eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy').text.strip()
    event_location = card.find('div', class_ ='card-text--truncated__one').text.strip()
    date = card.find('div', class_='eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm').text.strip()
    organizer_name = card.find('div', class_='eds-event-card__sub-content--organizer eds-text-color--ui-800 eds-text-weight--heavy card-text--truncated__two')
    price = card.find('div', class_='eds-event-card-content__sub eds-text-bm eds-text-color--ui-600 eds-l-mar-top-1').text.strip()

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
