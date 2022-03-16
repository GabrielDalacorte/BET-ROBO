mydivs = soup.find_all("div", {"class": "rsm-MeetingHeader_MeetingName"})


if __name__ == "__main__":

    init_data = InitBrowser(url='https://www.bet365.com/#/AS/B4/') #Galgo Example
    init_data.extract_data(init_data.init())

