class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        
        if not member.get('id'):
            member['id'] = self._generate_id()
        
        
        if 'last_name' not in member:
            member['last_name'] = self.last_name
            
        
        self._members.append(member)
        return member

    def delete_member(self, id):
        
        for i, member in enumerate(self._members):
            if member['id'] == id:
                
                return self._members.pop(i)
        return None  

    def get_member(self, id):
        
        for member in self._members:
            if member['id'] == id:
                return member
        return None  

    
    def get_all_members(self):
        return self._members