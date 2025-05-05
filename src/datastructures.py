
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
        {

        "id": self._generateId(),
        "first_name": "Jhon",
        "last_name": last_name,
        "age": "33 Years Old",
        "lucky_numbers":[7,13,22]
        },
        {

        "id": self._generateId(),
        "first_name": "Jane",
        "last_name": last_name,
        "age": "35 Years Old",
        "lucky_numbers":[10,14,3]
        },
        {

        "id": self._generateId(),
        "first_name": "Jimmy",
        "last_name": last_name,
        "age": "5 Years Old",
        "lucky_numbers":[1]
        },
        
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        new_member = {

        "id": member["id"],
        "first_name": member["first_name"],
        "last_name": self.last_name,
        "age": member["age"],
        "lucky_numbers":member["lucky_numbers"]
        }
        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        for member in self._members:  # 
            if member["id"] == id:
                self._members.remove(member)  
                return member  
        return None


    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
