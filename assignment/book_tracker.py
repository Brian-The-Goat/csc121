def dashboard():
       print("========================================")
       print("Brian's Awesome Library")
       print("========================================")


def estimate_reading_time(pages, hours):
    return pages / hours 





def add_book():
       title = "The Martian"
       author = "Andy Weir"
       pages = "387"
       hours = estimate_reading_time(387, 40)
       print(f"'{title}' by {author} -- approx. {hours} to read")



def main():
       dashboard()
       add_book()


main()

       


