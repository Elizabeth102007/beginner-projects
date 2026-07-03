from urllib.request import urlopen
import certifi 
import json
import math

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urlopen(address, cafile=certifi.where())
    result = response.read().decode('utf-8')
    data = json.loads(result)  # converts JSON string → Python list/dict
    
    courses = []
    for course in data:
        if course["enabled"] == True:  # filter active courses only
            tuple_entry = (
                course["fullName"],          
                course["name"],              
                course["year"],              
                sum(course["exercises"])     
            )
            courses.append(tuple_entry)
    
    return courses  # must RETURN, not print


def retrieve_course(course_name: str):
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urlopen(address, cafile=certifi.where())
    result = response.read().decode('utf-8')
    data = json.loads(result)  # this is a dict, not a list

    weeks = len(data)                                                        
    students = max(week["students"] for week in data.values())               
    hours = sum(week["hour_total"] for week in data.values())                
    exercises = sum(week["exercise_total"] for week in data.values())        
    hours_average = math.floor(hours / students)                             
    exercises_average = math.floor(exercises / students)                     

    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average
    }

if __name__ == "__main__":
   print(retrieve_all())
   print(retrieve_course("ofs2019"))


