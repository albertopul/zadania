import operator
from faker import Faker
faker = Faker()


   

class BaseContact:
    def __init__(self, name, surname, email, priv_phone_number):
        self.name = name
        self.surname = surname
        self.email = email
        self.priv_phone_number = priv_phone_number

    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.priv_phone_number}'

    def contact(self):
        return f"Wybieram numer: {self.priv_phone_number} i dzwonię do {self.name} {self.surname}"

    @property
    def label_length(self):
        return f'Liczba liter w imieniu i nazwisku: {len(self.name)} {len(self.surname)}'



class BusinessContact(BaseContact):
    def __init__(self, business_phone_number, company_name, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone_number = business_phone_number
        self.company_name = company_name
        self.job = job
    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.company_name} {self.job} {self.business_phone_number}'

    def contact(self):
        return f"Wybieram numer: {self.business_phone_number} i dzwonię do {self.name} {self.surname}"

    @property
    def  label_length(self):
        return f'Liczba liter w imieniu i nazwisku: {len(self.name)} {len(self.surname)}'





base_list = []
business_list = []
def create_contacts():
    print("Wizytówki:")
    print(" ")
    for person in range(3):
        person = BaseContact(name=faker.first_name(), surname=faker.last_name(), email=faker.email(), priv_phone_number=faker.phone_number())
        base_list.append(person)
    for obj in base_list:
        print(obj)
        print(" ")
        print(BaseContact.contact(obj))
        print(" ")
        print(obj.label_length)
        print("------------")
    print("Wizytówki biznesowe:")
    print(" ")
    for person in range(3):
        person = BusinessContact(name=faker.first_name(), surname=faker.last_name(), email=faker.email(), company_name=faker.company(), job=faker.job(), priv_phone_number=faker.phone_number(), business_phone_number=faker.phone_number())
        business_list.append(person)
    for obj in business_list:
        print(obj)
        print(" ")
        print(BusinessContact.contact(obj))
        print(" ")
        print(obj.label_length)
        print("------------")
create_contacts()


 
