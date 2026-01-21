def get_hurt(current_health, damage):
    current_health -= damage
    if current_health < 0:
        current_health = 0
    return current_health
