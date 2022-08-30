qna = {
    'hello' : 'hi',
    'what is your name' : 'My name is Ansari Bot ! 😜',
    'how are you' : 'I am fine, How are You ?',
    'how old are you' : "I am a Bot and I don't know my age .."
}
while True:
    try:
        ques = input()
        if ques == 'quit':
            break
        else:
            print(qna[ques])
    except:
        print("I don't know ")