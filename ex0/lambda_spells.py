def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key=lambda
                              artifacts: artifacts['power'], reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda mages: mages['power']
                                 >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells = list(map(lambda spells: '*' + spells + '*', spells))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mages: mages['power'])['power']
    min_power = min(mages, key=lambda mages: mages['power'])['power']
    avg_power = round(sum(map(lambda mages: mages['power'], mages)))
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


artifacts = artifact_sorter([
    {'name': 'Crystal Orb', 'power': 85, 'type': 'magic'},
    {'name': 'Fire Staff', 'power': 92, 'type': 'magic'}
])

spells = ['fireball', 'heal', 'shield']

mages = [
    {'name': 'alfred', 'power': 300},
    {'name': 'jesse', 'power': 200},
    {'name': 'walter', 'power': 350}
]
print("Testing artifact sorter...")
print(f"{artifacts[0].get('name')} ({artifacts[0].get('power')} power) "
      f"comes before {artifacts[1].get('name')} "
      f"({artifacts[1].get('power')} power)")

print("\nTesting spell transformer...")
for spell in spell_transformer(spells):
    print(spell, end=' ')
