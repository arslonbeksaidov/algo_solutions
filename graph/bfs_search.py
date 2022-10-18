from collections import deque


def bfs_search(start, target="elon_mask"):
    search_queue = deque()
    search_queue += graph[start]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f'{target}ni topdik!')
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


graph = {
    'siz': ['ali', 'vali', 'tohir'],
    'ali': ['aziza', 'olim'],
    'vali': ['botir', 'ziyoda'],
    'tohir': ['elon_mask', 'mohir'],
    'olim': [],
    'aziza': [],
    'botir': [],
    'ziyoda': ['aziza'],
    'elon_mask': [],
    'mohir': []

}

print(bfs_search('siz','mohir'))
