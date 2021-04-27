def abcd():
    import os

    print(os.getcwd())
    with open(f'{os.getcwd()}\\converters\\currencies\\USD.json') as file:
        print(file.read())
