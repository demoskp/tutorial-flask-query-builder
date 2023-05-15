from api.base_resources import NestIfLoaded
from extensions import ma
from models.user import User, Preference, Address, Role


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        exclude = ["id"]


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        exclude = ["id"]


class PreferenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Preference
        exclude = ["id"]


class UserSchema(ma.SQLAlchemyAutoSchema):
    preference = NestIfLoaded(PreferenceSchema)
    addresses = NestIfLoaded(AddressSchema, many=True)
    roles = NestIfLoaded(RoleSchema, many=True)

    class Meta:
        model = User
