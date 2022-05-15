class Principal:
    def __init__(self, user_id, scope):
        self.user_id = user_id
        self.scope = scope

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'scope': self.scope
        }
