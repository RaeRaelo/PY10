from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    scaled_power = initial_power

    def scaler(power_to_add: int) -> int:
        nonlocal scaled_power
        scaled_power += power_to_add
        return scaled_power
    return scaler


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any):
        memory[key] = value
        return f"Stored [{key}: {value}]"

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


print("Testing mage counter...")
count = mage_counter()
print(f"Call 1: {count()}")
print(f"Call 2: {count()}")
print(f"Call 3: {count()}")

flame = enchantment_factory("Flaming")
freeze = enchantment_factory("Frozen")
print("\nTesting enchantment factory...")
print(flame("Sword"))
print(freeze("Shield"))
