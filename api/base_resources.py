from __future__ import annotations

import typing

from marshmallow_sqlalchemy import fields
from sqlalchemy import inspect


class NestIfLoaded(fields.Nested):
    def serialize(
        self,
        attr: str,
        obj: typing.Any,
        accessor: typing.Callable[[typing.Any, str, typing.Any], typing.Any] | None = None,
        **kwargs,
    ):
        if obj is not None:
            ins = inspect(obj)
            if attr in ins.unloaded:
                return [] if attr[-1] == "s" else None

        return super().serialize(attr, obj, accessor, **kwargs)
