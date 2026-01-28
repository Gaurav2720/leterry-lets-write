print ("-----------------HELLO USERRRRRR WASSUP---------------\n")


print("            LETS TAKE A QUICK PERSONALTITY TEST\n")


print("                    AFRAID??????????\n")


choice = input('''                 make achoice brooo.  
                    AFRAID or not ?\n''')
if (choice == 'yes'):
    print("dont worry hota hai hota hai.......")
    pass    
else:
    name = input("enter your name-->")
    print(f"lesss gooo {name}!!!!! just answer some questions and u will get some advice, a personality, maybe a lesson")   

    inference = []

    q1_inference = {
        
        "A": "You are logical, introspective, and love learning and mental challenges.",
        "B": "You are outgoing, fun-loving, and energized by people.",
        "C": "You are imaginative and expressive, thriving in art, music, or ideas.",
        "D": "You are compassionate and empathetic, always ready to support others."
    }

        
    q2_inference = {
        "A": "You value facts and clarity, and make decisions based on reason.",
        "B": "You believe in shared wisdom and value others’ perspectives.",
        "C": "You trust your instincts and let your inner voice guide you.",
        "D": "You are thoughtful and sensitive to the feelings of those around you."
    }


    q3_inference = {
        "A": "You take charge, keep things structured, and guide others.",
        "B": "You bring positivity and keep the group engaged.",
        "C": "You bring fresh ideas and artistic flair to the project.",
        "D": "You’re the backbone, always helping others succeed."
    }

    q4_inference = {
        "A": "You do your best in calm, focused environments.",
        "B": "You love buzz, interactions, and collaborative energy.",
        "C": "You shine when you have space to express yourself and explore ideas.",
        "D": "You need warmth, connection, and emotional understanding."
    }


    q5_inference = {
        "A": "You’re seen as smart, deep, and reliable with advice.",
        "B": "People admire your energy, presence, and self-assurance.",
        "C": "You often think outside the box and bring unique perspectives.",
        "D": "You’re the one friends go to for comfort, care, and honesty."
    }
   
   
   
    print ("QUESTION 1 ::")
    print (''' Q1: What do you enjoy doing the most in your free time?
                    A. Solving puzzles or reading
                    B. Hanging out with friends
                    C. Drawing, writing, or creating
                    D. Helping someone with their problems

    ''')
    option = input ("enter your option-->").strip().upper()

    if (option == 'a'):
            inference.append(q1_inference[option])
    elif (option == 'b'):
            inference.append(q1_inference[option])
    elif (option == 'c'):
            inference.append(q1_inference[option])
    else:
            inference.append(q1_inference[option])


    
    
    
    print('''Q2: How do you usually make decisions?
                A. By thinking logically
                B. By asking others for advice
                C. By going with your gut feeling
                D. By considering how it affects others) ''')


    option = input ("enter your option-->").strip().upper()

    if (option == 'a'):
            inference.append(q2_inference[option])
    elif (option == 'b'):
            inference.append(q2_inference[option])
    elif (option == 'c'):
            inference.append(q2_inference[option])
    else:
            inference.append(q2_inference[option])

    
    
    
    
    print('''Q3: What's your role in a group project?
                A. The planner/organizer
                B. The motivator
                C. The creative contributor
                D. The one who supports everyone

    ''')
    option = input ("enter your option-->").strip().upper()

    if (option == 'a'):
            inference.append(q3_inference[option])
    elif (option == 'b'):
            inference.append(q3_inference[option])
    elif (option == 'c'):
            inference.append(q3_inference[option])
    else:
            inference.append(q3_inference[option])

    
    
    
    
    
    print('''Q4: Which environment do you thrive in?
                A. Structured and quiet
                B. Social and energetic
                C. Free and expressive
                D. Caring and emotionally safe''')


    option = input ("enter your option-->").strip().upper()

    if (option == 'a'):
            inference.append(q4_inference[option])
    elif (option == 'b'):
            inference.append(q4_inference[option])
    elif (option == 'c'):
            inference.append(q4_inference[option])
    else:
            inference.append(q4_inference[option])



  
  
    print('''Q5: What would friends say about you?
                A. Intelligent and focused
                B. Outgoing and confident
                C. Imaginative and deep
                D. Kind and understanding''')


    option = input ("enter your option-->").strip().upper()

    if (option == 'a'):
            inference.append(q5_inference[option])
    elif (option == 'b'):
            inference.append(q5_inference[option])
    elif (option == 'c'):
            inference.append(q5_inference[option])
    else:
            inference.append(q5_inference[option])

print("HERE IS YOUR PERSONALITY CHECK , GOOD LUCCK !!!!1 DO WELL!!!!")
for i, option in enumerate(inference, 1):
    print(f"{i}. {option}")


            