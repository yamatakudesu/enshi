class Lab:
    members = None

    def __init__(self):
        self.members = []

    def add_member(self, new_member):
        self.members.append(new_member)

    def print_member(self):
        for member in self.members:
            member.print_info()
            
            
class LabMember:
    name = None

    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def __lt__(self, ob):
        return self.name < ob.name

    
class Student(LabMember):
    grade = 0

    def __init__(self, name):
        LabMember.__init__(self, name)

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

    def promotion(self):
        print ("student %s is going to be in the %dth(st, nd, rd) grade."%(self.name, self.grade + 1))

    def print_info(self):
        print("student name = %s (%d)"%(self.name, self.grade))

    def __str__(self):
        return "student name = %s (%d)"%(self.name, self.grade)
        
class Professor(LabMember):
    room = 0

    def __init__(self, *args, **kwargs):
        LabMember.__init__(self, *args, **kwargs)
        
    def set_room(self, room):
        self.room = room

    def get_room(self):
        return self.room

    def print_info(self):
        print("professor name = %s (%d)"%(self.name, self.room))

    def __str__(self):
        return "professor name = %s (%d)"%(self.name, self.room)
