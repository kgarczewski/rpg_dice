import random

possible_dices_1 = (
     "D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def roll_the_dice(dice_code):
    for dice in possible_dices_1:
        if dice in dice_code:
            try:
                amount, modifier = dice_code.split(dice)
            except ValueError:
                return "wrong input"
            dice_value = int(dice[1:])
            break
    try:
        amount = int(amount) if amount else 1
    except ValueError:
        return "wrong input"
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "wrong input"
    return sum([random.randint(1, dice_value) for _ in range(amount)]) + modifier


print(roll_the_dice("D12-1"))