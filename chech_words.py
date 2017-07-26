import urllib

def read_text():
    text_file = open("/Users/codex/Downloads/movie_quotes.txt")
    content_of_file = text_file.read()

    print(content_of_file)
    text_file.close()

    check_bad_words(content_of_file)

def check_bad_words():
    connection = urllib.urlopen(
        "http://lojavirtu.esy.es/")

    response_output = connection.read()

    print(response_output)

    connection.close()

check_bad_words()
