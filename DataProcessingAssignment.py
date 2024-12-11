class InMemoryDB:
    def __init__(self):
        self.main_state = {}
        self.transaction_state = None

    def get(self, key):
        # Check only the main state for committed values
        value = self.main_state.get(key, None)

        if value is None:
            print("null")
        else:
            print(value)


    def put(self, key, val):
        # Ensure a transaction is active
        if self.transaction_state is None:
            raise Exception("No transaction in progress")
        # Enforce type constraints
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(val, int):
            raise TypeError("Value must be an integer")
        # Update the transaction state
        self.transaction_state[key] = val


    def begin_transaction(self):
        # Ensure no active transaction
        if self.transaction_state is not None:
            raise Exception("A transaction is already in progress")
        # Create a new transaction state
        self.transaction_state = {}

    def commit(self):
        # Ensure a transaction is active
        if self.transaction_state is None:
            raise Exception("No transaction in progress")
        # Apply transaction changes to the main state
        self.main_state.update(self.transaction_state)
        # End the transaction
        self.transaction_state = None

    def rollback(self):
        # Ensure a transaction is active
        if self.transaction_state is None:
            raise Exception("No transaction in progress")
        # Discard transaction changes
        self.transaction_state = None

# Example usage
if __name__ == "__main__":
    db = InMemoryDB()

    db.get("A")
    db.begin_transaction()
    db.rollback()
    db.begin_transaction()
    db.put("B", 4)
    db.rollback()
    db.get("B")
    db.begin_transaction()
    db.put("A", 5)
    db.put("B", 10)
    db.commit()
    db.get("A")
    db.get("B")