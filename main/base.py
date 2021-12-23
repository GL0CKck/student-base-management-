import time
from contextlib import contextmanager
from threading import local

from django.utils.encoding import force_text
from django.db.backends.postgresql.base import DatabaseWrapper as DjangoDatabaseWrapper
from django.db.backends.utils import CursorWrapper as DjangoCursorWrapper

thread_local = local()


@contextmanager
def calc_sql_time(sql):
    timestamp = time.monotonic()

    yield
    if hasattr(thread_local, 'sql_count'):
        thread_local.sql_count += 1
        thread_local.sql_total += time.monotonic() - timestamp

    # print(f'Продолжительность SQL-запроса {sql} - {time.monotonic() - timestamp:.3f} сек.')


def make_safe(s):
    return s.replace('*', '').replace('\\', '').replace('%', '')


class CursorWrapper(DjangoCursorWrapper):
    def execute(self, sql, params=None):
        path = getattr(thread_local, 'path', '')
        if path:
            path = make_safe(path)
            sql = f'/* {path} */\n{force_text(sql)}\n/* {path} */'
        with calc_sql_time(sql):
            return super().execute(sql, params)


class DatabaseWrapper(DjangoDatabaseWrapper):
    def create_cursor(self, name=None):
        cursor = super().create_cursor(name)
        return CursorWrapper(cursor, self)

