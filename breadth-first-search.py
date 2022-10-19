from collections import deque

graph = {"you": ['alice', 'bob', 'claire'], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + "is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                return False


def person_is_seller(name):
    return name[-1] == 'm' #This function checks whether the person’s name ends with the letter m. If it does, they’re a mango seller.


if __name__ == '__main__':
    print(graph)
    print(graph.get("you"))
    search("you")


