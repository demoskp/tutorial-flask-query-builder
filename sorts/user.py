from flask_query_builder.sorts import Sort

from models.user import Preference


class LanguageSort(Sort):
    def sort(self, query, model, sort_name, descending):
        if descending:
            return query.order_by(Preference.language.desc())
        return query.order_by(Preference.language)
