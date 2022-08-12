def txt_recipes(txt):
    with open(txt, 'r', encoding='utf-8') as f:
        recipes_lst = f.read().split('*')
    return ''.join(recipes_lst)


recipe = txt_recipes('recipes.txt')


if __name__ == '__main__':
    print(txt_recipes('recipes.txt'))