import functools
from typing import Callable
import time


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Spell completed in {execution_time:.4f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self, spell_name, power, *args, **kwargs):
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        pass
            return f"Spell casting failed after {max_attempts}"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"successfully cast {spell_name} with {power} power"


@spell_timer
def fireball():
    """A simple spell that takes exactly 0.101 seconds to cast."""
    time.sleep(0.101)
    return "Fireball cast!"


if __name__ == "__main__":

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("Testing MageGuild...")

    print(MageGuild.validate_mage_name("Rae"))
    print(MageGuild.validate_mage_name("Jo"))

    my_guild = MageGuild()
    print(my_guild.cast_spell("Lightning", 15))
