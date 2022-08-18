meal = {}


def txt_recipes(txt):
    with open(txt, 'r', encoding='utf-8') as f:
        recipes_lst = f.read().split('**')
        meal['fish'] = recipes_lst[1]
        meal['meat'] = recipes_lst[2]
        meal['vegetables'] = recipes_lst[3]
        meal['chicken'] = recipes_lst[4]
        meal['first'] = recipes_lst[5]
        meal['dessert'] = recipes_lst[6]
        meal['drink'] = recipes_lst[7]
        meal['snacks'] = recipes_lst[8]
    return meal


recipe = txt_recipes('recipes.txt')


if __name__ == '__main__':
    print(txt_recipes('recipes.txt'))