#!/usr/bin/python

zombie_apocalypse = """\n My family and I went to a cabin in the woods for {} vacation.

On our first night, when all around was {}, we started hearing {} noises coming

from the woods. There were banging noises, {}, and the sounds of general {}.

My parents told us to {} in the corner and hide but that was not my {}. I told 

them that I was going to go out and {}. I grabbed a {} and went outside. Oh my gosh!

There were zombies {}! What are we going to do? How do you {} zombies? This

was not what I was expecting for this {}. It is going to be a {} night.\n """


answers = []

answers.append(raw_input("Enter 'SEASON': "))
answers.append(raw_input("Enter 'ADJECTIVE': "))
answers.append(raw_input("Enter 'ADJECTIVE': "))
answers.append(raw_input("Enter 'VERB ENDING IN ING': "))
answers.append(raw_input("Enter 'NOUN': "))
answers.append(raw_input("Enter 'VERB': "))
answers.append(raw_input("Enter 'NOUN': "))
answers.append(raw_input("Enter 'VERB': "))
answers.append(raw_input("Enter 'NOUN': "))
answers.append(raw_input("Enter 'ADVERB': "))
answers.append(raw_input("Enter 'VERB': "))
answers.append(raw_input("Enter 'NOUN': "))
answers.append(raw_input("Enter 'ADJECTIVE': "))


print zombie_apocalypse.format(*answers)
