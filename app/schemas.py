from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    age = fields.Int(required=False)

    @validates("username")
    def validate_username(self, value):
        if len(value) < 3:
            raise ValidationError("Username must be at least 3 characters long.")

    @validates("password")
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

    @validates("age")
    def validate_age(self, value):
        if value < 18:
            raise ValidationError("You must be at least 18 years old.")
