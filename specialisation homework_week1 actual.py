"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""



    
    class CashRegister:
    
    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0
    #this is the reset_register method
    #this is the start of the transaction
    #i will use reset to print the name 


    def new_transaction(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        welcome = "SOSO BOUTIQUE"
        print(f"\n"
              f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"{welcome:^30}\n"
              f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def add_item(self, item, price):
        self.total_items[item.capitalize()] = price
        self.total_price += price
        print(f"{item.capitalize():>20s}{price:>10.2f}")

    def remove_item(self, item):
        try:
            removed = self.total_items.pop(item.capitalize())
        except KeyError:
            print("Item not found.")
        else:
            self.total_price -= removed
            item_str = f"*CANCELLED* {item.capitalize()}"  
            price_str = f"–{removed:.2f}"                  
            print(f"{item_str:>30s}{price_str:>10}")

    def apply_discount(self, percentage_discount):
        self.discount = (percentage_discount/100) * self.total_price
        self.total_price = self.total_price - self.discount

    def get_total(self):
        print(f"————————————————————————————————————————")
        # Add discount details 
        if self.discount:
            discount_str = "DISCOUNT APPLIED"
            discount_amount_str = f"-£{self.discount:.2f}"
            print(f"{discount_str:>30s}{discount_amount_str:>10}")
        total_str = "TOTAL"
        total_price_str = f"£{self.total_price:.2f}"
        print(f"{total_str:>30s}{total_price_str:>10}\n"
              f"————————————————————————————————————————")

    
    def show_items(self):
        if not self.total_items:
            output = "No items  yet"
            print(f"{output:^30}")
        else:
            for item in self.total_items:
                price = f"£{self.total_items.get(item):0.2f}"
                print(f"{item:>30s}{price:>10}")



# EXAMPLE code run:

# ADD
# till is an object
till = CashRegister()
#the example is for customer with discount

till.new_transaction()
till.add_item('bread', 1.20)
till.add_item('milk', 0.65)
till.add_item('plates ', 10.50)
till.add_item('cereals ', 3.00)
till.add_item('apples', 2.45)
till.add_item('juice', 21.00)
till.add_item('unicorn  cake', 8.50)
till.remove_item('plates')
till.apply_discount(25)
till.get_total()

# customer without discount
# new_transaction 
till.new_transaction()
till.add_item('shampoo', 2.50)
till.add_item('pencils', 1.50)
till.add_item(' case', 3.60)
till.add_item('white chocolate bar', 0.65)
till.get_total()


print("\n>>> till.show_items()")
till.show_items()


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


#class Student:

  #  def __init__(self, name, age, id):
   #     self.name = name
   #     self.age = age
   #     self.id = id
  #      self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


class Student:
    """A base class is name as a student"""

    def __init__(self, fname, lname, age, institution, s_id):
        """Initialise the class Student
        :param fname: student's first name
        :type fname: str
        :param lname: student's last name
        :type lname: str
        :param age: student's age
        :type age: int
        :param institution: student's institution
        :type institution: str
        :param id: student's student ID reference
        :type id: str
        """
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.age = age  
        self.institution = institution.title()
        self.s_id = s_id

    def view_student_details(self):
        """Print out data held on a student
        :return: print out of details
        """
        print(f"–––––––––––––––\n"
              f"STUdent information \n"
              f"–––––––––––––––\n"
              f"First Name: {self.fname}\n"
              f"Last Name: {self.lname}\n"
              f"Age: {self.age}\n"
              f"Institution: {self.institution}\n"
              f"Student ID: {self.s_id}\n")


#this is my student subclass 

class CFGsoftwarestudent(Student):
    """A subclass to represent a Code First Girls  student"""

    def __init__(self, fname, lname, age, institution, s_id, specialisation):
       
        
        super().__init__(fname, lname, age, institution, s_id)
        self.course = "Software"
        self.specialisation = specialisation.capitalize()
        self.modules = set()
        self.grades = {"Foundation Theory": None,
                       "Specialisation Theory": None,
                       "Foundation Exam": None,
                       "Specialisation Exam": None,
                       "Homework": None,
                       "Project": None}
        self.final_result = None

    def view_student_details(self):
        
        print(f"\n–––––––––––––––\n"
              f"student information\n"
              f"–––––––––––––––\n"
              f"First Name: {self.fname}\n"
              f"Last Name: {self.lname}\n"
              f"Age: {self.age}\n"
              f"Institution: {self.institution}\n"
              f"Student ID: {self.s_id}\n"
              f"Course: {self.course}\n"
              f"Specialisation: {self.specialisation}\n"
              f"Modules: {', '.join(self.modules)}\n"
              f"Final Result: {self.final_result}\n")

    def module_reg(self, module_name):
       
        self.modules.add(module_name)
        print(f"{self.fname} {self.lname} 
              f"{module_name}.")

    def module_dereg(self, module_name):
        
        self.modules.discard(module_name)
        print(f"{self.fname} {self.lname} 
              f"{module_name}.")

    def add_grade(self, assessment, grade):
        
        assessment = assessment.title()
        try:
            self.grades[assessment] = grade
        except KeyError:
            print("Assessment not found.")
        else:
            print(f"name successfully entered on the student's record.")

    def weighted_grade(self):
        
        # Assessment weightings
        w_foundation_theory = 5
        w_specialisation_theory = 5
        w_foundation_exam = 20
        w_specialisation_exam = 25
        w_homework = 5
        w_project = 25

        # Student's results
        r_foundation_theory = self.grades["Foundation Theory"]
        r_specialisation_theory = self.grades["Specialisation Theory"]
        r_foundation_exam = self.grades["Foundation Exam"]
        r_specialisation_exam = self.grades["Specialisation Exam"]
        r_homework = self.grades["Homework"]
        r_project = self.grades["Project"]

        # Calculate weighted grade
        weighted_grade = (
                                 (w_foundation_theory * r_foundation_theory) +
                                 (w_specialisation_theory * r_specialisation_theory) +
                                 (w_foundation_exam * r_foundation_exam) +
                                 (w_specialisation_exam * r_specialisation_exam) +
                                 (w_homework * r_homework) +
                                 (w_project * r_project)
                         ) / 100

        self.final_result = weighted_grade
        print(f"software Final Grade: {int(weighted_grade)} %")