"""На заводе «Кофейный» открывается новое кафе. Изначально есть некоторое количество
кофейных зерен, молока и взбитых сливок.
Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая возвращает напиток, 
который можно приготовить из имеющихся продуктов (ingredients). На вход функция принимает заранее неизвестное 
количество предпочтений посетителя. Все напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
Бариста готовит наиболее предпочитаемый напиток из доступных."""

ingredient = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0], 
'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2], 
    'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]} 
def choose_coffee(*preferences): 
    list = []  
    for i in preferences: 
        if ingredient[i][0] <= ingredients[0] and ingredient[i][1] <= ingredients[1] \
                and ingredient[i][2] <= ingredients[2]: 
            ingredients[0] -= ingredient[i][0] 
            ingredients[1] -= ingredient[i][1] 
            ingredients[2] -= ingredient[i][2] 
            list.append (i) 
            return list 
    return 'К сожалению, не можем предложить Вам напиток' 
 
 
ingredients = [4, 4, 0] 
print(choose_coffee("Капучино", "Маккиато", "Эспрессо")) 
print(choose_coffee("Капучино", "Маккиато", "Эспрессо")) 
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))

# ingredients = [1, 2, 3] 
# print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна")) 
# print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна")) 
