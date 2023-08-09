from functools import cached_property

class Lesson:
    """Lesson object"""

    def __init__(self, lesson_name : str,  start_time_str : str, end_time_str : str) -> None:
        
        """Getting name of the lesson, start and end times in str format with ':' separator (example: '9:30')"""
        
        start_arr = start_time_str.split(":")
        start_hours = int(start_arr[0])
        start_minutes = int(start_arr[1])

        end_arr = end_time_str.split(":")
        end_hours = int(end_arr[0])
        end_minutes = int(end_arr[1])

        self.name = lesson_name
        self.start_time_str = start_time_str
        self.end_time_str = end_time_str
        self.start_time = start_hours * 60 + start_minutes
        self.end_time = end_hours * 60 + end_minutes

    def __str__(self) -> str:
        return f"{self.name}: {self.start_time_str}-{self.end_time_str}"

class Schedule:


    def __init__(self, possible_lessons : list) -> None:
        """Getting list of lessons of type Lesson"""
        self.possible_lessons = possible_lessons

    @cached_property
    def optimal_schedule(self):
        self.possible_lessons.sort(key=lambda x: x.start_time)
        optimal_lessons = []
        cur_start_time = min([lesson.start_time for lesson in self.possible_lessons])
        while True:
            min_end_time = float("inf")
            min_end_time_lesson = None
            for lesson in self.possible_lessons:
                if lesson.start_time >= cur_start_time and lesson.end_time < min_end_time:
                    min_end_time = lesson.end_time
                    min_end_time_lesson = lesson
            if min_end_time_lesson == None:
                break
            else:
                optimal_lessons.append(min_end_time_lesson)
                cur_start_time = min_end_time

        return optimal_lessons


def main():

    lessons = [Lesson("Drawing", "9:00", "10:00"),
               Lesson("English", "9:30", "10:30"),
               Lesson("Music", "11:00", "12:00"),
               Lesson("Math", "10:00", "11:00"),
               Lesson("IT-science", "10:30", "11:30")]
    
    schedule = Schedule(lessons)
    print("Optimal schedule is:", *schedule.optimal_schedule, sep="\n")


main()