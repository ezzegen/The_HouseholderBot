import os


def txt_flowers(txt):
    """
    Function for text parsing
    :param txt: .txt file
    :return: list
    """
    with open(txt, 'r', encoding='utf-8') as f:
        fl_lst = f.read().split('*')
        clear_fllst = list(filter(None, fl_lst))
        return clear_fllst


def img_flowers(folder):
    """
    Function for output file names from a folder
    :param folder: the path to the folder(str)
    :return: list
    """
    img_lst = list(os.path.join(folder, item) for item in (os.listdir('content//images')))
    return img_lst


flower = txt_flowers('content//flowers.txt')
images = img_flowers('content//images')

if __name__ == '__main__':
    print(txt_flowers('content//flowers.txt'))
    print(img_flowers('content//images'))
