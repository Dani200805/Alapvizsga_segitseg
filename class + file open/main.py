from tanulo import Tanulo


tanulok_listaja : list[Tanulo] = []

def main():
    file_open('osztalyzatok.csv')
    print(f'Ennyi tanulo van: {len(tanulok_listaja)} db')

def file_open(filename: str) -> None:
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for row in file:
        tanulok_listaja.append(Tanulo(row))
    file.close()

main()