# def calc_circle_area(radius):
#     area = float(radius) * 2 * 3.1415926 ** 2
#     print('circle area is ' + str(area) )

# radius = input('what is the raius of circle?')
# calc_circle_area(radius)

def vogais(text):
    count_vowels = 0
    x = 'nao e vogal'
    for letter in text:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count_vowels +=1
        else:
            print(x)
    print('Number of vowels in text is :' + str (count_vowels))

text = input('qual e a menssagem?')
vogais(text)