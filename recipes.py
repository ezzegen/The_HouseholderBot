meal = {}


def txt_recipes(txt):
    with open(txt, 'r', encoding='utf-8') as f:
        recipes_lst = f.read().split('**')
        meal['fish'] = recipes_lst[1]
        meal['meat'] = recipes_lst[2]
        meal['vegetables'] = recipes_lst[3]
    return meal


recipe = txt_recipes('recipes.txt')


if __name__ == '__main__':
    print(txt_recipes('recipes.txt'))