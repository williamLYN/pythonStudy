menu = {
    '锅包头': ['猪头', '油', '番茄酱'],
    '铁锅炖': ['大鹅', '土豆', '排骨'],
    '地三鲜': ['茄子', '土豆', '青椒']
}
print(menu)

book = {
    '毛泽东选集': {'name': '毛泽东选集', 'press': '人民出版社出版', 'author': '毛主席'},
    '毛泽东诗词': {'name': '毛泽东诗词', 'press': '北京大学出版社', 'author': '毛主席'},
    '悲惨世界': {'name': '悲惨世界', 'press': '译林出版社', 'author': '雨果'}
}
print(book)


game_characters = {
    '战士': ['长剑', '轻甲'],
    '魔法师': ['法杖', '布甲', '法师帽'],
    '弓箭手': ['铁弓', '皮甲']
}
del game_characters['魔法师']
game_characters['野蛮人'] = ['大斧', '布甲']
for i in game_characters.keys():
    game_characters[i].append('草鞋')
print(game_characters)
