from pet_projects.bonus1 import feet_inches


def parse(feet_nches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches":inches}
