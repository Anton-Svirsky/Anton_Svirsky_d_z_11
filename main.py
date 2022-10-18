class Person:
    def __init__(self, name, patronymic, lastname, numbers):
        self.name = name
        self.patronymic = patronymic
        self.lastname = lastname
        self.numbers = numbers

    def get_phone(self, key = "private"):
        return self.numbers.get(key)


    def get_name(self):
        return f' {self.lastname} {self.name} {self.patronymic}'


    def get_work_phone(self):
        return self.get_phone("work")


    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.patronymic} примите участие в нашем ' \
               f'беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, company_name, c_type, company_numbers, *args):
        self.company_name = company_name
        self.c_type = c_type
        self.company_numbers = company_numbers
        self.persons = args

    def get_phone(self, key = 'contact'):
        if key in self.company_numbers:
            return self.company_numbers.get(key)
        for person in self.persons:
            numb = person.get_work_phone()
            if numb:
                return numb

    def get_name(self):
        return self.company_name

    def sms_text(self):
        return f'Для компании {self.company_name} есть супер предложение! Примите участие в нашем беспроигрышном '\
                f'конкурсе для {self.c_type}'


def send_sms(*args):
    for i in args:
        if i.get_phone() is not None:
            return f'Отправлено СМС на номер {i.get_phone()} с текстом:{i.get_sms_text()}'
        else:
            return f'Не удалось отправить сообщение абоненту: {i.name or i.company_name} '


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)

person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
