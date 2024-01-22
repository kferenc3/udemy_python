"""
Exercise: building a quiz system
In the last lecture, we learned how to open, read from, and write to a file with Python. It allows us to access and store data in permanent storage.
In this exercise, we challenge you to build something useful: a quiz system, using what we've just learnt.
Our quiz system will load data from a text file named questions.txt, whose format is like this:

1+1=2
2+2=4
7-4=3
As you can tell, each line represents a Q&A, where questions and answer are separated by a =.

Your application must:
Load the Q&As from questions.txt.
For each Q&A, prompt the user with the question and expect an input from the user as the answer before moving to the next question.
For example, for the sample file provided above, it should print out 1+1=, and then wait for the user input their answer.
You need to keep track of the answers, and after the user answers all the questions, you need to store their grade into a file named result.txt.
The format of the grade should be Your final score is {n}/{m}., where {n} and {m} should be replaced by the number of correct answers and total number of questions respectively.
Please try to run your script in your IDE or via terminal to see if it works before submitting the code—we have provided a sample questions.txt  for you to look at.
Once you finish this exercise, take a moment to think about where you can go from this project, we're sure you'll come up with some more excellent ideas!
Happy coding!
"""
with open('questions.txt', 'r') as f:
    qanda = {q: a for q,a in [x.strip().split('=') for x in f.readlines()]}

total = len(qanda)
result = 0

for question, answer in qanda.items():
    user_answ = input(f'What is the result of the following?\n{question}=')
    if user_answ == answer:
        result += 1

res = f'Your final score is {result}/{total}'
print(res)
f = open('results.txt', '+w')
f.write(res)
f.close()