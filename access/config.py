from djchoices import ChoiceItem, DjangoChoices


class GenderChoices(DjangoChoices):
    """Choices for user gender"""

    male = ChoiceItem("male", "Male")
    female = ChoiceItem("female", "Female")
    others = ChoiceItem("others", "Others")
