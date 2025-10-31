"""
Estimate: 20 mins
Actual Time: 35 mins
"""

from prac_06.ProgrammingLanguage import ProgrammingLanguage


def main():
    """Create ProgrammingLanguage objects and display information about them."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print one language to test __str__ output
    print(python)

    # Store languages in a list
    languages = [python, ruby, visual_basic]
    print(languages)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
