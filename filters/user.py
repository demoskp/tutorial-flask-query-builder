from flask_query_builder.filters import Filter

from models.user import Role


class RoleFilter(Filter):
    def filter(self, query, model, filter_name, values):
        print(values)
        if not len(values):
            return query
        return query.filter(Role.slug.in_(values))
