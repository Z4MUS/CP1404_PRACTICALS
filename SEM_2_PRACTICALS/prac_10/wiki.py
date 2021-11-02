import wikipedia


def main():
    page = input("search title or phrase: ")
    while page != "":
        page_summary = ''
        try:
            page_summary = wikipedia.summary(page)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        print(page_summary)
        page = input("search title or phrase: ")
    print("hope you had fun")


main()
