def create_family_tree(n: int) -> dict:
    """
    Creates a family tree, that uses connections provided by user
    :param n: amount of connections
    :return: family tree
    """
    graph = {}

    for _ in range(n):
        parent, child = input().split()
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)
    return graph


def count_descendants(family: dict, member: str, checked=None) -> int:
    """
    Counts descendants of particular family member
    :param family: users family
    :param member: researched family member
    :param checked: set of checked children
    :return: number of descendants
    """
    if checked is None:
        checked = set()

    if member not in family:
        return 0

    counter = 0
    if member not in checked:
        checked.add(member)

    for child in family[member]:
        counter += 1 + count_descendants(family, child, checked)

    return counter

def main() -> None:
    tree = create_family_tree(int(input()))
    name = input()

    print(count_descendants(tree, name))


if __name__ == '__main__':
    main()