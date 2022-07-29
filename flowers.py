def txt_flowers(txt):
    with open(txt, 'r', encoding='utf-8') as f:
        fl_lst = f.read().split('*')
        clear_fllst = list(filter(None, fl_lst))
        return clear_fllst


flower = txt_flowers('flowers.txt')

if __name__ == '__main__':
    txt_flowers('flowers.txt')
