from random import randrange

def compliments():
    quote = {
        1:'You have a wonderful smile',
        2:'Nice T-Shirt!',
        3:'You got this!',
        4:'Have a great day',
        5:'Keep smiling',
        6:'I believe in you',
        7:'You are awesome',
        8:'Keep on going',
        9:'You are not alone',
        10:"Don't give up",
        11:"You just made my day!",
        12:"You are someone who matters"
    }

    return quote[randrange(len(quote))]