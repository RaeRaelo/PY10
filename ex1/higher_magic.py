from typing import Callable, Any


def spell_combiner(spell: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args, **kwargs):
        result1 = spell(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def spell_multiplier(*args, **kwargs):
        original_power = base_spell(*args, **kwargs)
        return original_power * multiplier
    return spell_multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def checker(*args, **kwargs):
        if condition():
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return checker


def spell_sequence(spells: list[Callable]) -> Callable:
    def wrapper(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return wrapper


if __name__ == "__main__":
    def fireball(target: Any) -> str:
        return f"Fireball hits {target}"

    def heal(target: Any) -> str:
        return f"Heals {target}"

    def base_damage():
        return 10

    def is_daytime():
        return True

    def is_nighttime():
        return False

    print("Testing spell combiner...")
    combined_cast = spell_combiner(fireball, heal)

    res1, res2 = combined_cast("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_damage = power_amplifier(base_damage, 3)
    print(f"Original: {base_damage()}, Amplified: {mega_damage()}")

    print("\nTesting conditional caster...")
    day_spell = conditional_caster(is_daytime, fireball)
    night_spell = conditional_caster(is_nighttime, fireball)
    print(f"Daytime cast: {day_spell('Goblin')}")
    print(f"Nighttime cast: {night_spell('Goblin')}")

    print("\nTesting spell sequence...")
    combo_attack = spell_sequence([fireball, heal, fireball])
    print(f"Sequence results: {combo_attack('Orc')}")
