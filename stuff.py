#!/usr/bin/env python3

#Imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import string

import spacy
nlp = spacy.load("en_core_web_sm")

#Chatbot k
snek = ChatBot("Snooter the Civil War Snek")


#ChatBot Training - Lists and Corpus
trainer = ListTrainer(snek)
convo1 = ["Hello, how are you?",
          "As good as I can be. What about you?",
          "I'm good! I've had quite a day.",
          "I can discuss topics such as the 'Confederate States', the 'American Union', 'Lincoln's Speeches', 'Abraham's Position,' the '54th Regiment,' and more! To learn about any of these 5 subjects, type the word or phrase in quotes."]

convo2 = ["Confederate States",
          "Would you like to learn more about the Confederacy? Type '1.1' to skip or exit.",
          "Yes",
          "When the Southern states split from the Union, they created their own country. It was originally named the Confederate States of America, but its shortened name (which is more commonly known) was the Confederacy. Was that helpful?",
          "Who was the president?",
          "The president was a Mississippi (Southern) politician named Jefferson Davis! While Republican Abraham Lincoln led the Union, Democrat Jefferson Davis ran the Confederacy. Being a country with a 'shortened lifespan,' its first and last president lost power following the war's end. Was that helpful?",
          "What happened to the Confederacy at the end of the Civil War?",
          "Eventually, the Union wore down the Confederacy so much that they had not choice but to surrender. They lost. Was that helpful?",
          "Does the Confederacy still exist?",
          "Thankfully, no, not anymore.",
          "1.1",
          "I can discuss topics such as the 'Confederate States', the 'American Union', 'Lincoln's Speeches', 'Abraham's Position,' the '54th Regiment,' and more! To learn about any of these 5 subjects, type the word or phrase in quotes."]
convo3 = ["American Union",
          "Can I tell you about the Union? Type '12' to skip or exit.",
          "Why not!",
          "Before it became the United States of today, the Union (at the time of the Civil War) consisted of Northern states and Border states. Was that helpful?",
          "How did the Union become the United States?",
          "Ultimately, it happened because the Union won the Civil War. With Abraham Lincoln as president throughout, the Union was able to defeat the Confederacy in about 4 years. Was that helpful?",
          "What helped the Union win?",
          "There were many factors that contributed to their victory, but some of the significant factors (at the start) included their strong economy, their overwhelming numbers (of both people and soldiers), their abundance of transportation networks (throughout the states), and their abundance of factories! In an economy like theirs, manufacturing weapons could be done more easily and in great numbers! Was that helpful?",
          "12",
          "I can discuss topics such as the 'Confederate States', the 'American Union', 'Lincoln's Speeches', 'Abraham's Position,' the '54th Regiment,' and more! To learn about any of these 5 subjects, type the word or phrase in quotes."]
         
convo4 = ["Lincoln's Speeches",
          "Do you know which one of Lincoln's speeches addressed equality for all during the Civil War? Was it the his First Inaugural Address, the Emancipation Proclamation, or the Gettysburg Address?. Type '123' to skip or exit.",
          "The First Inaugural Address",
          "Wrong. That leaves the Emancipation Proclamation and the Gettysburg Address! Is this what you were looking for?",
          "Emancipation Proclamation",
          "Nope, but you're close! That leaves the First Inaugural Address and the Gettysburg Address. Is this what you were looking for?",
          "Lincoln's Gettysburg Address?",
          "Ah yes! It was through this speech that Abraham Lincoln spoke of granting equality to all people in all parts of the United States. Being the last of the 3 speeches listed, it was truly when he became determined to set all slaves free. Is this what you were looking for?",
          "What did he say during the First Inaugural Address?",
          "During the First Inaugural Address, Lincoln discussed 3 main topics. These included the South’s secession (after he was elected President in 1860), limiting slavery, & the coming Civil War. While he did plan on stopping slavery's spread, he did not plan on abolishing it (at the time). Was that helpful?",
          "What did Lincoln say during the Emancipation Proclamation?",
          "During the Emancipation Proclamation, Lincoln stated that, should the Confederacy refuse to return to the Union by 1863, all slavery would be abolished there permanently! Nothing would be done (by the Union) to stop those of color from gaining their liberties there, and African Americans were allowed to join the fight (on the side of the Union) now! Was that helpful?",
          "Doesn't that free all slaves?",
          "Unfortunately, the Emancipation Proclamation only applied to the states opposing the Union. It did not include border states, which had slaves, but were fighting with the Union. Was that helpful?",
          "123",
          "I can discuss topics such as the 'Confederate States', the 'American Union', 'Lincoln's Speeches', 'Abraham's Position,' the '54th Regiment,' and more! To learn about any of these 5 subjects, type the word or phrase in quotes."]
convo5 = ["Abraham's Position",
          "Did you know that Abraham Lincoln did not always plan on abolishing slavery? Type '1234' to skip or exit.",
          "How come?",
          "At first, President Lincoln did not feel that he was given the power to abolish slavery, even as president! Besides, he did not feel it was necessary either. Was that helpful?",
          "How unfair!",
          "Abraham Lincoln was not trying to be do anything wrong! He still planned to stop slavery from spreading any further, but just did not expect to free people already in bondage. Plus, the war just started when he felt this way. Was that helpful?",
          "Did his view change?",
          "His view did change. As the war went on, he began to see how necessary abolishing slavery was. Whether it was to rally colored troops, directly hurt the Confederacy, or honor those who died, the Civil War had definitely changed Lincoln in clear ways. Was that helpful?",
          "He did eventually end all slavery correct?",
          "Of course he abolished slavery! Even though MOST slaves were freed by Lincoln's Emancipation Proclamation, ALL slaves were truly freed by the 13th Amendment. This Amendment was passed following the war's end, and banned slavery in America. Was that helpful?",
          "1234",
          "I can discuss topics such as the 'Confederate States', the 'American Union', 'Lincoln's Speeches', 'Abraham's Position,' the '54th Regiment,' and more! To learn about any of these 5 subjects, type the word or phrase in quotes."]
convo6 = ["54th Regiment",
          "After Lincoln's Emancipation Proclamation, a regiment known as the '54th Massachusetts Volunteer Infantry Regiment' was formed, changing the Civil War forever. Would you like to learn more? Type '12345' to skip or exit.",
          "Definitely!",
          "The 54th was important because it was one of the first colored regiments to serve! Was that helpful?",
          "You mean it had African American soldiers?",
          "The 54th was almost a complete African American Regiment! The people in it had been enlisted from places throughout America, and some may have even been Canadian! Even though there were some Caucasian officers in the regiment, this was not the case for most of them! Was that helpful?",
          "What did the 54th do?",
          "Perhaps the most significant thing that the 54th did was lead the assault on July 18th against Fort Wagner. Being followed into battle, the 54th lost their Colonel (Robert Shaw), and nearly half of their men. However, despite this, they continued on even with their devastating losses. Was that helpful?",
          "What effect could the 54th have possibly had?",
          "As a result of the 54th's endurance, bravery, courage, and tenacity, many other colored people were able to follow in their footsteps. At the end of the Civil War, it was recorded that as many as around 200,000 colored men saw battle! (They made up 1/10 of the Union army.) The 54th not only brought those of color to the war, but it also challenged inequality. Was that helpful?",
          "12345",
          "It was nice talking to you about the Civil War!"]
convo7_corpus_history = ["tell me about the american civil war",
                         "do you think the south was right?",
                         "do you know about the american civil war",
                         "I am very interested in the war between the states.",
                         "What is history?",
                         "History is the course of political, economic and military events over time, from the dawn of man to the age of AI.",
                         "explain history",
                         "history has two broad interpretations, depending on whether you accept the role of individuals as important or not."]
trainer.train(convo1)
trainer.train(convo2)
trainer.train(convo3)
trainer.train(convo4)
trainer.train(convo5)
trainer.train(convo6)
trainer = ChatterBotCorpusTrainer(snek)
trainer.train("chatterbot.corpus.english.history")


#Sentiment Value Dictionary with Keys and Values. See sentiment_values.csv
sentiment = open("sentiment_values.csv")
sentiment_value_dictionary = {"value" : 0.00} #0.00 = Key
def get_pair(line):
    key, sep, value = line.strip().partition(",") #Strips \n and makes key, value lists
    return key, value #Returns key, value lists to Dictionary
with open("sentiment_values.csv") as f:
    sentiment_value_dictionary = dict(get_pair(line) for line in f)


#Getting Sentiment Value from user_input. See Line 115.
def get_total_sentiment(user_input):
    global sentiment_value_dictionary
    global a
    a = 0
    user_input = user_input.translate(str.maketrans('', '', string.punctuation)) #Removes punctuation characters "'#@!$%^&*><?/:;{[}]\|""
    words = user_input.lower().split(" ")
    for word in words:
        a += float(sentiment_value_dictionary.get((word), 0.0))
    return a
       
       
def main():       
    #Intro/Greeting
    user_input = input("Enter Name:")
    print("I am Snooter the Civil War Snek, here to teach you about the Civil War!")
    print("To exit, please type the word 'exit'")
    print("Hello, pleasure to meet you!")
    user_input = ""

    #Continues Conversation
    while True:
        x = user_input
        global a
        user_input = input()
        if user_input == "exit":
            print("Conversation Terminated. Hope you learned something new!")
            break
        get_total_sentiment(user_input)
        if a > 1.5:
            snek.learn_response(snek_reply, x)
            print("Yay! So happy to help! :)")
     
        snek_reply = snek.get_response(user_input)
        print(snek_reply)

if __name__ == '__main__':
    main()
'''
#Citations - Thanks to all my sources for the info!

1. National Park Service (2022, May 25). 54th Massachusetts Regiment. National Park Service.
https://www.nps.gov/articles/54th-massachusetts-regiment.htm

2. American Battlefield Trust (2022). Jefferson Davis. American Battlefield Trust.
https://www.battlefields.org/learn/biographies/jefferson-davis

3. History.com Editors (2022, April 28). 13th Amendment. History.
https://www.history.com/topics/black-history/thirteenth-amendment
'''
