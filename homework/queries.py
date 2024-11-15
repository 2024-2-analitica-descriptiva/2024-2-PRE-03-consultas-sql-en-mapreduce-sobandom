"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

from .mapreduce import run_mapreduce_job # type: ignore

#
# Columns:
# total_bill, tip, sex, smoker, day, time, size
#

#
# SELECT *, tip/total_bill as tip_rate
# FROM tips;
#
def mapper_query_1(sequence):
    print(sequence)


def reducer_query_1(sequence):
    """Reducer"""
    return sequence


#
# ORQUESTADOR:
#
def run():
    """Orquestador"""

    run_mapreduce_job(
        mapper=mapper_query_1,
        reducer=reducer_query_1,
        input_directory="files/input",
        output_directory="files/query_1",
    )


if __name__ == "__main__":
