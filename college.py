choice = input("enter your choice    ")
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
