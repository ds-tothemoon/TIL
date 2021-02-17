class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        from datetime import datetime
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return days[datetime(year,month,day).weekday()]