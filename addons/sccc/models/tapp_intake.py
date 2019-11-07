from odoo import models, fields, api
from random import randint

class TappIntake(models.Model):
    _name = 'sccc.tapp_intake'
    _description = 'TAPP Intake'
    _rec_name = 'combination'
    combination = fields.Char (string='Form Name', compute='_compute_fields_combination', store=True)

    date = fields.Date('TAPP Intake Date')
    is_retake = fields.Char('Is this a Re-Intake? If yes, enter in which # intake the client is on (e.g. 2nd, 3rd, 4th)')
    interviewer = fields.Char('Interviewer')
    control_number = fields.Integer('Control Number')
    enter = fields.Char('Enter')

    marital_status = fields.Char('Marital Status')
    number_of_children = fields.Integer('Number of children living with you')
    number_not = fields.Integer('Not living with you')
    partner_name = fields.Char('Name of partner')
    relationship = fields.Selection([('Husband/Wife','Husband/Wife'), ('Common-Law','Common-Law'), ('Fiancee','Fiancee'), 
                                     ('Boyfriend/Girlfriend','Boyfriend/Girlfriend'), ('Other','Other')], 'Relationship')
    relationship_other = fields.Char('If other, please describe')
    partner_age = fields.Integer('His/Her age')
    relationship_years = fields.Integer('Number of years in relationship')
    living_together = fields.Selection([('Yes','Yes'), ('No','No')], 'Living together now?')
    partner_address = fields.Char('His/Her current address')
    address_years = fields.Integer('His/Her number of years at current address')
    reconcile = fields.Selection([('Yes','Yes'), ('No','No')], 'Do you hope to reconcile?')
    partner_home_phone = fields.Char('His/Her home phone')
    partner_work_phone = fields.Char('His/Her work phone')
    all_household_members = fields.Text('List name of all household members with whom you live, including their ages and relationships to you')

    case_number = fields.Char('Case number')
    current_charge = fields.Char('Current charge/s')
    incident_date = fields.Date('Date of incident')
    incident_description = fields.Text('Brief description of incident')
    arrest_date = fields.Date('Arrest date')
    jail_days = fields.Integer('How many days did you spend in jail?')
    sentence_date = fields.Date('Date of sentence or disposition')
    court_date = fields.Date('Date to report back to court')
    disposition = fields.Selection([('Convicted','Convicted'), ('Case pending','Case pending'), 
                                    ('Charges dropped','Charges dropped'), ('Other','Other')], 'Disposition')
    disposition_other = fields.Char('If other, please describe')
    currently_on = fields.Selection([('Parole','Parole'), ('Probation','Probation'), 
                                    ('Conditional Sentence','Conditional Sentence'), ('Summary Probation','Summary Probation')], 'Currently on')
    probation_years = fields.Integer('Number of years on probation')
    probation_end = fields.Date('Ending date of probation')
    probation_conditions = fields.Selection([('BTP', 'BTP'), ('Stay away order', 'Stay away order'), ('Abstain from alcohol', 'Abstain from alcohol')], 'Probation Conditions')
    fine = fields.Integer('Fine: $')
    modified_order = fields.Char('Modified Order? Explain')
    other_conditions = fields.Char('Describe any other conditions')
    probation_officer_name = fields.Char('Probation / Parole Officer name')
    probation_officer_phone = fields.Char('Phone Number')
    restraining_order = fields.Selection([('Yes','Yes'), ('No','No')], 'Is there a restraining order?')
    restraining_order_yes = fields.Char('If yes, describe the conditions')

    pending_criminal_charges = fields.Text('Describe any and all other pending criminal charges you have (circumstances, where the case is in the system)')
    police_called_home = fields.Text('How many times have police been called to your home because of family disputes?')
    current_is_first = fields.Selection([('Yes','Yes'), ('No','No')], 'Was the current incident your first and only assault or domestic/relationship violence arrest?')
    violent_crimes_arrests = fields.Text('Briefly describe all prior arrests you have had for non-violent crimes you have not described above, including date, offense, and disposition')

    alcohol_use = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Do you use, or have you ever used alcohol, drugs or tobacco?')
    substance_type = fields.Char('Substance type')
    how_consumed = fields.Char('How is it consumed')
    often_used = fields.Char('How often do you use it')
    last_time_used = fields.Char('Last time you used')
    substance_type2 = fields.Char('Substance type')
    how_consumed2 = fields.Char('How is it consumed')
    often_used2 = fields.Char('How often do you use it')
    last_time_used2 = fields.Char('Last time you used')
    substance_type3 = fields.Char('Substance type')
    how_consumed3 = fields.Char('How is it consumed')
    often_used3 = fields.Char('How often do you use it')
    last_time_used3 = fields.Char('Last time you used')

    substance_abuser = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Do you see yourself as being a substance abuser or as being substance-dependent?')
    substance_dependent = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Do you believe you have ever been substance-dependent or a substance abuser?')
    # Drug treatment
    treatment_type1 = fields.Boolean('AA')
    treatment_type2 = fields.Boolean('NA')
    treatment_type3 = fields.Boolean('Residential Treatment')
    treatment_type4 = fields.Boolean('Individual Counseling')
    treatment_type5 = fields.Boolean('Family counseling')
    treatment_type6 = fields.Boolean('Other')
    treatment_other = fields.Char('If other, please describe')

    # Provoked
    provoked_type1 = fields.Boolean('Friends')
    provoked_type2 = fields.Boolean('Family')
    provoked_type3 = fields.Boolean('Work')
    provoked_type4 = fields.Boolean('Finances')
    provoked_type5 = fields.Boolean('Relationship')
    provoked_type6 = fields.Boolean('Death')
    provoked_type7 = fields.Boolean('Not Applicable')
    provoked_type8 = fields.Boolean('Other')
    provoked_other = fields.Char('If other, please describe')

    # Sobriety
    sobriety_type1 = fields.Boolean('AA')
    sobriety_type2 = fields.Boolean('NA')
    sobriety_type3 = fields.Boolean('Counseling')
    sobriety_type4 = fields.Boolean('Not Applicable')
    sobriety_type5 = fields.Boolean('Nothin')
    sobriety_type6 = fields.Boolean('Other')
    sobriety_other = fields.Char('If other, please describe')

    emotional_health = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], 
                                        'What word you would use to describe your emotional/mental health')
    attended_therapy = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Have you ever attended counseling or therapy for any issue besides substance abuse?')
    describe_therapy_purpose = fields.Text('If yes, describe purpose you attended, dates attended, dates and whom seen')
    hospitalized = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Have you ever been hospitalized for any psychological or emotional problems?')
    hospitalized_purpose = fields.Text('If yes, for what purpose, when and where?')

    # Religious
    religious_type1 = fields.Boolean('Meditate')
    religious_type2 = fields.Boolean('Pray')
    religious_type3 = fields.Boolean('Read spiritual/religious materials')
    religious_type4 = fields.Boolean('None')
    religious_type5 = fields.Boolean('Atheist')
    religious_type6 = fields.Boolean('Other')
    religious_other = fields.Char('If other, please describe')

    # Hobbies
    hobby_type1 = fields.Boolean('Fishing')
    hobby_type2 = fields.Boolean('Body Building')
    hobby_type3 = fields.Boolean('Watching football games')
    hobby_type4 = fields.Boolean('Playing musical instruments')
    hobby_type5 = fields.Boolean('Mountain biking')
    hobby_type6 = fields.Boolean('Basketball')
    hobby_type7 = fields.Boolean('Hunting')
    hobby_type8 = fields.Boolean('Water Sports')
    hobby_type9 = fields.Boolean('Camping')
    hobby_type10 = fields.Boolean('Building Cars')
    hobby_type11 = fields.Boolean('Using computer/Internet')
    hobby_type12 = fields.Boolean('Hiking')
    hobby_type13 = fields.Boolean('Collecting guns')
    hobby_type14 = fields.Boolean('Watching TV')
    hobby_type15 = fields.Boolean('Other')
    hobby_other = fields.Char('If other, please describe')
    
    physical_activity = fields.Selection([('Very active','Very active'), ('Active','Active'), ('Somewhat active','Somewhat active'), 
                                          ('Not active','Not active')], 'Physical activity per week')
    physical_activity_description = fields.Char('Describe what physical activity (other than work) you do weekly')
    last_physical = fields.Char('When (month & year) did you have your last physical examination?')
    last_tested = fields.Char('When (month & year) were you last tested for HIV/AIDS?')
    medical_conditions = fields.Char('What medical conditions do you have (including head injuries) that we should know about?')
    last_tested2 = fields.Char('When (month & year) were you last tested for hepatitis C?')
    prescribed_medication = fields.Char('List any prescribed medication you are taking:')

    grade = fields.Selection([('8 or less','8 or less'), ('9 - 11','9 - 11'), ('12','12'), ('More than 12','More than 12')], 
                             'What grade in school did you complete?')
    have_one = fields.Selection([('High School Diploma','High School Diploma'), ('Equivalency Certificate','Equivalency Certificate'), 
                                 ('GED','GED'), ('College Degree','College Degree')], 'Do you have one')
    degrees = fields.Char('List your degrees, vocational certificates and licenses')
    served_military = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Served in the military?')
    service_branch = fields.Char('Branch of service')
    military_training = fields.Char('Type of military training')
    combat_action = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Did you see combat action?')
    combat_action_where = fields.Char('Where')
    combat_action_when = fields.Char('When')

    occupation = fields.Char('Your occupation')
    hours_per_week = fields.Char('Hours per week')
    company_name = fields.Char('Name of company')
    company_location = fields.Char('Where you work')
    job_years = fields.Integer('Number of years on job')
    work_schedule = fields.Char('Work schedule')
    hourly_wage = fields.Integer('Hourly wage')
    monthly_income = fields.Integer('Monthly income')
    before_taxes = fields.Integer('Before taxes')
    after_taxes = fields.Integer('After taxes')
    people_support = fields.Integer('Number of people you support')
    other_sources = fields.Char('Other sources of income')
    three_occupations = fields.Char('List your three most recent, previous occupations')
    
    anger_type1 = fields.Boolean('Spouse/Significant Other')
    anger_type2 = fields.Boolean('Minister/Priest/Rabbi')
    anger_type3 = fields.Boolean('Family')
    anger_type4 = fields.Boolean('Friends')
    anger_type5 = fields.Boolean('None')
    anger_type6 = fields.Boolean('Other')
    anger_other = fields.Char('If other, please specify')
    supportive_group = fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Do you have a supportive group in your life, such as a clean and sober network?')
    support_benefit = fields.Char('Describe what kinds of support you would benefit from in the BTP')

    emergency_name = fields.Char('Name')
    emergency_phone = fields.Char('Phone')
    emergency_relation = fields.Char('Relationship to you')
    emergency_street = fields.Char('Street address')
    emergency_city = fields.Char('City')
    emergency_zip = fields.Char('Zip Code')

    # Relations
    file = fields.Many2one('sccc.file', string='File', required=True)
    client = fields.Many2one('sccc.client', string='Client', required=True)

    @api.depends('file', 'date') 
    def _compute_fields_combination(self):
      self.combination = str(self.file.file_number) + ' - ' + str(self.file.name) + ' TAPP Intake'