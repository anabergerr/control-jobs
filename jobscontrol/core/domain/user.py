class User:
    def __init__(
        self, id, name, email, password_hash, created_at=None, updated_at=None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.updated_at = updated_at
