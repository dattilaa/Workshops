def unique_preferences(pref: set, friends_pref: set) -> int:
    """
    Shows amount of unique users preferences
    :param pref: users prefs
    :param friends_pref: others prefs
    :return: unique_prefs_count
    """
    return len(friends_pref - pref)


def main() -> None:
    sweet_prefs = set(list(input().split()))
    friends = set()
    
    for friend in range(n := int(input())):
        prefs = list(input().split())
        for pref in prefs:
            friends.add(pref)

    print(unique_preferences(sweet_prefs, friends))


if __name__ == '__main__':
    main()

