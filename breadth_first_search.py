from collections import deque

graph = {
    "Mawadda": ["Muhammad", "Menna", "Youmna"],
    "Muhammad": ["Kareem", "Laila"],
    "Menna": ["Youmna"],
    "Youmna": ["Noor", "Kareem"],
    "Kareem": [],
    "Laila": [],
    "Noor": []

}

def is_person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_person_is_seller(person):
                print(f" {person} is a Mango seller !")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print("Mango seller Not found ")
    return False


search("Youmna")