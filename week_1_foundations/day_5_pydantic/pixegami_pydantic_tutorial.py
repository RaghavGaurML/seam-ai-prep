# Code from the Pydantic tutorial by Pixegami on Youtube
# Link: https://www.youtube.com/watch?v=XIdQ6gO3Anc
# While Typing adds explicit type to define data
# Pydantic actually enforces those hints to keep data valid
# And allows us to easily Serialize/Deserialize data

from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    # Decorators are functions that wrap or modify other functions
    # Or classes to add extra behavior without changing their original code
    # And here, class methods act on the classes themselves, not just an
    # Instance of the class
    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

    # Example of a simple instance method (as opposed to a class method)
    def greet(self):
        return f"Hello, {self.name}!"


# user_data = {"name": "Raghav", "email": "raghavgaurrg@gmail.com", "account_id": 1234}
# user = User(**user_data)  # Unpack the dictionary data into User object

# JSON Serialization/Deserialization
# Serialization = turning Python objects into data that can be saved or sent.
# Deserialization = turning that data back into Python objects.
user_data = '{"name": "Raghav", "email": "raghavgaurrg@gmail.com", "account_id": 1234}'
user = User.model_validate_json(user_data)  # Used to validate json strings

print(user.name)
print(user.email)
print(user.account_id)
print("All User Data Correct!")


# Example 1: Invalid account_id Type
# invalid_user_data = {
#     "name": "Raghav",
#     "email": "raghavgaurrg@gmail.com",
#     "account_id": "ERROR", # Should be an integer
# }
#
# invalid_user = User(**invalid_user_data) # This catches the typing error
#
# print(invalid_user.name)
# print(invalid_user.email)
# print(invalid_user.account_id)

# Example 2: Invalid account_id Value
# invalid_user_data = {
#     "name": "Raghav",
#     "email": "raghavgaurrg@gmail.com",
#     "account_id": -1234,  # Should be a positive integer
# }

# invalid_user = User(**invalid_user_data)  # This catches the value error

# print(invalid_user.name)
# print(invalid_user.email)
# print(invalid_user.account_id)
