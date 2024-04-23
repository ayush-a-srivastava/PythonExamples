from random import choice

capital = "Delhi"
flower = "Lotus"
Bird = "Peacock"

def random_fun_facts():
    funfacts = [
        "India has the largest number of engineers and scientists in the world",
        "India is the world's largest producer of milk",
        "More than 13 million people work in Indian Railways!",
        "India has given yoga to the world, which is more than 5,000 years old",
        "The cleanest city in India is Indore"
    ]

    index = choice("01234")
    print(funfacts[int(index)])

if __name__ == "__main__":
    random_fun_facts()