from flask_query_builder.filters import Filter

from models.user import User, Role


class NameFilter(Filter):
    def filter(self, query, model, filter_name, values):
        if not len(values):
            return query
        value = values[0]
        return query.filter(
            User.first_name.ilike(f"%{value}%") | User.last_name.ilike(f"%{value}%")
        )


class RoleFilter(Filter):
    def filter(self, query, model, filter_name, values):
        if not len(values):
            return query
        return query.filter(Role.slug.in_(values))
