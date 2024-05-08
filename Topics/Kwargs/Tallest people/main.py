def tallest_people(**people):
  max_height = max(people.values())

  tallest = {name: height for name, height in people.items() if height == max_height}

  for name, height in sorted(tallest.items()):
    print(f"{name} : {height}")
