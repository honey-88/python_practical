# #KBC


# opation = {}


# print("WELCOME TO KAUN BANEGA CROREPATI...LET'S PLAY")
# print("Hello", input("Enter Your Name : "))

# questions = [
#     [
#         "When was the first known use of the word 'quiz'",
#         {
#             "a":"1781",
#             "b":"1771",
#             "c":"1871",
#             "d":"1881"
#         },
#         "a"
#     ],
#     [
#         "Which built-in function can get information from the user",
#         {
#             "a":"input",
#             "b":"get",
#             "c":"print",
#             "d":"write"
#         },
#         "a"
#     ],
#     [   
#         "Which keyword do you use to loop over a given list of elements",
#         {
#             "a":"while",
#             "b":"each",
#             "c":"for",
#             "d":"loop"},
#         "c"
#     ],
#     [
#         "What's the purpose of the built-in zip() function",
#         {
#             "a":"To combine several strings into one",
#             "b":"To compress several files into one archive",
#             "c":"To get information from the user",
#             "d":"To iterate over two or more sequences at the same time",
#         },
#         "d",
#     ],
# ]
# def quess(questions):
#     global score

#     for index, que in enumerate(questions):
#         print(f'\n\n\t{index + 1} : {que[0]}\n')
#         for opts, opts_value in que[1].items():
#             print(f'\t{opts} : {opts_value}')
        
        
#         quess_opt = input("\n\tEnter your option : ")
#         if quess_opt == que[2]:
#             score += 1
#             print("\tYou got it right, got 1 ppoint")
#             print(f"\tScore : {score}")
#         else:
#             print("\tSorry but that's the wrong answer")
#             print(f"\tYour total score : {score}\n\n")
#             break

# quess(questions)




questions = [
    [
        "When was the first known use of the word 'quiz'",
        {
            "a":"1781",
            "b":"1771",
            "c":"1871",
            "d":"1881"
        },
        "a"
    ],
    [
        "Which built-in function can get information from the user",
        {
            "a":"input",
            "b":"get",
            "c":"print",
            "d":"write"
        },
        "a"
    ],
    [   
        "Which keyword do you use to loop over a given list of elements",
        {
            "a":"while",
            "b":"each",
            "c":"for",
            "d":"loop"},
        "c"
    ],
    [
        "What's the purpose of the built-in zip() function",
        {
            "a":"To combine several strings into one",
            "b":"To compress several files into one archive",
            "c":"To get information from the user",
            "d":"To iterate over two or more sequences at the same time",
        },
        "d",
    ],
]

name = input("\n\tEnter your name : ")
score = 0


def guess(questions):
    global score
    print(f"\n\tName : {name}")

    for index, que in enumerate(questions):
        print(f'\n\n\t{index + 1} : {que[0]}\n')
        for opts, opts_value in que[1].items():
            print(f'\t{opts} : {opts_value}')
        
        
        quess_opt = input("\n\tEnter your option : ")
        if quess_opt == que[2]:
            score += 1
            print("\tYou got it right, got 1 ppoint")
            print(f"\tScore : {score}")
        else:
            print("\tSorry but that's the wrong answer")
            print(f"\tYour total score : {score}\n\n")
            break

guess(questions)



choice = int(input('do you play again:'))