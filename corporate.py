choice = input("enter your choice    ")
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

