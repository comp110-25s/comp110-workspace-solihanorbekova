"""The goal of this exercise is to understand and write simple funtions."""

__author__: str = "730468843"


def main_planner(guests: int) -> None:
    """Brings all the functions together to plan the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for the number of people for the party"""
    return 2 * people


def treats(people: int) -> int:
    """Calculates the total amount of treats needed for the number of people for the tea party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
