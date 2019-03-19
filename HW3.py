#Name: Shivani Pathak
#UIN: 661646405

from Person import Person
from Group import Group

list_of_people = []
list_of_groups = []

def print_all_groups(obj):
    print("Group ", obj.num_of_objects)
    for i in obj.list_people:
        print(i.attributes['firstName'], i.attributes['lastName'])

def print_specific_group(obj):
    for i in obj.list_people:
        print(i.attributes['firstName'], i.attributes['lastName'])

while True:
    prompt = input("Choose an option: ")
    if prompt == '-1':
        print("Goodbye!")
        break

    if prompt == '0':
        print("On -1, end the loop.")
        print("On 0, output what each number does")
        print("On 1, create a new Person. Ask for the first and last name.")
        print("On 2, create a new group, populated by existing Person objects. Loop while outputting the names of people ")
        print("who have not been assigned to a group and ask for the ids of the people to add.")
        print("On 3, allow the user to modify an existing group. Ask the user which group they wish to modify. Then ask")
        print("whether they are trying to add or remove members to/from the group. Then, interactively allow the user to add ")
        print("or remove as many users as they want by offering a list of available choices and having the user select which ")
        print("member to interact with.")
        print("On 4, validate all existing groups, as well as all people to check that they have a group.")
        print("On 5, output each group’s number and members.")

    if prompt == '1':
        person_first_name = input("What is the person's first name?")
        person_last_name = input("What is the person's last name?")
        p = Person(None, person_first_name, person_last_name, None)
        list_of_people.append(p)

    if prompt == '2':
        for i in list_of_people:
            print(i.attributes['iD'], i.attributes['firstName'], i.attributes['lastName'])
        g = Group(None)
        list_of_groups.append(g)
        while True:
            ask = input("Which person would you like to add to the new group? (-1 to finish adding people) : ")
            if ask == '-1':
                break
            else:
                for i in list_of_people:
                    if ask == str(i.attributes['iD']):
                        g.list_people.append(i)
                        i.attributes["groupName"] = g.num_of_objects
                        list_of_people.remove(i)
                for i in list_of_people:
                    print(i.attributes['iD'], i.attributes['firstName'], i.attributes['lastName'])

    if prompt == '3':
        group = input("Which group would you like to modify? ")
        chosen_group = list_of_groups[int(group) - 1]
        add_remove = input("Would you like to ADD or REMOVE members? ")
        if add_remove == 'ADD':
            for i in list_of_people:
                print(i.attributes['iD'], i.attributes['firstName'], i.attributes['lastName'])
            while True:
                add = input("Which person would you like to add to the new group? (-1 to finish adding people) :")
                if add == '-1':
                    break
                else:
                    for i in list_of_people:
                        if add == str(i.attributes['iD']):
                            chosen_group.list_people.append(i)
                            i.attributes['groupName'] = chosen_group.num_of_objects
                            #del list_of_people[i.p_id]
                            #list_of_people.pop(i)
                            list_of_people.remove(i)
                    for i in list_of_people:
                        print(i.attributes['iD'], i.attributes['firstName'], i.attributes['lastName'])

        if add_remove == 'REMOVE':
            print_specific_group(chosen_group)
            while True:
                remove = input("Which person would you like to remove from the group? (-1 to finish adding people) : ")
                if remove == '-1':
                    break
                else:
                    del chosen_group.list_people[int(remove)-1]
                    for i in chosen_group.list_people:
                        if i.attributes['groupName'] == remove:
                            i.attributes['groupName'] = None
                            list_of_people.append(i)
                        #if i.attributes['groupName'] == remove:
                         #   i.attributes['groupName'] = None
                          #  list_of_people.append(i)
                    #list_of_people.append()
                    #del chosen_group.list_people[i.p_id]
                print_specific_group(chosen_group)

    if prompt == '4':
        for i in list_of_groups:
            i.validate_group()
        for i in list_of_people:
            #i.validate_person(list_of_people)
            if i.attributes['groupName'] is None:
                print(i.attributes['firstName'], i.attributes['lastName'], "does not have an assigned group.")

    if prompt == '5':
        #print("Group ", Group.num_of_objects)
        #for i in Person.list_people:
           #print(i.attributes['firstName'], i.attributes['lastName'])
        for i in list_of_groups:
            print_all_groups(i)