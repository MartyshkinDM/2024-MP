# import random
#
# print(random.sample(range(1, 18), 4))

# Result: [2, 11, 10, 7]


import numpy as np
import random


#(0; 999999)
list_1 = [num for num in range(999999)]
random.shuffle(list_1)

#(-1, 1)
list_2 = list(np.arange(-1, 1, 99999))


#Сomplex numbers
def get_list_3():
    def get_point():
        r = 26 / 3
        while True:
            x = random.random() * r - r
            y = random.random() * r - r
            if x ** 2 + y ** 2 < r:
                point = complex(x, y) 
                return (point.real ** 2 + point.imag ** 2) ** 0.5

    return [get_point() for _ in range(42000)]


list_3 = get_list_3()



def get_list_4():
    text = ("Вечером мы выступили в ночной марш к реке Рузе, за тридцать километров от Волоколамска. Житель южного Казахстана, я привык к поздней зиме, а здесь, в Подмосковье, в начале октября утром уже подмораживало. На рассвете по схваченной морозом дороге, по затвердевшей, вывороченной колесами грязи мы подошли к селу Новлянскому. Оставив батальон близ села, в лесу, я с командирами рот отправился на рекогносцировку. Моему батальону было отмерено семь километров по берегу извилистой Рузы. В бою, по нашим уставам, такой участок велик даже для полка. Это, однако, не тревожило. Я был уверен, что, если противник действительно подойдет когда-нибудь сюда, его встретит на наших семи километрах не батальон, а пять или десять батальонов. С таким расчетом, думалось мне, надо готовить укрепления. Не ожидайте от меня живописания природы. Я не знаю, красив или нет был расстилавшийся перед нами вид. По темному зеркалу неширокой медлительной Рузы распластались большие, будто вырезанные листья, на которых летом цвели, наверное, белые лилии. Может быть, это красиво, но я для себя засек: дрянная речонка, она мелка и удобна противнику для переправы. Однако береговые скаты с нашей стороны были недоступными для танков: поблескивая свежесрезанной глиной, хранящей следы лопат, к воде ниспадал отвесный уступ, называемый на военном языке эскарпом. За рекой виднелась даль — открытые поля и отдельные массивы, или, как говорят, клины, леса. В одном месте, несколько наискосок от села Новлянского, лес на противоположном берегу почти вплотную примыкал к воде. В нем, быть может, было все, чего пожелал бы художник, пишущий русский осенний лес, но мне этот выступ казался отвратительным: тут вероятнее всего мог, укрываясь от нашего огня, сосредоточиться для атаки противник. К черту эти сосны и ели! Вырубить их! Отодвинуть лес от реки! Хотя никто из нас, как сказано, не ожидал здесь вскорости боев, но нам была поставлена задача: оборудовать оборонительный рубеж, и следовало выполнить ее с полной добросовестностью, как положено офицерам и солдатам Красной Армии.")
    return text.split()[:15000]


list_4 = get_list_4()

#(2)
def buble_sort(arr: list) -> list:
    result = arr

    for j in range(len(result)):
        swapped = False
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            return result
print(buble_sort(list_3))

#(11)
def merge_sort(arr: list) -> list:
    def merge(left_list, right_list):
        result = []
        left_index = right_index = 0

        left_length, right_length = len(left_list), len(right_list)

        for _ in range(left_length + right_length):
            if left_index < left_length and right_index < right_length:
                if left_list[left_index] <= right_list[right_index]:
                    result.append(left_list[left_index])
                    left_index += 1
                else:
                    result.append(right_list[right_index])
                    right_index += 1

            elif left_index == left_length:
                result.append(right_list[right_index])
                right_index += 1

            elif right_index == right_length:
                result.append(left_list[left_index])
                left_index += 1

        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
print(merge_sort(list_4))
#(10)
def quick_sort(arr: list) -> list:
    result = arr
    if len(result) <= 1:
        return result
    else:
        q = random.choice(result)
        left_nums = []
        right_nums = []
        equal_nums = []
        for number in result:
            if number < q:
                left_nums.append(number)
            elif number > q:
                right_nums.append(number)
            else:
                equal_nums.append(number)
        return quick_sort(left_nums) + equal_nums + quick_sort(right_nums)
print(quick_sort(list_1))   
#(7)
def gnome_sort(arr: list) -> list:
    result = arr
    i = 0

    while i < len(result):
        if i == 0 or result[i] >= result[i - 1]:
            i += 1
        else:
            result[i], result[i - 1] = result[i - 1], result[i]
            i -= 1
    return result
print(gnome_sort(list_2))
