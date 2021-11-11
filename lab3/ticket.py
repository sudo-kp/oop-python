import datetime
import json
import os
import uuid

all_tickets = []


class Event:
    def __init__(self, name="noname", date=None,
                 entry_fee=0, num_of_tickets=0, filename="default.json"):
        if not isinstance(filename, str):
            raise TypeError("Wrong type of file name")
        if not len(filename):
            raise ValueError("Empty file name")
        self.filename = filename
        self.name = name
        self.date = date
        self.entry_fee = entry_fee
        self.num_of_tickets = num_of_tickets
        with open(self.filename, "w") as file:
            json.dump(self.__dict__, file, indent=1)

    def __str__(self):
        return f"Event {self.name} on {self.date} costs {self.entry_fee}, {self.num_of_tickets} tickets left"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong event name")
        self.__name = name
        if os.path.exists(self.filename) and os.stat(self.filename).st_size:
            with open(self.filename, "w") as file:
                json.dump(self.__dict__, file, indent=1)

    @property
    def date(self):
        return datetime.datetime.strptime(self.__date, "%Y-%m-0%d %H:%M:%S")

    @date.setter
    def date(self, date):
        if not date:
            self.__date = datetime.datetime.now().__str__()
            return
        if not isinstance(date, datetime.datetime):
            raise TypeError("Wrong date type")
        if date < datetime.datetime.now():
            raise ValueError("Wrong date value")
        self.__date = date.__str__()
        if os.path.exists(self.filename) and os.stat(self.filename).st_size:
            with open(self.filename, "w") as file:
                json.dump(self.__dict__, file, indent=1)

    @property
    def entry_fee(self):
        return self.__entry_fee

    @entry_fee.setter
    def entry_fee(self, entry_fee):
        if not isinstance(entry_fee, (int, float)):
            raise TypeError("Wrong entry fee type")
        if entry_fee < 0:
            raise ValueError("Wrong entry fee value")
        self.__entry_fee = entry_fee
        if os.path.exists(self.filename) and os.stat(self.filename).st_size:
            with open(self.filename, "w") as file:
                json.dump(self.__dict__, file, indent=1)

    @property
    def num_of_tickets(self):
        return self.__num_of_tickets

    @num_of_tickets.setter
    def num_of_tickets(self, num_of_tickets):
        if not isinstance(num_of_tickets, int):
            raise TypeError("Wrong type of number of tickets")
        if num_of_tickets < 0:
            raise ValueError("Wrong value of number of tickets")
        self.__num_of_tickets = num_of_tickets
        if os.path.exists(self.filename) and os.stat(self.filename).st_size:
            with open(self.filename, "w") as file:
                json.dump(self.__dict__, file, indent=1)

    def factory(self, person):
        if not isinstance(person, Person):
            raise TypeError("Wrong person type")
        if self.num_of_tickets <= 0:
            raise RuntimeError("No more tockets")
        date = datetime.datetime.now()
        self.num_of_tickets -= 1
        if person.is_student:
            return StudentTicket
        if self.date - date == datetime.timedelta(60):
            return AdvancedTicket
        if self.date - date == datetime.timedelta(10):
            return LateTicket
        return Ticket


class Person:
    def __init__(self, name, surname, is_student):
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("Wrong surname or name type")
        if not isinstance(is_student, bool):
            raise TypeError("Wrong is_student type")
        if not len(name) or not len(surname):
            raise ValueError("Empty name or surname")
        self.name = name
        self.surname = surname
        self.is_student = is_student

    def __str__(self):
        return f"{self.name} {self.surname}"


class Ticket:
    def __init__(self, evnt, person):
        if not isinstance(evnt, Event):
            raise TypeError("Wrong event type")
        self.event = evnt
        self.number = uuid.uuid4().__str__()
        self.person = person
        all_tickets.append(self)

    def __str__(self):
        return f"Ticket: {self.number} on event {self.event.name}\nfor {self.person}"

    def price(self):
        return self.event.entry_fee


def find_ticket(ticket_number):
    for ticket in all_tickets:
        if ticket.number == ticket_number:
            return ticket


STUDENT_DISCOUNT = 0.5
ADVANCED_DISCOUNT = 0.4
LATE_ADD = 1.1


class AdvancedTicket(Ticket):
    def price(self):
        return self.event.entry_fee * ADVANCED_DISCOUNT


class StudentTicket(Ticket):
    def price(self):
        return self.event.entry_fee * STUDENT_DISCOUNT


class LateTicket(Ticket):
    def price(self):
        return self.event.entry_fee * LATE_ADD


with open("1.json", "r") as file:
    edict = json.load(file)

event = Event(edict["_Event__name"], datetime.datetime.strptime(edict["_Event__date"], "%Y-%m-0%d %H:%M:%S"),
              edict["_Event__entry_fee"], edict["_Event__num_of_tickets"], "2.json")

person1 = Person("Anna", "Sydorenko", True)
person2 = Person("Kate", "Brown", False)

class_name = event.factory(person1)
ticket1 = class_name(event, person1)

class_name = event.factory(person2)
ticket2 = class_name(event, person2)

print(ticket1)
print(ticket2)
print(find_ticket(ticket2.number))
print(event)

