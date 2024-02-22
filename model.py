phone_book = {}
path = "book.txt"
SEPARATOR = ";"


def open_phone_book():
    global phone_book
    with open(path, "r", encoding="UTF-8") as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):
        phone_book[u_id] = contact.strip().split(SEPARATOR)


def save_phone_book():
    pass


def _next_id():
    global phone_book
    if phone_book:
        return max(phone_book) + 1 if phone_book else 1


def add_new_contact(new_contact: list[str]):
    global phone_book
    phone_book[_next_id()] = new_contact


def find_contact(search_word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if search_word.lower() in " ".join(contact).lower():
            result[u_id] = contact
        return result


def edit_contact(u_id: int, edited_contact: list[str]):
