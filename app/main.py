class Person:
    people = {}

    def __init__(self, name, age, ):
        self.name = name
        self.age = age

def create_person_list(people: list) -> list:
    new_list = []

    for person in people:
        new_person = Person(name=person["name"], age=person["age"])
        Person.people[person["name"]] = new_person
        new_list.append(new_person)

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[person["name"]].husband = Person.people[person["husband"]]

    return new_list

