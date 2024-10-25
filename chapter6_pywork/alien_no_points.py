alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned')

#leaving out the value in get
no_value = alien_0.get('points')

print(no_value)

print(point_value)