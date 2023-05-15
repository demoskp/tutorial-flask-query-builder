from flask_query_builder.querying import QueryBuilder, AllowedFilter, AllowedSort
from flask_restful import Resource
from sqlalchemy.orm import joinedload

from api.schemas.user import UserSchema
from filters.user import RoleFilter
from models.user import User
from sorts.user import LanguageSort


class UserList(Resource):
    def get(self):
        users = (
            QueryBuilder(User)
            .allowed_filters([
                AllowedFilter.exact("name", "first_name"),
                AllowedFilter.partial("email"),
                AllowedFilter.custom("role", RoleFilter()),
            ])
            .allowed_sorts([
                AllowedSort.field("name", "first_name"),
                AllowedSort.custom("language", LanguageSort())
            ])
            .query
            .join(User.roles)
            .join(User.preference)
            .options(
                joinedload(User.preference),
                joinedload(User.roles),
            )
            .all()
        )

        schema = UserSchema(many=True)

        return {"results": schema.dump(users)}
