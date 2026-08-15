import csv
from collections import Counter

def importer():
    bok = []
    with open("library_books.csv", "r", encoding= 'utf-8-sig') as book:
        books = csv.DictReader(book)
        for row in books:
            bok.append(row) 
    return bok

def filter_by_category(books):
    cat = input("enter the category: ").strip().lower()
    category = []
    found = False
    for row in books:
        if row['category'].lower() == cat:
            category.append(row)
            found = True
    if found:
        print("find")
        return category
    else:
        print("not find")

def filter_result(books):
    user_cat = input("insert your favourite category: ").lower().strip()
    user_rate = input("enter your recorede rate: ")
    try:
        user_rate = float(user_rate)
    except ValueError:
        print("insert a number")

    outcome = []
    for row in books:
        if float(row['rating']) >= user_rate and row['category'].lower() == user_cat:
            outcome.append(row)

    if not outcome:
        print("nothing found")
    else:
        return outcome





        
    
def filter_by_rating(books):
    result = []
    while True:
        rate = input("enter the minumun rate: ")
        try:
            rate = float(rate)
            break
        except ValueError:
            print("insert correct number")

    for row in books:
        if rate <= float(row['rating']):
            result.append(row)

    if not result:
        print("not dound")
    else:
        print("found")
        return result



def catagory_analysis(books):
        
    cnt = Counter(row['category'] for row in books)
    mst = cnt.most_common(5)
    print(mst)
    print("------category analysis-------\n")

    for index, category in enumerate(mst):
        print(f"{index}. {category[0]} --------> {category[1]} --------> {(int(category[1]) / len(books) * 100):.2f}")

    print(f"most common category = {mst[0][0]}")


def inventory_by_category(books):
    inventt = {}
    for row in books:
        ccategory = row['category']  
        copp = int(row['copies'])
        if ccategory in inventt:
            inventt[ccategory] += copp
        else:
            inventt[ccategory] = copp

    print(inventt)
        
    







def library_statics(book):
    numb = len(book)
    tot = sum(int(row['copies']) for row in book)
    avail = sum(int(row['available_copies']) for row in book)
    avreg = sum(float(row['rating']) for row in book) / numb
    mx = max(book, key=lambda row: float(row['rating']))
    mn = min(book, key=lambda row: float(row['rating']))
    print(f"-------library statics--------\n"
          f"total books = {numb}\n"
          f"total copies = {tot}\n"
          f"total available = {avail}\n"
          f" average rating = {avreg:.2f}\n"
          f"max rate is title = {mx['title']} and the rating is {mx['rating']}\n"
          f"min rate is title = {mn['title']} and the rating is {mn['rating']}")


def search_engine(books):
    searched =  input("enter the title: ").strip().lower()
    print(searched)
    found = False
    for row in books:
        if row['title'].lower() == searched or searched.lower() in row['title'].lower():
            print(f"founded\n"
                  f"book_id = {row['book_id']}\n"
                  f"title = {row['title']}\n"
                  f"author = {row['author']}\n"
                  f"year = {row['year']}\n"
                  f"rating = {row['rating']}\n"
                  f"copies = {row['copies']}\n"
                  f"available_copies = {row['available_copies']}\n")
            found = True

    if found:
        print("founded")
    else:
        print("not found")


def sore_by_rating(books):
    if not books:
        print("nothing found")
    else:
        return sorted(books, key=lambda row: float(row['rating']), reverse=True)



        
all_books = importer()

#finall = filter_result(all_books)
#asl = sore_by_rating(finall)
#catagory_analysis(all_books)
#print(asl)
##library_statics(all_books)
inventory_by_category(all_books)





