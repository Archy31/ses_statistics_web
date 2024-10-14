from types import NoneType
from typing import Iterable, Any
from enum import Enum

# from sqlalchemy.sql.operators import distinct_op

from config import DB_PORT, DB_USER, DB_HOST, DB_NAME, DB_PASS
from sqlalchemy import create_engine, Column, VARCHAR, REAL, Date, Time, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


engine = create_engine(
    f'postgresql+psycopg2://{DB_USER}:{DB_PASS}\@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Phase(Base):
    __tablename__ = 'bulls'

    event_id = Column(VARCHAR(50), nullable=False)
    ev_status = Column(VARCHAR(10), nullable=False)
    latitude = Column(REAL, nullable=False)
    longitude = Column(REAL, nullable=False)
    reg_date = Column(Date, nullable=False)
    reg_time = Column(Time, nullable=False)
    magnitude = Column(REAL, nullable=False)
    num_phases = Column(REAL, nullable=False)
    ns = Column(REAL, nullable=False)
    dist_type = Column(VARCHAR(7), nullable=False)
    p_type = Column(VARCHAR(10), nullable=False)
    p_error = Column(REAL, nullable=False)
    last_phase_time = Column(Time, nullable=False)
    phase_id = Column(VARCHAR(50), nullable=False, primary_key=True)


# class Phase(Base):
#     __tablename__ = 'bulls'
#
#     event_id = Column(Integer, nullable=False, primary_key=True)
#     status = Column(VARCHAR(10), nullable=False)
#     lat = Column(REAL, nullable=False)
#     lon = Column(REAL, nullable=False)
#     registr_date = Column(Date, nullable=False)
#     registr_time = Column(Time, nullable=False)
#     mb = Column(REAL, nullable=False)
#     np = Column(REAL, nullable=False)
#     ns = Column(REAL, nullable=False)
#     dist_type = Column(VARCHAR(7), nullable=False)
#     type = Column(VARCHAR(10), nullable=False)
#     error = Column(REAL, nullable=False)
#     time_at_the_epicenter = Column(Time, nullable=False)
#     # phase_id = Column(VARCHAR(50), nullable=False)


def unpack_iterable(*obj: Iterable):
    """
    Fot getting unpacked data.
    :param obj:
    :type obj:
    :return:
    :rtype:
    """
    return obj


def do_list(obj: Any) -> list | Any:
    """
    From Any object doing list object.
    :param obj:
    :type obj:
    :return:
    :rtype:
    """
    if type(obj) not in {list, tuple, set, NoneType}:
        return [obj]

    return obj


class Compare(Enum):
    Less = "<"
    Equal = "="
    Greeter = ">"


class Where(Phase):
    def __init__(self, column: Column, compare: Compare, value: Any):
        self.column = column
        self.compare = compare.value
        self.value = value


class Table:
    def __init__(self, sessionObj: Session, table: Base):
        self.Table = table
        self.Session = sessionObj

    def select(
            self,
            columns: Base | list[Base] | None = None,
            order_by: Base | list[Base] | None = None,
            where: Where | None = None,
            distinct_by: Base | list[Base] | None = None
    ) -> Any | None:
        """
        For getting data rows from PostgreSQL DB.
        :param where:
        :type where:
        :param distinct_by:
        :type distinct_by:
        :param order_by:
        :type order_by:
        :param columns:
        :type columns:
        :return:
        :rtype:
        """
        result = None
        try:
            columns = None if columns is None else do_list(obj=columns)
            order_by = None if order_by is None else do_list(obj=order_by)
            distinct_by = None if distinct_by is None else do_list(obj=distinct_by)

            return self.Session.query(self.Table).all()

            # noinspection PyUnreachableCode
            if distinct_by is None:
                if where is None:
                    if order_by is None:
                        if columns is None:
                            return self.Session.query(self.Table).all()

                        return self.Session.query(*columns).all()

                    if columns is None:
                        return self.Session.query(self.Table).order_by(*order_by).all()

                    return self.Session.query(*columns).order_by(*order_by).all()
                # ---------------------------------------------------------------------- #
                if order_by is None:
                    if columns is None:
                        exec(
                            f"result = self.Session.query(self.Table)"
                            f".filter({where.column} {where.compare} {where.value}).all()"
                        )

                    exec(
                        f"result = self.Session.query(*columns)"
                        f".filter({where.column} {where.compare} {where.value}).all()"
                    )

                if columns is None:
                    exec(
                        f"result = self.Session.query(self.Table)"
                        f".filter({where.column} {where.compare} {where.value}).order_by(*order_by).all()"
                    )

                exec(
                    f"result = self.Session.query(*columns)"
                    f".filter({where.column} {where.compare} {where.value}).order_by(*order_by).all()"
                )
            # ------------------------------------------------------------------------------------- #
            if where is None:
                if order_by is None:
                    if columns is None:
                        return self.Session.query(self.Table).all()

                    return self.Session.query(*columns).all()

                if columns is None:
                    return self.Session.query(self.Table).order_by(*order_by).all()

                return self.Session.query(*columns).order_by(*order_by).all()
            # ---------------------------------------------------------------------- #
            if order_by is None:
                if columns is None:
                    exec(
                        f"result = self.Session.query(self.Table).distinct(*distinct_by)"
                        f".filter({where.column} {where.compare} {where.value}).all()"
                    )

                exec(
                    f"result = self.Session.query(*columns).distinct(*distinct_by)"
                    f".filter({where.column} {where.compare} {where.value}).all()"
                )

            if columns is None:
                exec(
                    f"result = self.Session.query(self.Table).distinct(*distinct_by)"
                    f".filter({where.column} {where.compare} {where.value}).order_by(*order_by).all()"
                )

            exec(
                f"result = self.Session.query(*columns).distinct(*distinct_by)"
                f".filter({where.column} {where.compare} {where.value}).order_by(*order_by).all()"
            )

        except Exception as _ex:
            print(f"[EXCEPTION] {_ex}")

        # finally:
        #     return result


phases = Table(sessionObj=session, table=Phase).select()


if phases is not None:
    for ph in phases:
        print(ph.latitude)

else:
    print(phases)







