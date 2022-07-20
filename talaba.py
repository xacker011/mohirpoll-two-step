class Person:
    def __init__(self, student_id, full_name, nationalitty, gender, faculty, admission_year):
        self.__student_id = student_id
        self.full_name = full_name
        self.nationalitty = nationalitty
        self.gender = gender
        self.faculty = faculty
        self.admission_year = admission_year
        
    def get_full_name(self):
        return self.full_name
        
    def get_nationalitty(self):
        return self.nationalitty
        
    def get_gender(self):
        return self.gender
        
    def get_faculty(self):
        return self.faculty
        
    def get_admission_year(self):
        return self.admission_year
    
    
    
    def get_student_id(self):
        return self.__student_id
    
    
class Undergraduate(Person):
    def __init__(self,student_id, full_name, nationalitty, gender, faculty, admission_year,residential_hall):
        super().__init__(student_id, full_name, nationalitty, gender, faculty, admission_year)
        self.residential_hall=residential_hall
        
    def get_residential_hall(self):
        return self.residential_hall
    
    
    
    
class Postgraduate(Person):
    def __init__(self,student_id, full_name, nationalitty, gender, faculty, admission_year, supervisor_name, research_topic):
        super().__init__(student_id, full_name, nationalitty, gender, faculty, admission_year)
        self.supervisor_name=supervisor_name
        self.research_topic=research_topic
    
    def get_supervisor_name(self):
        return self.supervisor_name
    
    def get_research_topic(self):
        return self.research_topic
    
