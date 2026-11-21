import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
            'user_id': int(user_elem.find('user_id').text),
            'name': user_elem.find('name').text,
            'age': int(user_elem.find('age').text),
            'weight': int(user_elem.find('weight').text),
            'fitness_level': user_elem.find('fitness_level').text,
            'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []

def load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
            'workout_id': int(workout_elem.find('workout_id').text),
            'user_id': int(workout_elem.find('user_id').text),
            'date': workout_elem.find('date').text,
            'type': workout_elem.find('type').text,
            'duration': int(workout_elem.find('duration').text),
            'distance': float(workout_elem.find('distance').text),
            'calories': int(workout_elem.find('calories').text),
            'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
            'intensity': workout_elem.find('intensity').text
            }
            workouts.append(workout)
        return workouts    
    except FileNotFoundError:
        print("Файл не найден")
        return []


def main():
    users = load_users_data()
    workouts = load_workouts_data()
    get_stats(users, workouts)

def get_stats(users, workouts):
    print("ОБЩАЯ СТАТИСТИКА")
    print("===========================")
    print(f"Всего тренировок: {len(workouts)}")
    print(f"Всего пользователей: {len(users)}")
    print(f"Сожжено калорий: {sum(w['calories'] for w in workouts)}")
    print(f"Общее время: {round(sum(w['duration'] for w in workouts) / 60, 1)} часов")
    print(f"Пройдено дистанции: {sum(w['distance'] for w in workouts)} км")

def analyze_user_activity(users):
    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")

if __name__ == "__main__":
    main()