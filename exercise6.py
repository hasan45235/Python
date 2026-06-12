exercises = {
    "Chest": ["Bench", "Dumbbell Press", "Dumbbell Flies", "Push Ups"],
    "Back":  ["Pull Ups", "Rowings", "Pull Downs", "Deadlifts"],
    "Shoulder": ["Dumbbell Press", "Lateral Raise", "Front Raise", "Shrugs"]
}


userInp = input("Enter Body Part: ")
fetchedExercises = exercises.get(userInp.capitalize()) or ["Not Found"]

for i in fetchedExercises:
    print(i)