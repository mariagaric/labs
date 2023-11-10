#Lab2

points_person = {}

with open("score2.txt", 'r') as file:
    for line in file:
        elements = line.strip().split()  
        if elements[0] == "upg.":
            name = f"{elements[2]} {elements[3]}"
            points = int(elements[4])

            if name in points_person:
                points_person[name] += points
            else:
                points_person[name] = points

max_points = max(points_person.values())

top_scorers = [name for name, points in points_person.items() if points == max_points]

for name in top_scorers:
    print(f"{name} got the most points: {max_points} points.")
