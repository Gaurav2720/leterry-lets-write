print("welcome! to lettery!! ")

print('''Types of Letters (School, College, Corporate, Government''')

print('''      
                1-->SCHOOL-RELATED LETTERS
                2-->COLLEGE-RELATED LETTERS
                3-->CORPORATE / OFFICE LETTERS
                4-->GOVERNMENT-RELATED LETTERS
                5-->MISCELLANEOUS LETTERS
''')
choice = int (input("enter your choise --> "))

if(choice == 1):
    
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
     
    if(type  == '1'):
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

if (choice == 2):
    print('''     1. Leave Application
                    2. Internship Request Letter
                    3. Recommendation Request Letter (for higher studies or job)
                    4. Application for Fee Refund
                    5. Application for Fee Payment Extension
                    6. Application for Hostel Accommodation
                    7. Application for Change of Subject/Course
                    8. Application for Bonafide Certificate
                    9. Application for Scholarship/Financial Aid
                    10. Letter to HoD or Dean
                    11. Complaint Letter in College
                    12. Letter for Campus Placement Eligibility
                    13. Project Submission Cover Letter
                    14. Staff Resignation Letter (College Faculty)
                    15. Application for College Transfer''')
      
    type = input("enter the type of letter --->")
     
    if (type == '1'):
        print('''   A. Medical Leave
                    B. Exam Leave
                    C. Emergency Leave''')

        which_type = input("enter the type, select abc = ")

        if (which_type == 'a'):
            your_name = input("enter your name to be displayed = ")
            deans = input("enter your deans name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number or enrollment number = ")
            department = input("enter your department = ")
            reason = input("enter the reason if required = ")
            leave_start_date = input("enter when will the leave start = ")
            leave_end_date = input("when will the leave end = ")
            illness = input("what's your illness = ")
            number_of_days = input("enter the number of days = ")
            print(f'''Subject: Application for Medical Leave
    Dear {deans},
    I am {your_name}, a student of {department} in your college. I have been suffering from {illness} and have been advised by my doctor to take rest for {number_of_days} days.
    Kindly grant me leave from {leave_start_date} to {leave_end_date}. I will make sure to catch up on missed work.
    Thank you for your consideration.
    Sincerely,
    {your_name}
    {roll_no}
    {date}''')

        elif (which_type == 'b'):
            your_name = input("enter your name to be displayed = ")
            deans = input("enter your deans name = ")
            date = input("date month, year = ")
            department = input("enter your department = ")
            roll_no = input("enter your roll number or enrollment number = ")
            exam_name = input("enter exam name = ")
            leave_start_date = input("enter the leave starting date = ")
            leave_end_date = input("enter the leave ending date = ")

            print(f'''Subject: Application for Exam Leave
    Dear {deans},
    I, {your_name}, a student of {department}, request leave from {leave_start_date} to {leave_end_date} to prepare for my {exam_name} exams.
    I will complete all pending assignments upon my return. Kindly approve my leave.
    Sincerely,
    {your_name}
    {roll_no}
    {date}''')

        elif (which_type == 'c'):
            your_name = input("enter your name to be displayed = ")
            deans = input("enter your deans name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number or enrollment number = ")
            department = input("enter your department = ")
            leave_start_date = input("enter start date = ")
            leave_end_date = input("enter end date = ")
            emergency_details = input("briefly describe the emergency = ")
            print(f'''Subject: Application for Emergency Leave
    Dear {deans},
    I am writing to inform you that due to {emergency_details}, I will not be able to attend college from {leave_start_date} to {leave_end_date}.
    I kindly request your approval for this leave. I will ensure that I cover the missed work.
    Sincerely,
    {your_name}
    {roll_no}
    {department}
    {date}''')

    elif (type == '2'):
        your_name = input("enter your name to be displayed = ")
        deans = input("enter principal/HoD's name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        company_name = input("enter company name = ")
        internship_duration = input("enter internship duration = ")
        internship_period = input("enter internship period (dates) = ")
        
        print(f'''Subject: Request for Internship Permission
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, wish to apply for an internship at {company_name} for {internship_duration} during {internship_period}.
    Kindly grant me permission to pursue this opportunity which will enhance my practical knowledge.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '3'):
        your_name = input("enter your name to be displayed = ")
        professor_name = input("enter professor's name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        purpose = input("enter purpose (higher studies/job) = ")
        institution_name = input("enter institution/company name = ")
        
        print(f'''Subject: Request for Recommendation Letter
    Dear Professor {professor_name},
    I, {your_name}, {roll_no}, {department}, am applying for {purpose} at {institution_name}. 
    I would be grateful if you could write me a recommendation letter highlighting my academic performance and skills.
    Thank you for your support.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '4'):
        your_name = input("enter your name to be displayed = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        amount = input("enter fee amount = ")
        reason = input("enter reason for refund = ")
        
        print(f'''Subject: Request for Fee Refund
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, request a refund of {amount} paid towards {reason}. 
    Attached are the relevant payment receipts for your reference.
    Kindly process the refund at the earliest.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '5'):
        your_name = input("enter your name to be displayed = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        new_date = input("enter proposed payment date = ")
        reason = input("enter reason for extension = ")
        
        print(f'''Subject: Request for Fee Payment Extension
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, request an extension until {new_date} to pay my fees due to {reason}.
    I assure you the payment will be made by the proposed date. Kindly consider my request.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '6'):
        your_name = input("enter your name to be displayed = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        academic_year = input("enter academic year = ")
        preference = input("enter hostel preference (AC/Non-AC) = ")
        
        print(f'''Subject: Application for Hostel Accommodation
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, request hostel accommodation for the academic year {academic_year}.
    I prefer {preference} accommodation and have attached all required documents. Kindly approve my application.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '7'):
        your_name = input("enter your name to be displayed = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        current_subject = input("enter current subject/course = ")
        new_subject = input("enter new subject/course = ")
        reason = input("enter reason for change = ")
        
        print(f'''Subject: Request for Subject/Course Change
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, request to change from {current_subject} to {new_subject} due to {reason}.
    Kindly approve this change at the earliest. Attached are supporting documents if required.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '8'):
        your_name = input("enter your name to be displayed = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        purpose = input("enter purpose for certificate = ")
        
        print(f'''Subject: Request for Bonafide Certificate
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, require a Bonafide Certificate for {purpose}.
    Kindly issue the certificate at your earliest convenience.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '9'):
        your_name = input("enter your name to be displayed = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        family_income = input("enter approximate family income = ")
        reason = input("enter reason for financial aid = ")
        
        print(f'''Subject: Application for Scholarship/Financial Aid
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, come from a family with annual income of {family_income}. 
    I request financial assistance/scholarship to continue my education due to {reason}.
    Attached are all required income documents. Kindly consider my application.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '10'):
        print('''A. Academic Issues
    B. Course Grievance
    C. Lab or Project Support''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            hod_name = input("enter HoD's name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number = ")
            department = input("enter your department = ")
            issue = input("describe your academic issue = ")
            
            print(f'''Subject: Regarding Academic Issue
    Dear Dr. {hod_name},
    I, {your_name}, {roll_no}, {department}, wish to bring to your attention that {issue}.
    I would appreciate your guidance in resolving this matter at the earliest.
    Sincerely,
    {your_name}
    {date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            hod_name = input("enter HoD's name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number = ")
            department = input("enter your department = ")
            course_name = input("enter course name = ")
            grievance = input("describe your grievance = ")
            
            print(f'''Subject: Grievance Regarding {course_name}
    Dear Dr. {hod_name},
    I, {your_name}, {roll_no}, {department}, would like to formally register my concern about {grievance} in {course_name}.
    I request your intervention to address this issue appropriately.
    Sincerely,
    {your_name}
    {date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            hod_name = input("enter HoD's name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number = ")
            department = input("enter your department = ")
            project_name = input("enter project name = ")
            requirements = input("list your lab/project requirements = ")
            
            print(f'''Subject: Request for Project Support
    Dear Dr. {hod_name},
    I, {your_name}, {roll_no}, {department}, working on {project_name}, require {requirements} to complete my project successfully.
    Kindly approve the necessary support at the earliest.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '11'):
        print('''A. About Ragging
    B. Faculty Behavior
    C. Infrastructure Issues''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            deans = input("enter deans name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number = ")
            department = input("enter your department = ")
            incident_details = input("describe the ragging incident = ")
            
            print(f'''Subject: Formal Complaint About Ragging
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, wish to formally report a ragging incident where {incident_details}.
    I request immediate action to prevent such incidents in future while maintaining my anonymity.
    Sincerely,
    {your_name}
    {date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            deans = input("enter deans name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number = ")
            department = input("enter your department = ")
            faculty_name = input("enter faculty name = ")
            issue = input("describe the behavior issue = ")
            
            print(f'''Subject: Complaint Regarding Faculty Behavior
    Dear {deans},
    I, {your_name}, {roll_no}, {department}, wish to bring to your notice that {faculty_name} has been {issue}.
    I request you to address this matter appropriately while maintaining confidentiality.
    Sincerely,
    {your_name}
    {date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            deans = input("enter deans name = ")
            date = input("date month, year = ")
            roll_no = input("enter your roll number = ")
            department = input("enter your department = ")
            infrastructure_issue = input("describe the infrastructure problem = ")
            location = input("enter location of issue = ")
            
            print(f'''Subject: Complaint About Infrastructure
    Dear {deans},
    I wish to bring to your attention the poor condition of {location} where {infrastructure_issue}.
    As a student of {department}, I request immediate action to resolve this issue for better academic environment.
    Sincerely,
    {your_name}
    {roll_no}
    {date}''')

    elif (type == '12'):
        your_name = input("enter your name = ")
        placement_officer = input("enter placement officer's name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        cgpa = input("enter your CGPA = ")
        skills = input("list your key skills = ")
        
        print(f'''Subject: Request for Campus Placement Eligibility
    Dear Mr./Ms. {placement_officer},
    I, {your_name}, {roll_no}, {department} with CGPA {cgpa}, possess skills in {skills}.
    I request you to consider my profile for upcoming campus placements and notify me of relevant opportunities.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '13'):
        your_name = input("enter your name = ")
        professor_name = input("enter professor's name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        project_title = input("enter project title = ")
        submission_date = input("enter submission date = ")
        
        print(f'''Subject: Project Submission - {project_title}
    Dear Professor {professor_name},
    Please find attached my project titled "{project_title}" submitted for evaluation on {submission_date}.
    I, {your_name}, {roll_no}, {department}, declare that this is my original work.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '14'):
        your_name = input("enter your name = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        department = input("enter your department = ")
        designation = input("enter your designation = ")
        last_working_day = input("enter last working day = ")
        reason = input("enter reason for resignation = ")
        
        print(f'''Subject: Resignation Letter
    Dear {deans},
    I, {your_name}, {designation} of {department}, hereby submit my resignation effective {last_working_day} due to {reason}.
    I appreciate the opportunities provided during my tenure. Please let me know the formalities to complete.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '15'):
        your_name = input("enter your name = ")
        deans = input("enter deans name = ")
        date = input("date month, year = ")
        roll_no = input("enter your roll number = ")
        department = input("enter your department = ")
        current_college = input("enter current college = ")
        new_college = input("enter new college = ")
        reason = input("enter reason for transfer = ")
        
        print(f'''Subject: Application for College Transfer
    Dear {deans},
    I, {your_name}, {roll_no}, {department} at {current_college}, request a transfer to {new_college} due to {reason}.
    Kindly process my transfer certificate and necessary documents at the earliest.
    Sincerely,
    {your_name}
    {date}''')

    else:
        pass

if (choice == 3):
    print('''     1. Leave Application
                    2. Resignation Letter
                    3. Job Application Letter
                    4. Transfer Request Letter
                    5. Promotion Request Letter
                    6. Grievance Letter (Workplace issues)
                    7. Response to Warning Letter
                    8. Experience Certificate Request Letter
                    9. Recommendation Request Letter
                    10. Offer Letter (Employer to Candidate)
                    11. Appointment Letter
                    12. Promotion Letter (from HR/Manager)
                    13. Warning Letter (from HR/Manager)
                    14. Termination Letter
                    15. Salary Revision Request Letter
                    16. Work-from-Home Request Letter
                    17. Relieving Letter Request
                    18. Internship Completion Certificate Letter
                    19. Joining Letter (by selected candidate)''')
      
    type = input("enter the type of letter --->")
     
    if (type == '1'):
            print('''   A. Sick Leave
                        B. Casual Leave
                        C. Maternity/Paternity Leave
                        D. Emergency Leave''')

            which_type = input("enter the type, select abcd = ")

            if (which_type == 'a'):
                your_name = input("enter your name = ")
                manager_name = input("enter manager's name = ")
                date = input("date month, year = ")
                employee_id = input("enter your employee ID = ")
                department = input("enter your department = ")
                leave_start_date = input("enter leave start date = ")
                leave_end_date = input("enter leave end date = ")
                illness = input("enter illness/medical condition = ")
                doctor_advice = input("is there doctor's advice? (yes/no) = ")
                print(f'''Subject: Application for Sick Leave
        Dear {manager_name},
        I am writing to inform you that I am suffering from {illness} and my doctor has advised {doctor_advice} me to take rest. 
        I request you to kindly grant me sick leave from {leave_start_date} to {leave_end_date}.
        I will keep you updated about my health status and will submit the medical certificate upon joining.
        Sincerely,
        {your_name}
        {employee_id}
        {department}
        {date}''')

            elif (which_type == 'b'):
                your_name = input("enter your name = ")
                manager_name = input("enter manager's name = ")
                date = input("date month, year = ")
                employee_id = input("enter your employee ID = ")
                department = input("enter your department = ")
                leave_dates = input("enter leave dates = ")
                reason = input("enter reason for casual leave = ")
                print(f'''Subject: Application for Casual Leave
        Dear {manager_name},
        I request you to grant me casual leave on {leave_dates} due to {reason}.
        I have completed all my pending work and will be available on phone if needed.
        Kindly approve my leave application.
        Regards,
        {your_name}
        {employee_id}
        {department}
        {date}''')

            elif (which_type == 'c'):
                your_name = input("enter your name = ")
                manager_name = input("enter manager's name = ")
                date = input("date month, year = ")
                employee_id = input("enter your employee ID = ")
                department = input("enter your department = ")
                leave_start_date = input("enter leave start date = ")
                leave_end_date = input("enter leave end date = ")
                type_leave = input("maternity/paternity leave? = ")
                print(f'''Subject: Application for {type_leave} Leave
        Dear {manager_name},
        I am writing to formally apply for {type_leave} leave from {leave_start_date} to {leave_end_date} as per company policy.
        I have attached all the required documents for your reference. 
        Kindly process my leave application at the earliest.
        Sincerely,
        {your_name}
        {employee_id}
        {department}
        {date}''')

            elif (which_type == 'd'):
                your_name = input("enter your name = ")
                manager_name = input("enter manager's name = ")
                date = input("date month, year = ")
                employee_id = input("enter your employee ID = ")
                department = input("enter your department = ")
                emergency_details = input("briefly describe the emergency = ")
                leave_dates = input("enter leave dates required = ")
                print(f'''Subject: Emergency Leave Application
        Dear {manager_name},
        Due to an unexpected emergency situation ({emergency_details}), I need to take leave on {leave_dates}.
        I sincerely apologize for the short notice and will complete any pending work as soon as possible.
        Kindly approve my emergency leave request.
        Regards,
        {your_name}
        {employee_id}
        {department}
        {date}''')

    elif (type == '2'):
            your_name = input("enter your name = ")
            manager_name = input("enter manager's name = ")
            date = input("date month, year = ")
            employee_id = input("enter your employee ID = ")
            department = input("enter your department = ")
            last_working_day = input("enter last working day = ")
            reason = input("enter reason for resignation (optional) = ")
            print(f'''Subject: Resignation Letter
        Dear {manager_name},
        Please accept this letter as formal notification of my resignation from my position as [Your Designation] at [Company Name].
        My last working day will be {last_working_day}. {reason if reason else ''}
        I appreciate the opportunities I've had during my time here and am grateful for the support provided.
        Please let me know how I can help with the transition process.
        Sincerely,
        {your_name}
        {employee_id}
        {department}
        {date}''')

    elif (type == '3'):
        your_name = input("enter your name = ")
        hiring_manager = input("enter hiring manager's name = ")
        date = input("date month, year = ")
        position = input("enter position applying for = ")
        company = input("enter company name = ")
        experience = input("enter your relevant experience = ")
        skills = input("enter your key skills = ")
        print(f'''Subject: Application for {position} Position
    Dear {hiring_manager},
    I am excited to apply for the {position} position at {company}. With {experience} of experience and skills in {skills}, I believe I would be a valuable addition to your team.
    Attached is my resume for your review. I would welcome the opportunity to discuss how my qualifications align with your needs.
    Thank you for your time and consideration.
    Sincerely,
    {your_name}
    {date}''')

    elif (type == '4'):
        your_name = input("enter your name = ")
        manager_name = input("enter manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter current department = ")
        current_location = input("enter current location = ")
        requested_location = input("enter requested location = ")
        reason = input("enter reason for transfer = ")
        print(f'''Subject: Request for Transfer to {requested_location}
    Dear {manager_name},
    I am writing to formally request a transfer from {current_location} to {requested_location} due to {reason}.
    I believe this transfer will enable me to continue contributing effectively while addressing my personal circumstances.
    I would appreciate your positive consideration of this request.
    Thank you for your time.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '5'):
        your_name = input("enter your name = ")
        manager_name = input("enter manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        current_designation = input("enter current designation = ")
        requested_designation = input("enter requested designation = ")
        achievements = input("list your key achievements = ")
        print(f'''Subject: Request for Promotion to {requested_designation}
    Dear {manager_name},
    I am writing to formally request consideration for promotion to the position of {requested_designation}.
    During my tenure as {current_designation}, I have {achievements}. I believe my contributions and skills warrant this progression.
    I would appreciate the opportunity to discuss this request with you.
    Thank you for your consideration.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '6'):
        your_name = input("enter your name = ")
        hr_manager = input("enter HR manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        issue = input("describe the workplace issue = ")
        solution = input("suggest possible solution = ")
        print(f'''Subject: Formal Grievance Regarding {issue}
    Dear {hr_manager},
    I am writing to formally bring to your attention an ongoing workplace issue regarding {issue}.
    I have tried resolving this through regular channels without success. I suggest {solution} as a possible resolution.
    I request your intervention to address this matter appropriately while maintaining confidentiality.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '7'):
        your_name = input("enter your name = ")
        manager_name = input("enter manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        warning_date = input("enter date of warning letter = ")
        response = input("enter your response/explanation = ")
        improvement = input("enter improvement measures taken = ")
        print(f'''Subject: Response to Warning Letter Dated {warning_date}
    Dear {manager_name},
    I am writing in response to the warning letter dated {warning_date}. {response}
    I have taken the following corrective measures: {improvement}
    I appreciate your understanding and assure you of my commitment to meeting all expectations moving forward.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '8'):
        your_name = input("enter your name = ")
        hr_manager = input("enter HR manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        purpose = input("enter purpose for experience certificate = ")
        last_working_day = input("enter last working day (if applicable) = ")
        print(f'''Subject: Request for Experience Certificate
    Dear {hr_manager},
    I request you to kindly issue my experience certificate for the period of my employment at [Company Name]. 
    This certificate is required for {purpose}. My last working day was {last_working_day if last_working_day else '[still employed]'}.
    I would appreciate if you could process this at the earliest.
    Thank you.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '9'):
        your_name = input("enter your name = ")
        colleague_name = input("enter colleague's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        purpose = input("enter purpose for recommendation = ")
        qualities = input("mention qualities to highlight = ")
        print(f'''Subject: Request for Recommendation Letter
    Dear {colleague_name},
    I hope this message finds you well. I am applying for {purpose} and would be honored if you could write me a recommendation letter.
    I believe you can best speak to my {qualities}. Please let me know if you need any additional information.
    Thank you for your time and support.
    Best regards,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '10'):
        hr_name = input("enter HR manager's name = ")
        candidate_name = input("enter candidate's name = ")
        date = input("date month, year = ")
        position = input("enter position offered = ")
        joining_date = input("enter joining date = ")
        salary = input("enter salary offered = ")
        benefits = input("enter key benefits = ")
        print(f'''Subject: Offer Letter for {position} Position
    Dear {candidate_name},
    We are pleased to offer you the position of {position} at [Company Name] with a starting date of {joining_date}.
    Your compensation will be {salary} per [month/year] with benefits including {benefits}.
    Please sign and return this letter by [date] to indicate your acceptance. We look forward to having you on our team.
    Sincerely,
    {hr_name}
    HR Manager
    [Company Name]
    {date}''')

    elif (type == '11'):
        hr_name = input("enter HR manager's name = ")
        employee_name = input("enter employee's name = ")
        date = input("date month, year = ")
        position = input("enter appointed position = ")
        joining_date = input("enter joining date = ")
        reporting_to = input("enter reporting manager = ")
        print(f'''Subject: Appointment Letter for {position}
    Dear {employee_name},
    We are delighted to confirm your appointment as {position} at [Company Name] effective {joining_date}.
    You will be reporting to {reporting_to}. Your compensation and benefits are as per the enclosed details.
    Please sign and return the duplicate of this letter as acknowledgment of your acceptance.
    Welcome aboard!
    Sincerely,
    {hr_name}
    HR Manager
    [Company Name]
    {date}''')

    elif (type == '12'):
        hr_name = input("enter HR manager's name = ")
        employee_name = input("enter employee's name = ")
        date = input("date month, year = ")
        old_position = input("enter previous position = ")
        new_position = input("enter new position = ")
        effective_date = input("enter effective date = ")
        print(f'''Subject: Promotion Letter to {new_position}
    Dear {employee_name},
    We are pleased to inform you of your promotion from {old_position} to {new_position} effective {effective_date}.
    This promotion recognizes your valuable contributions and comes with revised compensation as discussed.
    Congratulations on this achievement! We look forward to your continued success.
    Sincerely,
    {hr_name}
    HR Manager
    [Company Name]
    {date}''')

    elif (type == '13'):
        hr_name = input("enter HR manager's name = ")
        employee_name = input("enter employee's name = ")
        date = input("date month, year = ")
        issue = input("enter performance/conduct issue = ")
        improvement = input("enter expected improvement = ")
        timeline = input("enter improvement timeline = ")
        print(f'''Subject: Warning Letter Regarding {issue}
    Dear {employee_name},
    This letter serves as a formal warning regarding {issue}. Despite previous discussions, the matter persists.
    You are expected to {improvement} within {timeline}. Failure to improve may lead to further disciplinary action.
    We hope to see immediate improvement and are available to support your efforts.
    Sincerely,
    {hr_name}
    HR Manager
    [Company Name]
    {date}''')

    elif (type == '14'):
        hr_name = input("enter HR manager's name = ")
        employee_name = input("enter employee's name = ")
        date = input("date month, year = ")
        last_working_day = input("enter last working day = ")
        reason = input("enter reason for termination = ")
        print(f'''Subject: Termination of Employment
    Dear {employee_name},
    We regret to inform you that your employment with [Company Name] will be terminated effective {last_working_day} due to {reason}.
    You are required to complete the exit formalities including returning company property by [date].
    We wish you success in your future endeavors.
    Sincerely,
    {hr_name}
    HR Manager
    [Company Name]
    {date}''')

    elif (type == '15'):
        your_name = input("enter your name = ")
        manager_name = input("enter manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        current_salary = input("enter current salary = ")
        requested_salary = input("enter requested salary = ")
        justification = input("enter justification for revision = ")
        print(f'''Subject: Request for Salary Revision
    Dear {manager_name},
    I request a salary revision from {current_salary} to {requested_salary} in recognition of {justification}.
    I believe this adjustment reflects my contributions and is in line with industry standards for my role.
    I would appreciate the opportunity to discuss this matter with you.
    Thank you for your consideration.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '16'):
        your_name = input("enter your name = ")
        manager_name = input("enter manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        wfh_days = input("enter requested WFH days = ")
        reason = input("enter reason for WFH request = ")
        assurance = input("enter productivity assurance = ")
        print(f'''Subject: Work-from-Home Request for {wfh_days}
    Dear {manager_name},
    I request permission to work from home on {wfh_days} due to {reason}. 
    I assure you that {assurance} and will remain available during working hours.
    Kindly approve this arrangement.
    Thank you.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '17'):
        your_name = input("enter your name = ")
        hr_name = input("enter HR manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        last_working_day = input("enter last working day = ")
        print(f'''Subject: Request for Relieving Letter
    Dear {hr_name},
    I request you to kindly issue my relieving letter as my employment with [Company Name] ended on {last_working_day}.
    This document is required for my future employment. I have completed all exit formalities.
    Please process this at the earliest.
    Thank you.
    Sincerely,
    {your_name}
    {employee_id}
    {department}
    {date}''')

    elif (type == '18'):
        your_name = input("enter your name = ")
        manager_name = input("enter manager's name = ")
        date = input("date month, year = ")
        intern_id = input("enter your intern ID = ")
        department = input("enter your department = ")
        internship_duration = input("enter internship duration = ")
        skills_learned = input("enter skills learned = ")
        print(f'''Subject: Request for Internship Completion Certificate
    Dear {manager_name},
    I have successfully completed my internship of {internship_duration} in {department} where I gained experience in {skills_learned}.
    Kindly issue my internship completion certificate at the earliest as I need it for my academic records.
    Thank you for the valuable learning opportunity.
    Sincerely,
    {your_name}
    {intern_id}
    {department}
    {date}''')

    elif (type == '19'):
        your_name = input("enter your name = ")
        hr_name = input("enter HR manager's name = ")
        date = input("date month, year = ")
        employee_id = input("enter your employee ID = ")
        department = input("enter your department = ")
        joining_date = input("enter joining date = ")
        print(f'''Subject: Joining Letter
    Dear {hr_name},
    This is to confirm that I, {your_name}, accept the offer for the position of [Designation] in {department} at [Company Name].
    I will be joining on {joining_date} as per the terms discussed. I have completed all required documentation.
    Looking forward to being part of your team.
    Sincerely,
    {your_name}
    {employee_id}
    {date}''')

    else:
        pass

if (choice == 4):

    print('''     1. RTI Application (Right to Information)
                    2. Public Grievance Letter
                    3. Letter to MLA/MP
                    4. Police Complaint Letter
                    5. Application for Government Certificate
                    6. Application for Government Scheme
                    7. Letter to RTO
                    8. Letter to Passport Office
                    9. Letter to Aadhar/PAN Authorities
                    10. Letter to Collector or District Magistrate
                    11. Letter to Government Ministry
                    12. Letter to Municipality or Local Body''')
    
    type = input("enter the type of letter --->")
    
    if (type == '1'):
        applicant_name = input("enter your name = ")
        address = input("enter your address = ")
        pio_name = input("enter Public Information Officer's name = ")
        department = input("enter department name = ")
        date = input("enter date = ")
        information_requested = input("enter information you are requesting = ")
        fee_details = input("enter RTI fee details if any = ")
        
        print(f'''Subject: RTI Application
To,
The Public Information Officer
{department}

Dear {pio_name},
I, {applicant_name}, resident of {address}, request the following information under the Right to Information Act, 2005:
{information_requested}

I have attached the required fee of {fee_details} with this application. Kindly provide the information within 30 days as mandated by the RTI Act.

Sincerely,
{applicant_name}
{address}
{date}''')

    elif (type == '2'):
        print('''A. Roads/Transport
                B. Water/Electricity
                C. Sanitation/Waste''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            department = input("enter concerned department = ")
            location = input("enter location of issue = ")
            date = input("enter date = ")
            issue_details = input("describe the road/transport issue = ")
            
            print(f'''Subject: Complaint Regarding Road/Transport Issue
To,
The {department}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to bring to your attention the following issue regarding roads/transport at {location}:
{issue_details}

This issue has been persisting for [duration] and is causing inconvenience to the public. Kindly take necessary action at the earliest.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            department = input("enter concerned department = ")
            location = input("enter location of issue = ")
            date = input("enter date = ")
            issue_details = input("describe the water/electricity issue = ")
            
            print(f'''Subject: Complaint Regarding Water/Electricity Issue
To,
The {department}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to bring to your attention the following utility issue at {location}:
{issue_details}

This issue has been affecting our daily life severely. Kindly resolve this matter urgently.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            department = input("enter concerned department = ")
            location = input("enter location of issue = ")
            date = input("enter date = ")
            issue_details = input("describe the sanitation/waste issue = ")
            
            print(f'''Subject: Complaint Regarding Sanitation/Waste Issue
To,
The {department}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to bring to your attention the following sanitation issue at {location}:
{issue_details}

This is creating unhygienic conditions in our area. Kindly take immediate action to resolve this problem.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '3'):
        print('''A. Local Issue Representation
B. Community Request
C. Infrastructure Development''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            mla_mp_name = input("enter MLA/MP name = ")
            constituency = input("enter constituency = ")
            date = input("enter date = ")
            issue_details = input("describe the local issue = ")
            
            print(f'''Subject: Representation Regarding Local Issue
To,
Honorable {mla_mp_name}
MLA/MP of {constituency}

Respected Sir/Madam,
I, {your_name}, resident of {address}, wish to bring to your kind attention the following issue in our locality:
{issue_details}

This matter requires your immediate intervention for resolution. Kindly look into this matter at the earliest.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            organization = input("enter organization name if any = ")
            address = input("enter your address = ")
            mla_mp_name = input("enter MLA/MP name = ")
            constituency = input("enter constituency = ")
            date = input("enter date = ")
            request_details = input("describe the community request = ")
            
            print(f'''Subject: Community Request
To,
Honorable {mla_mp_name}
MLA/MP of {constituency}

Respected Sir/Madam,
On behalf of the residents of {address}, I, {your_name} {organization if organization else ''}, would like to request your support for:
{request_details}

We would be grateful for your assistance in this matter which would benefit our community greatly.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            organization = input("enter organization name if any = ")
            address = input("enter your address = ")
            mla_mp_name = input("enter MLA/MP name = ")
            constituency = input("enter constituency = ")
            date = input("enter date = ")
            project_details = input("describe the infrastructure development needed = ")
            
            print(f'''Subject: Request for Infrastructure Development
To,
Honorable {mla_mp_name}
MLA/MP of {constituency}

Respected Sir/Madam,
I, {your_name} {organization if organization else ''}, on behalf of residents of {address}, would like to bring to your attention the need for infrastructure development in our area:
{project_details}

We request your kind intervention to initiate this much-needed development work in our constituency.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '4'):
        print('''A. Theft or FIR
B. Harassment Complaint
C. Missing Document Complaint''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            police_station = input("enter police station name = ")
            date = input("enter date = ")
            incident_details = input("describe the theft incident = ")
            incident_date = input("enter incident date = ")
            incident_time = input("enter incident time = ")
            items_stolen = input("list stolen items if any = ")
            
            print(f'''Subject: Complaint Regarding Theft
To,
The Station House Officer
{police_station}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to lodge a complaint regarding a theft that occurred on {incident_date} at {incident_time}.
Incident Details:
{incident_details}

Stolen Items:
{items_stolen}

I request you to register an FIR and investigate this matter. Please provide me with a copy of the FIR.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            police_station = input("enter police station name = ")
            date = input("enter date = ")
            incident_details = input("describe the harassment incident = ")
            harasser_details = input("describe the harasser if known = ")
            
            print(f'''Subject: Harassment Complaint
To,
The Station House Officer
{police_station}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to lodge a serious complaint regarding harassment I have been facing:
{incident_details}

Harasser Details:
{harasser_details}

I request immediate action to stop this harassment and ensure my safety.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            police_station = input("enter police station name = ")
            date = input("enter date = ")
            document_details = input("describe the missing document = ")
            last_seen = input("when/where was it last seen = ")
            
            print(f'''Subject: Complaint Regarding Missing Document
To,
The Station House Officer
{police_station}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to report the loss of an important document:
Document Details: {document_details}

Last Seen: {last_seen}

I request you to register this complaint and provide me with a copy of the complaint for my records.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '5'):
        print('''A. Domicile Certificate
B. Caste Certificate
C. Income Certificate''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            father_name = input("enter father's name = ")
            address = input("enter your address = ")
            tehsil = input("enter tehsil = ")
            district = input("enter district = ")
            date = input("enter date = ")
            
            print(f'''Subject: Application for Domicile Certificate
To,
The Tehsildar
{tehsil}, {district}

Dear Sir/Madam,
I, {your_name} s/o {father_name}, resident of {address}, request you to kindly issue me a Domicile Certificate. My details are as follows:

Name: {your_name}
Father's Name: {father_name}
Address: {address}

I have attached all required documents with this application. Kindly process my request at the earliest.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            father_name = input("enter father's name = ")
            caste = input("enter your caste = ")
            address = input("enter your address = ")
            tehsil = input("enter tehsil = ")
            district = input("enter district = ")
            date = input("enter date = ")
            
            print(f'''Subject: Application for Caste Certificate
To,
The Tehsildar
{tehsil}, {district}

Dear Sir/Madam,
I, {your_name} s/o {father_name}, belonging to {caste} caste, resident of {address}, request you to kindly issue me a Caste Certificate. 

I have attached all necessary documents including proof of caste. Kindly process my application at the earliest.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            father_name = input("enter father's name = ")
            address = input("enter your address = ")
            tehsil = input("enter tehsil = ")
            district = input("enter district = ")
            annual_income = input("enter approximate annual income = ")
            date = input("enter date = ")
            
            print(f'''Subject: Application for Income Certificate
To,
The Tehsildar
{tehsil}, {district}

Dear Sir/Madam,
I, {your_name} s/o {father_name}, resident of {address}, with annual income of approximately {annual_income}, request you to kindly issue me an Income Certificate. 

I have attached all required income proofs with this application. This certificate is required for [mention purpose]. Kindly process my request at the earliest.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '6'):
        scheme_name = input("enter scheme name = ")
        your_name = input("enter your name = ")
        father_name = input("enter father's name = ")
        address = input("enter your address = ")
        department = input("enter concerned department = ")
        date = input("enter date = ")
        eligibility = input("enter why you're eligible = ")
        
        print(f'''Subject: Application for {scheme_name} Scheme
To,
The {department}

Dear Sir/Madam,
I, {your_name} s/o {father_name}, resident of {address}, wish to apply for the {scheme_name} scheme as I fulfill the eligibility criteria ({eligibility}).

I have attached all required documents with this application. Kindly process my application and let me know if any further formalities are required.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '7'):
        print('''A. Driving License Issues
B. Vehicle Registration
C. Ownership Transfer''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            dl_number = input("enter DL number if any = ")
            rto_office = input("enter RTO office = ")
            date = input("enter date = ")
            issue_details = input("describe your DL issue = ")
            
            print(f'''Subject: Application Regarding Driving License Issue
To,
The Regional Transport Officer
{rto_office}

Dear Sir/Madam,
I, {your_name}, resident of {address}, holder of Driving License No. {dl_number if dl_number else 'applying for new DL'}, wish to bring to your attention the following issue:
{issue_details}

I request you to kindly resolve this matter at the earliest. I have attached all required documents with this application.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            vehicle_details = input("enter vehicle details = ")
            rto_office = input("enter RTO office = ")
            date = input("enter date = ")
            
            print(f'''Subject: Application for Vehicle Registration
To,
The Regional Transport Officer
{rto_office}

Dear Sir/Madam,
I, {your_name}, resident of {address}, have recently purchased the following vehicle:
{vehicle_details}

I request you to kindly register this vehicle in my name. I have attached all required documents including invoice, insurance, and PUC. Kindly process my application at the earliest.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            vehicle_details = input("enter vehicle details = ")
            registration_no = input("enter registration number = ")
            rto_office = input("enter RTO office = ")
            date = input("enter date = ")
            seller_details = input("enter seller details = ")
            
            print(f'''Subject: Application for Ownership Transfer
To,
The Regional Transport Officer
{rto_office}

Dear Sir/Madam,
I, {your_name}, resident of {address}, have purchased the following vehicle from {seller_details}:
Vehicle: {vehicle_details}
Registration No.: {registration_no}

I request you to kindly transfer the ownership of this vehicle to my name. I have attached all required documents including NOC, sale deed, and insurance. Kindly process my application.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '8'):
        print('''A. Verification Follow-Up
B. Correction in Passport
C. Reissue Request''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            passport_no = input("enter passport number = ")
            address = input("enter your address = ")
            passport_office = input("enter passport office = ")
            date = input("enter date = ")
            application_date = input("enter original application date = ")
            
            print(f'''Subject: Follow-Up on Passport Verification
To,
The Passport Officer
{passport_office}

Dear Sir/Madam,
I, {your_name}, holder of Passport No. {passport_no}, had applied for passport renewal/issuance on {application_date}. 

I would like to follow up on the status of my application as the verification process seems to be delayed. Kindly update me on the current status and any required actions from my side.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            passport_no = input("enter passport number = ")
            address = input("enter your address = ")
            passport_office = input("enter passport office = ")
            date = input("enter date = ")
            correction_details = input("describe the correction needed = ")
            
            print(f'''Subject: Request for Correction in Passport
To,
The Passport Officer
{passport_office}

Dear Sir/Madam,
I, {your_name}, holder of Passport No. {passport_no}, have noticed an error in my passport details:
{correction_details}

I request you to kindly make the necessary corrections and reissue my passport. I have attached all required documents to support my request.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            passport_no = input("enter passport number = ")
            address = input("enter your address = ")
            passport_office = input("enter passport office = ")
            date = input("enter date = ")
            reason = input("enter reason for reissue = ")
            
            print(f'''Subject: Request for Passport Reissue
To,
The Passport Officer
{passport_office}

Dear Sir/Madam,
I, {your_name}, holder of Passport No. {passport_no}, request reissue of my passport due to {reason}.

I have attached all required documents including old passport and supporting documents. Kindly process my application at the earliest.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '9'):
        print('''A. Correction
B. Linking
C. Address Update''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            aadhar_pan = input("enter Aadhar/PAN number = ")
            address = input("enter your address = ")
            office = input("enter concerned office = ")
            date = input("enter date = ")
            correction_details = input("describe the correction needed = ")
            
            print(f'''Subject: Request for Correction in {aadhar_pan[:4]} Document
To,
The Concerned Officer
{office}

Dear Sir/Madam,
I, {your_name}, holder of {aadhar_pan}, request correction in my document for the following details:
{correction_details}

I have attached all required proof documents with this application. Kindly make the necessary corrections and provide me with an updated document.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            aadhar_no = input("enter Aadhar number = ")
            pan_no = input("enter PAN number = ")
            address = input("enter your address = ")
            office = input("enter concerned office = ")
            date = input("enter date = ")
            
            print(f'''Subject: Request for Linking Aadhar and PAN
To,
The Concerned Officer
{office}

Dear Sir/Madam,
I, {your_name}, holder of:
Aadhar No.: {aadhar_no}
PAN No.: {pan_no}

Request you to kindly link my Aadhar and PAN cards. I have attached copies of both documents with this application.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            aadhar_pan = input("enter Aadhar/PAN number = ")
            old_address = input("enter old address = ")
            new_address = input("enter new address = ")
            office = input("enter concerned office = ")
            date = input("enter date = ")
            
            print(f'''Subject: Request for Address Update in {aadhar_pan[:4]}
To,
The Concerned Officer
{office}

Dear Sir/Madam,
I, {your_name}, holder of {aadhar_pan}, have recently shifted from:
Old Address: {old_address}
To New Address: {new_address}

I request you to kindly update my address in your records. I have attached proof of new address with this application.

Sincerely,
{your_name}
{new_address}
{date}''')

    elif (type == '10'):
        your_name = input("enter your name = ")
        address = input("enter your address = ")
        district = input("enter district = ")
        date = input("enter date = ")
        subject = input("enter subject of letter = ")
        content = input("enter details of your request/complaint = ")
        
        print(f'''Subject: {subject}
To,
The District Collector/District Magistrate
{district}

Respected Sir/Madam,
I, {your_name}, resident of {address}, would like to bring the following matter to your kind attention:
{content}

I request your immediate intervention in this matter which is causing hardship to [me/the public]. Kindly take necessary action at the earliest.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '11'):
        print('''A. Internship Request
B. Project Proposal Submission
C. CSR/Funding Request''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            institution = input("enter your institution = ")
            course = input("enter your course = ")
            address = input("enter your address = ")
            ministry = input("enter ministry name = ")
            date = input("enter date = ")
            duration = input("enter preferred internship duration = ")
            
            print(f'''Subject: Application for Internship Opportunity
To,
The {ministry}

Dear Sir/Madam,
I, {your_name}, currently pursuing {course} at {institution}, am writing to express my interest in undertaking an internship with your esteemed ministry for a period of {duration}.

I am particularly interested in [specific area] and believe this internship would provide me valuable exposure to government functioning. I have attached my resume and academic transcripts for your consideration.

I would be grateful for this opportunity and assure you of my sincere efforts during the internship period.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            organization = input("enter your organization = ")
            address = input("enter your address = ")
            ministry = input("enter ministry name = ")
            date = input("enter date = ")
            project_name = input("enter project name = ")
            brief_description = input("enter brief project description = ")
            
            print(f'''Subject: Submission of Project Proposal - {project_name}
To,
The {ministry}

Dear Sir/Madam,
On behalf of {organization}, I, {your_name}, am pleased to submit our project proposal titled "{project_name}" for your kind consideration.

Project Brief:
{brief_description}

We believe this project aligns with your ministry's objectives and would request you to review our detailed proposal attached with this letter. We would be happy to provide any additional information required.

Sincerely,
{your_name}
{organization}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            organization = input("enter your organization = ")
            address = input("enter your address = ")
            ministry = input("enter ministry name = ")
            date = input("enter date = ")
            purpose = input("enter purpose of funding request = ")
            amount = input("enter requested amount if any = ")
            
            print(f'''Subject: Request for CSR Funding/Support
To,
The {ministry}

Dear Sir/Madam,
I, {your_name}, representing {organization}, would like to request your support for our initiative focused on {purpose}.

This project aims to [briefly explain impact]. We would greatly appreciate any CSR funding or support your ministry could provide {amount if amount else ''} to help us achieve our objectives.

We have attached detailed project documents for your perusal and would be happy to make a presentation if required.

Sincerely,
{your_name}
{organization}
{address}
{date}''')

    elif (type == '12'):
        print('''A. Road Repair Request
B. Drainage/Sanitation Issues
C. Public Utility Complaint''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            municipal_office = input("enter municipal office name = ")
            date = input("enter date = ")
            location = input("enter road location = ")
            issue_details = input("describe the road condition = ")
            
            print(f'''Subject: Request for Road Repair
To,
The Commissioner
{municipal_office}

Dear Sir/Madam,
I, {your_name}, resident of {address}, would like to bring to your attention the poor condition of the road at {location}:
{issue_details}

This has been causing inconvenience to residents and needs urgent repair. Kindly take necessary action at the earliest.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            municipal_office = input("enter municipal office name = ")
            date = input("enter date = ")
            location = input("enter location of issue = ")
            issue_details = input("describe the drainage/sanitation issue = ")
            
            print(f'''Subject: Complaint Regarding Drainage/Sanitation Issue
To,
The Commissioner
{municipal_office}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to bring to your attention the following issue at {location}:
{issue_details}

This is creating unhygienic conditions in our area and needs immediate attention. Kindly arrange for necessary action at the earliest.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            municipal_office = input("enter municipal office name = ")
            date = input("enter date = ")
            utility_type = input("enter utility type = ")
            location = input("enter location of issue = ")
            issue_details = input("describe the public utility issue = ")
            
            print(f'''Subject: Complaint Regarding {utility_type} Issue
To,
The Commissioner
{municipal_office}

Dear Sir/Madam,
I, {your_name}, resident of {address}, wish to bring to your attention the following issue with public utilities at {location}:
{issue_details}

This has been causing inconvenience to the residents. Kindly take necessary action to resolve this issue at the earliest.

Sincerely,
{your_name}
{address}
{date}''')

elif (choice == 5):
    
    print('''     1. Apology Letter
                    2. Thank You Letter
                    3. Invitation Letter
                    4. Condolence Letter
                    5. Congratulation Letter
                    6. Letter to Newspaper Editor
                    7. Feedback/Suggestion Letter
                    8. Letter for Volunteering Opportunity
                    9. Letter for NGO or NPO Collaboration
                    10. Letter for Requesting Sponsorship''')
    
    type = input("enter the type of letter --->")
    
    if (type == '1'):
        print('''A. To Teacher
B. To Manager
C. To Friend/Colleague''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            teacher_name = input("enter teacher's name = ")
            date = input("enter date = ")
            mistake = input("enter what you're apologizing for = ")
            
            print(f'''Subject: Apology Letter
Dear {teacher_name},

I am writing to sincerely apologize for {mistake}. I realize my behavior/action was inappropriate and I truly regret it.

I assure you this won't happen again and I will be more mindful in the future. Please accept my heartfelt apology.

Sincerely,
{your_name}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            manager_name = input("enter manager's name = ")
            date = input("enter date = ")
            mistake = input("enter what you're apologizing for = ")
            
            print(f'''Subject: Apology Letter
Dear {manager_name},

Please accept my sincere apologies for {mistake}. I take full responsibility for my actions and understand the inconvenience caused.

I assure you I have learned from this experience and will take all necessary steps to ensure it doesn't happen again. Thank you for your understanding.

Regards,
{your_name}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            recipient_name = input("enter recipient's name = ")
            date = input("enter date = ")
            mistake = input("enter what you're apologizing for = ")
            
            print(f'''Subject: My Sincere Apology
Dear {recipient_name},

I wanted to personally apologize for {mistake}. I feel terrible about it and want you to know how sorry I am.

Our friendship/working relationship means a lot to me, and I hope you can forgive me for this mistake. I'll make sure to be more considerate in the future.

Warm regards,
{your_name}
{date}''')

    elif (type == '2'):
        print('''A. For Interview
B. For Referral
C. For Mentorship''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            interviewer_name = input("enter interviewer's name = ")
            company = input("enter company name = ")
            date = input("enter date = ")
            position = input("enter position interviewed for = ")
            
            print(f'''Subject: Thank You for the Interview Opportunity
Dear {interviewer_name},

I sincerely thank you for taking the time to interview me for the {position} position at {company}. I appreciate the opportunity to learn more about your organization and share my qualifications.

Regardless of the outcome, I enjoyed our conversation and am grateful for the experience. Please don't hesitate to contact me if you need any additional information.

Best regards,
{your_name}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            recipient_name = input("enter recipient's name = ")
            date = input("enter date = ")
            help_received = input("enter what they helped you with = ")
            
            print(f'''Subject: Thank You for Your Referral
Dear {recipient_name},

I wanted to take a moment to sincerely thank you for {help_received}. Your support and recommendation mean a great deal to me.

I truly appreciate you taking the time to help me in this way. Please let me know if I can ever return the favor.

Warm regards,
{your_name}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            mentor_name = input("enter mentor's name = ")
            date = input("enter date = ")
            guidance_received = input("enter what guidance they provided = ")
            
            print(f'''Subject: Thank You for Your Mentorship
Dear {mentor_name},

I am writing to express my deepest gratitude for {guidance_received}. Your mentorship has been invaluable to my personal and professional growth.

Thank you for sharing your wisdom, time, and patience with me. I hope to make you proud by applying all that you've taught me.

With sincere appreciation,
{your_name}
{date}''')

    elif (type == '3'):
        print('''A. For Events
B. For Seminars/Workshops
C. For Personal Occasions''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            organization = input("enter organization name if any = ")
            event_name = input("enter event name = ")
            date_time = input("enter event date and time = ")
            venue = input("enter venue = ")
            rsvp = input("enter RSVP details = ")
            
            print(f'''Subject: Invitation to {event_name}
Dear [Recipient's Name],

We are pleased to invite you to {event_name} organized by {organization if organization else 'us'} on {date_time} at {venue}.

[Brief description about the event and why it's important]

We would be honored by your presence. Kindly RSVP by {rsvp} to confirm your attendance.

Looking forward to seeing you there!

Best regards,
{your_name}
{organization if organization else ''}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            organization = input("enter organization name if any = ")
            seminar_name = input("enter seminar/workshop name = ")
            date_time = input("enter date and time = ")
            venue = input("enter venue = ")
            benefits = input("enter key benefits of attending = ")
            
            print(f'''Subject: Invitation to Attend {seminar_name}
Dear [Recipient's Name],

We cordially invite you to participate in {seminar_name} organized by {organization if organization else 'us'} on {date_time} at {venue}.

This seminar will cover:
{benefits}

Your presence would add great value to this event. Please let us know your availability at your earliest convenience.

Sincerely,
{your_name}
{organization if organization else ''}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            occasion = input("enter occasion = ")
            date_time = input("enter date and time = ")
            venue = input("enter venue = ")
            rsvp = input("enter RSVP details = ")
            
            print(f'''Subject: Invitation to {occasion}
Dear [Recipient's Name],

I am delighted to invite you to celebrate {occasion} with me/my family on {date_time} at {venue}.

[Personal message about why you want them there]

Please RSVP by {rsvp} so we can make necessary arrangements. Looking forward to sharing this special occasion with you!

Warm regards,
{your_name}''')

    elif (type == '4'):
        deceased_name = input("enter deceased name = ")
        relationship = input("enter your relationship to deceased = ")
        bereaved_name = input("enter bereaved person's name = ")
        date = input("enter date = ")
        qualities = input("enter qualities of deceased = ")
        your_name = input("enter your name")
        he_she = input("enter the pronoun he/she?")
        
        print(f'''Subject: Condolence Letter
Dear {bereaved_name},

I was deeply saddened to hear about the passing of {deceased_name}. {qualities} will always be remembered by those whose lives {he_she} touched.

Please accept my heartfelt condolences during this difficult time. If there's anything I can do to support you, please don't hesitate to reach out.

With deepest sympathy,
{your_name}
{date}''')

    elif (type == '5'):
        recipient_name = input("enter recipient's name = ")
        achievement = input("enter the achievement = ")
        date = input("enter date = ")
        your_name = input("enter your name = ")
        
        print(f'''Subject: Congratulations on Your Achievement!
Dear {recipient_name},

I was thrilled to hear about your recent accomplishment - {achievement}! This is a testament to your hard work and dedication.

Please accept my warmest congratulations on this well-deserved success. Wishing you continued achievements in all your future endeavors.

Best regards,
{your_name}
{date}''')

    elif (type == '6'):
        print('''A. On Public Issue
B. On Awareness Campaign
C. On Social Concern''')
        
        which_type = input("enter the type, select abc = ")
        
        if (which_type == 'a'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            date = input("enter date = ")
            issue = input("enter the public issue = ")
            concerns = input("enter your concerns = ")
            suggestions = input("enter your suggestions = ")
            
            print(f'''Subject: Regarding {issue}
To,
The Editor
[Newspaper Name]

Dear Editor,

I am writing to bring attention to the pressing issue of {issue} in our community. {concerns}

{suggestions}

I hope through your esteemed publication, this matter receives the attention it deserves from authorities and the public alike.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'b'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            date = input("enter date = ")
            campaign = input("enter awareness campaign = ")
            importance = input("enter why it's important = ")
            
            print(f'''Subject: Need for Awareness About {campaign}
To,
The Editor
[Newspaper Name]

Dear Editor,

I wish to highlight through your newspaper the importance of {campaign} awareness in our society. {importance}

I request your support in spreading awareness about this crucial issue that affects [target population]. Your platform can make a significant difference in educating the public.

Sincerely,
{your_name}
{address}
{date}''')
            
        elif (which_type == 'c'):
            your_name = input("enter your name = ")
            address = input("enter your address = ")
            date = input("enter date = ")
            concern = input("enter the social concern = ")
            impact = input("enter its impact = ")
            call_to_action = input("enter what should be done = ")
            
            print(f'''Subject: Rising Concern About {concern}
To,
The Editor
[Newspaper Name]

Dear Editor,

I am writing to express my deep concern about the growing problem of {concern} in our society. {impact}

{call_to_action}

I hope your newspaper will help bring this issue to the forefront of public discourse and prompt necessary action.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '7'):
        your_name = input("enter your name = ")
        address = input("enter your address = ")
        date = input("enter date = ")
        product_service = input("enter product/service = ")
        organization = input("enter organization name = ")
        feedback = input("enter your feedback/suggestion = ")
        
        print(f'''Subject: Feedback/Suggestion Regarding {product_service}
To,
The {organization}

Dear Sir/Madam,

I recently [used/experienced] your {product_service} and would like to share my feedback:
{feedback}

I hope you find these suggestions valuable for your continuous improvement efforts. Thank you for your attention to this matter.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '8'):
        your_name = input("enter your name = ")
        address = input("enter your address = ")
        date = input("enter date = ")
        organization = input("enter organization name = ")
        event_cause = input("enter event/cause = ")
        skills = input("enter your relevant skills = ")
        
        print(f'''Subject: Application for Volunteering Opportunity
To,
The {organization}

Dear Volunteer Coordinator,

I am writing to express my interest in volunteering for {event_cause} with your organization. 

With my skills in {skills}, I believe I can contribute meaningfully to your mission. I am available [your availability] and would welcome the opportunity to discuss how I might assist your team.

Thank you for considering my application. I look forward to the possibility of contributing to your important work.

Sincerely,
{your_name}
{address}
{date}''')

    elif (type == '9'):
        your_name = input("enter your name = ")
        your_organization = input("enter your organization = ")
        address = input("enter your address = ")
        date = input("enter date = ")
        ngo_name = input("enter NGO/NPO name = ")
        collaboration_idea = input("enter your collaboration idea = ")
        
        print(f'''Subject: Proposal for Collaboration
To,
The {ngo_name}

Dear [Recipient's Name],

I am writing on behalf of {your_organization} to explore potential collaboration opportunities with your esteemed organization. 

We are particularly interested in {collaboration_idea} and believe our combined efforts could create greater impact. 

I would appreciate the opportunity to discuss this further at your convenience. Please let me know a suitable time for a meeting.

Looking forward to your positive response.

Sincerely,
{your_name}
{your_organization}
{address}
{date}''')

    elif (type == '10'):
        your_name = input("enter your name = ")
        your_organization = input("enter your organization = ")
        address = input("enter your address = ")
        date = input("enter date = ")
        company = input("enter company name = ")
        event_cause = input("enter event/cause = ")
        sponsorship_type = input("enter what you're requesting = ")
        
        print(f'''Subject: Request for Sponsorship
To,
The {company}

Dear [Recipient's Name],

On behalf of {your_organization}, I am writing to request your sponsorship for {event_cause}. 

Your support as a {sponsorship_type} sponsor would greatly contribute to the success of this initiative while providing your company with [mention benefits like visibility, CSR fulfillment etc.].

We have attached a detailed sponsorship proposal for your consideration. We would be happy to discuss customization options to align with your marketing/CSR objectives.

Thank you for your time and consideration. We hope to partner with you for this meaningful cause.

Sincerely,
{your_name}
{your_organization}
{address}
{date}''')

else:
    pass