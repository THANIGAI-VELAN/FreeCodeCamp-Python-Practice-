full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):

    # --- Validate name ---
    if not isinstance(name, str):
        return "The character name should be a string."

    if len(name) > 10:
        return "The character name is too long."

    if " " in name:
        return "The character name should not contain spaces."

    # --- Pack stats ---
    stats = [strength, intelligence, charisma]

    # --- Validate stats type ---
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers."

    # --- Validate minimum ---
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1."

    # --- Validate maximum ---
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4."

    # --- Validate total ---
    if sum(stats) != 7:
        return "The character should start with 7 points."

    # --- Build stat bar helper ---
    def build(label, value):
        return f"{label} " + ("●" * value) + ("○" * (10 - value))

    # --- Final output ---
    return (
        f"{name}\n"
        f"{build('STR', strength)}\n"
        f"{build('INT', intelligence)}\n"
        f"{build('CHA', charisma)}"
    )
print(create_character("ren", 4, 2, 1))
