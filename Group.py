#Name: Shivani Pathak
#UIN: 661646405

class Group:
    num_of_objects = 0

    def __init__(self, g_id=None):
        Group.num_of_objects += 1
        self.g_id = g_id
        if g_id is None:
            self.g_id = Group.num_of_objects
        #self.attributes = g_attributes
        self.list_people = []

    def validate_group(self):
        for i in self.list_people:
            #value = {'iD', 'firstName', 'lastName', 'groupName'}
            #i.validate_person(value)
            value = {'iD', 'firstName', 'lastName'}
            i.validate_person(value)
        if len(self.list_people) < 3:
                print("Group ", self.g_id, " has ", len(self.list_people), " people, less than three")
        if len(self.list_people) > 5:
                print("Group ", self.g_id, " has ", len(self.list_people), " people, more than five")
