import data


def report_resource():
    for res in data.resources:
        print(f' {res} : {data.resources[res]}')


def add_resource(res, quantity):
    total = data.resources[res]
    total += quantity
    data.resources[res] = total


def check_resource(coffee):
    ingredients = coffee['ingredients']

    for i in ingredients:
        if ingredients[i] > data.resources[i]:
            print(f'Sorry there is not enough {i}')
            return True


def insert_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(ingredients):
    for i in ingredients:
        data.resources[i] = data.resources[i] - ingredients[i]
    print("here your COFFEE")


def proccess_transaction(coffee, coin):
    if coffee['cost'] > coin:
        print(f" the price should {coffee['cost']}, Sorry that's not enough money. Money refunded ${coin}")
        return False
    elif coffee['cost'] < coin:
        back = round(coin - coffee['cost'], 2)
        print(f'Here is ${back} in change ')

    data.resources['money'] += coffee['cost']
    return  True


def process_machine(types):
    coffee = data.MENU[types]
    empty = check_resource(coffee)
    if empty:
        return

    coin = insert_coin()
    success = proccess_transaction(coffee, coin)
    if not success:
        return
    make_coffee(coffee['ingredients'])


def vending_machine():
    on = True
    while on:
        print("Welcome...")
        pick = input("What would you like? (espresso/latte/cappuccino):")

        match pick:
            case 'espresso' | '1':
                process_machine("espresso")
            case 'latte' | '2':
                process_machine("latte")
            case 'cappuccino' | '3':
                process_machine("cappuccino")
            case 'report':
                report_resource()
            case 'off':
                on = False


vending_machine()

