#Name: Shivani Pathak
#UIN: 661646405

class Person:
    num_of_people = 0

    def __init__(self, p_id=None, first_name=None, last_name=None, p_attributes=None):
        Person.num_of_people += 1
        self.p_id = p_id
        if self.p_id is None:
            self.p_id = Person.num_of_people
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = p_attributes
        if self.attributes is None:
            #self.attributes = {'firstName': first_name, 'lastName': last_name, 'iD': Person.num_of_people,
             #                  'groupName': p_attributes}
            self.attributes = {'firstName': first_name, 'lastName': last_name, 'iD': Person.num_of_people,
                               'groupName': p_attributes}

    def validate_person(self, obj_list):
        for i in obj_list:
            if self.attributes[i] is None:
                print("Person ", self.p_id, "does not have ", i)
            #if self.attributes['groupName'] is None:
             #   print(i.attributes['firstName'], i.attributes['lastName'], "does not have an assigned group.")
