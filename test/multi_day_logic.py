import re
from datetime import date, timedelta
from typing import Optional

startdate = "2021-03-23"
enddate = "2021-04-12"

startdate_fragments = re.split("-", startdate)
enddate_fragments = re.split("-", enddate)

sdate = date(int(startdate_fragments[0]), int(startdate_fragments[1]), int(startdate_fragments[2]))  # start date
edate = date(int(enddate_fragments[0]), int(enddate_fragments[1]), int(enddate_fragments[2]))  # end date

delta = edate - sdate  # as timedelta

for i in range(delta.days + 1):
    currentdate = re.split("-", str(sdate + timedelta(days=i)))
    year = int(currentdate[0])  # type: Optional[int]
    month = int(currentdate[1])  # type: Optional[int]
    day = int(currentdate[2])  # type: Optional[int]

    print(year, month, day)

    """
    expected output:

2021 3 24
2021 3 25
2021 3 26
2021 3 27
2021 3 28
2021 3 29
2021 3 30
2021 3 31
2021 4 1
2021 4 2
2021 4 3
2021 4 4
2021 4 5
2021 4 6
2021 4 7
2021 4 8
2021 4 9
2021 4 10
2021 4 11
2021 4 12
"""
