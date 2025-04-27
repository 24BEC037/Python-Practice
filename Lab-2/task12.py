def point_in_circle(cx, cy, r, x, y):
    distance_squared = (x - cx)**2 + (y - cy)**2
    r_squared = r**2
    if distance_squared < r_squared:
        return 'Inside'
    elif distance_squared == r_squared:
        return 'On'
    else:
        return 'Outside'