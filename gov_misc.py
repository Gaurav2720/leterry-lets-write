choice = int (input("enter your choise --> "))
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
        he_she = input("entert")
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