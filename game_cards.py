import file_operations
from faker import Faker
import random
import os


ANCIENT_ALPHABET = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}

SKILLS_LST = [
    "Стремительный прыжок", 
    "Электрический выстрел", 
    "Ледяной удар", 
    "Стремительный удар", 
    "Кислотный взгляд", 
    "Тайный побег", 
    "Ледяной выстрел", 
    "Огненный заряд"
]

DIRECTORY = os.path.join(os.path.dirname(__file__), 'cards')


def create_directory():
    os.makedirs(DIRECTORY, exist_ok=True)


def transform_letters(number_of_card):
    skills = list(random.sample(SKILLS_LST, 3))
    runic_skills = []

    for number in skills:
        for letter in ANCIENT_ALPHABET:
            number = number.replace(letter, ANCIENT_ALPHABET[letter])
        runic_skills.append(number)

    the_1_skill = runic_skills[0]
    the_2_skill = runic_skills[1]
    the_3_skill = runic_skills[2]

    fake = Faker("ru_RU")

    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": the_1_skill, 
        "skill_2": the_2_skill, 
        "skill_3": the_3_skill
    }

    filename = "charsheet-{number_of_card}.svg".format(number_of_card=number_of_card)
    filepath = os.path.join(DIRECTORY, filename)
    file_operations.render_template("charsheet.svg", filepath, context)


def main():
    create_directory()
    for number_of_card in range(1, 11):
        transform_letters(number_of_card)


if __name__ == '__main__':
    main()