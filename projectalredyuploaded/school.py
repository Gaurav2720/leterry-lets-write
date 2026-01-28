choice = input("enter your choice    ")

if   (choice == 1):
      print('''     1. Leave Application
                    2. Permission Letters
                    3. Application for Transfer Certificate (TC)
                    4. Application for Bonafide Certificate
                    5. Application for Fee Concession
                    6. Application for Change of Subject
                    7. Application for Character Certificate
                    8. Letter for Rechecking Exam Papers
                    9. Complaint Letter to Principal
                    10. Letter from Parent to Principal
                    11. Consent Letter for School Events or Tours
                    12. Teacher's Resignation Letter
                    13. Letter from Teacher to Parents (Progress or Discipline)
                    14. Recommendation Letter by Teacher for Student''')
      
     
      type  = input ("enter the type of letter --->")
     
if   (type  == '1'):
    print('''   A. Sick Leave
                B. Urgent Work Leave
                C. Family Emergency Leave''')

    which_type = input("enter the type , select abc = ")

    if (which_type == 'a'):
        your_name = input("enter your name to be displayed = ")
        principal_name = input("enter your principal's first name = ")
        date = input("date month, year = ")
        Class = input("enter your class in roman numbers = ")
        roll_no = int(input("enter your roll number or enrollment number = "))
        reason = input("enter the reason if required, you can even leave it blank, your wish = ")
        leave_start_date = input("enter when will the leave start = ")
        leave_end_date = input("when will the leave end = ")
        illness = input("what's your illness = ")
        illness_start_date = input("when did your illness start = ")
        number_of_days = input("enter the number of days = ")
        print(f'''Subject: Application for Sick Leave
              Dear {principal_name},
              I am {your_name}, a student of Class {Class} in your school. I have been suffering from {illness} since {illness_start_date} and have been advised by my doctor to take rest for {number_of_days} days.
              Kindly grant me leave from {leave_start_date} to {leave_end_date}. I will make sure to catch up on missed lessons.
              Thank you for your consideration.
              Sincerely,
              {your_name}
              {roll_no}
              {date}''')

    elif (which_type == 'b'):
        your_name = input("enter your name to be displayed = ")
        principal_name = input("enter your principal's first name = ")
        date = input("date month, year = ")
        Class = input("enter your class in roman numbers = ")
        number_of_days = input("enter the number of days = ")
        leave_start_date = input("enter the leave starting date = ")
        leave_end_date = input("enter the leave ending date = ")
        roll_no = int(input("enter your roll number or enrollment number = "))

        print(f'''Subject: Application for Urgent Work Leave
            Dear {principal_name},
            I, {your_name}, a student of Class {Class}, request leave for {number_of_days} days from {leave_start_date} to {leave_end_date} due to an urgent family matter that requires my presence.
            I will complete all pending assignments upon my return. Kindly approve my leave.
            Sincerely,
            {your_name}
            {roll_no}
            {date}''')

    elif (which_type == 'c'):
        your_name = input("enter your name to be displayed = ")
        principal_name = input("enter your principal's first name = ")
        date = input("date month, year = ")
        roll_no = int(input("enter your roll number or enrollment number = "))
        leave_start_date = input("enter start date = ")
        leave_end_date = input("enter end date = ")
        print(f'''Subject: Application for Family Emergency Leave
                Dear {principal_name},
                I am writing to inform you that due to a family emergency, I will not be able to attend school from {leave_start_date} to {leave_end_date}.
                I kindly request your approval for this leave. I will ensure that I cover the missed syllabus.
                Sincerely,
                {your_name}
                {roll_no}
                {date}''')

elif (type  == '2'):
        print(''' A. For School Trip
              B. For Special Classes/Competitions
              C. For Library or Extra Facilities''')

elif (type  == '3'):
    your_name = input("enter your name to be displayed = ")
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    roll_no = int(input("enter your roll number or enrollment number = "))
    Class = input("enter the class you are in = ")

    print(f'''
            Subject: Request for Transfer Certificate
            Dear {principal_name} sir,
            I, {your_name}, a student of Class {Class}, Roll No. {roll_no}, request a Transfer Certificate as my family is relocating to [new city]. Kindly process my TC at the earliest.
            Sincerely,
            {your_name}
            {date}''')

elif (type  == '4'):
    your_name = input("enter your name to be displayed = ")
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    roll_no = int(input("enter your roll number or enrollment number = "))
    Class = input("enter the class you are in = ")
    reason = input("enter the reason if required, you can even leave it blank, your wish = ")

    print(f'''Subject: Request for Bonafide Certificate
              Dear {principal_name} sir,
              I, {your_name}, a student of Class {Class}, require a Bonafide Certificate for {reason}. Kindly issue the certificate at your earliest convenience.
              Sincerely,
              {your_name}
              {roll_no}
              {date}''')

elif (type  == '5'):
    your_name = input("enter your name to be displayed = ")
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    roll_no = int(input("enter your roll number or enrollment number = "))
    Class = input("enter the class you are in = ")

    print(f'''Subject: Request for Fee Concession
              Dear Principal {principal_name},
              I, {your_name}, a student of Class {Class}, come from a financially constrained background. I kindly request a fee concession to continue my education.
              Attached are the necessary documents for verification.
              Sincerely,
              {your_name}
              {roll_no}
              {date}''')

elif (type  == '6'):
    your_name = input("enter your name to be displayed = ")
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    roll_no = int(input("enter your roll number or enrollment number = "))
    Class = input("enter the class you are in = ")
    current_subject = input("enter the current subject = ")
    new_subject = input("enter the new subject = ")
    reason = input("enter the reason if required, you can even leave it blank, your wish = ")

    print(f'''Subject: Request for Subject Change
              Dear Principal {principal_name},
              I, {your_name}, {Class}, wish to change my elective subject from {current_subject} to {new_subject} due to {reason}. Kindly approve my request.
              Sincerely,
              {your_name}
              {roll_no}
              {date}''')

elif (type  == '7'):
    reason = input("enter the reason if required, you can even leave it blank, your wish = ")
    your_name = input("enter your name to be displayed = ")
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    roll_no = int(input("enter your roll number or enrollment number = "))
    Class = input("enter the class you are in = ")

    print(f'''Subject: Request for Character Certificate
          Dear Principal {principal_name},
          I, {your_name}, a student of Class {Class}, require a Character Certificate for {reason}. Kindly issue it at the earliest.
          Sincerely,
          {your_name}
          {roll_no}
          {date}''')

elif (type  == '8'):
    your_name = input("enter your name to be displayed = ")
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    roll_no = int(input("enter your roll number or enrollment number = "))
    subject = input("enter the subject = ")

    print(f'''Subject: Request for Re-evaluation of Answer Sheet
              Dear Principal {principal_name},
              I, {your_name}, Roll No. {roll_no}, request a rechecking of my {subject} exam paper as I believe there may be an error in marking. Kindly process my request.
              Sincerely,
              {your_name}
              {date}''')

elif (type  == '9'):
    print('''A. Regarding Bullying
              B. Regarding Teacher Behavior
              C. Regarding Infrastructure''')

elif (type  == '10'):
    print('''A. Health Issue
              B. Feedback or Concerns
              C. Special Requests''')

elif (type  == '11'):
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    roll_no = int(input("enter your roll number or enrollment number = "))
    Class = input("enter the class you are in = ")
    parent_name = input("enter parent name = ")
    child_name = input("enter child's name = ")
    event_name = input("enter the event name = ")
    event_date = input("enter event date = ")
    contact_number = int(input("enter your contact number = "))

    print(f'''     Subject: Consent Letter for {event_name}       
          Dear Principal {principal_name},
          I, {parent_name}, grant permission for my child, {child_name}, to participate in {event_name} on {event_date}. I understand all safety measures will be followed.
          Sincerely,
          {parent_name}
          {contact_number}
          {date}''')

elif (type  == '12'):
    your_name = input("enter your name to be displayed = ")
    principal_name = input("enter your principal's first name = ")
    date = input("date month, year = ")
    designation = input("enter your designation = ")
    last_date = input("enter the last date = ")

    print(f'''Subject: Resignation Letter
              Dear Principal {principal_name},
              I, {your_name}, hereby resign from my position as {designation} effective {last_date}. Thank you for the opportunity.
              Sincerely,
              {your_name}
              {date}''')

elif (type  == '13'):
    parent_name = input("enter parent name = ")
    student_name = input("enter student name = ")
    academic_behavioral = input("enter the issue = ")
    teacher_name = input("enter teacher name = ")
    school_name = input("enter the name of school = ")
    date = input("enter the date = ")

    print(f'''        Subject: Concern About {student_name}'s Progress
            Dear {parent_name},
            I wish to discuss your child's {academic_behavioral} progress. Kindly schedule a meeting at your earliest convenience.
            Sincerely,
            {teacher_name}
            {school_name}
            {date}''')

elif (type  == '14'):
    school_name = input("enter the name of school = ")
    opportunity = input("enter the opportunity = ")
    teacher_name = input("enter teacher name = ")
    school_name = input("enter school name = ")
    he_she = input("specify the pronoun = ")
    student_name = input("enter student name = ")
    recipient_name = input("enter the recipient name = ")
    date = input("enter the date = ")

    print(f'''Subject: Letter of Recommendation for {student_name}
            Dear {recipient_name},
            I highly recommend {student_name} for {opportunity}. {he_she} is hardworking and deserving.
            Sincerely,
            {teacher_name}
            {school_name}
            {date}''')

else :
    pass
