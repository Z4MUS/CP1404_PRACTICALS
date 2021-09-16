
from SEM_2_PRACTICALS.prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
# for language in languages:
#     print(language)

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        name = language.name
        print(name)

