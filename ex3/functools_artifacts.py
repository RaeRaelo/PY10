import functools
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    ops_map = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops_map:
        raise ValueError(f"Unknown magical operation: {operation}")
    if not spells:
        raise ValueError("Cannot reduce an empty spellbook!")

    func_to_apply = ops_map[operation]

    return functools.reduce(func_to_apply, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantments = {
        'fire_enchant': functools.partial(base_enchantment, power=50,
                                          element='fire'),
        'ice_enchant': functools.partial(base_enchantment,
                                         power=50, element='ice'),
        'lightning_enchant': functools.partial(base_enchantment,
                                               power=50, element='lightning')
    }
    return enchantments


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def cast_spell(arg):
        return f"Uknown magic type '{type(arg).__name__}'. Spell fizzled."

    @cast_spell.register(int)
    def _(power):
        return f"Casting Damage Spell: Deals {power} damage!"

    @cast_spell.register(str)
    def _(enchantment):
        return f"Casting Enchantment: Weapon glows with {enchantment} aura!"

    @cast_spell.register(list)
    def _(spell_list):
        results = []
        for item in spell_list:
            results.append(cast_spell(item))
        return "Multi-cast triggered:\n -> " + "\n -> ".join(results)

    return cast_spell


print("Testing spell reducer...")
my_spells = [40, 30, 20, 10]
print(f"Sum: {spell_reducer(my_spells, 'add')}")
print(f"Product: {spell_reducer(my_spells, 'multiply')}")
print(f"Max: {spell_reducer(my_spells, 'max')}")

print("\nTesting memoized fibonacci...")
print(f"Fib(10): {memoized_fibonacci(10)}")
print(f"Fib(15): {memoized_fibonacci(15)}")
