import json

BOT = {}


def create_json(path):
    with open(path, 'w', encoding='windows-1251') as f:
        data = {"а": "б"}
        json.dump(data, f, ensure_ascii=False)


def init(path):
    global BOT
    with open(path, 'r', encoding='windows-1251') as f:
        BOT = json.load(f)


def print_greeting():
    print(f'{BOT["greeting"]}, my name is {BOT["name"]}')
    print(f'Status: {BOT["status"]}')


def choose_scen():
    scens = BOT["scens"]
    print("Choose scen:")
    for i, scen in enumerate(scens.keys()):
        print(f'{scen} - {i}')
    choice = int(input())
    print(f'{list(scens.keys())[choice]}:')
    choice = list(scens.values())[choice]
    print(choice)


if __name__ == '__main__':
    init('example.json')
    print_greeting()
    choose_scen()
