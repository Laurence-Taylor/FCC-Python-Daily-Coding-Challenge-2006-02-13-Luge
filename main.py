def get_fastest_speed(times):
    # Faster Speed Reference Variable
    faster_speed = 0
    # Creaet a list of segments distances
    dist_segments = [320, 280, 350, 300, 250]
    # Init segment counter
    segmen = 1
    # iterate over segments distances and times
    for time, distance in zip(times, dist_segments):
        # calculate segment speed
        speed = round(distance/time,2)
        # if speed is faster
        if speed > faster_speed:
            # update faster speed
            faster_speed = speed
            # storage faster segment
            faster_segment = segmen
        segmen += 1
    return f'The luger\'s fastest speed was {faster_speed} m/s on segment {faster_segment}.'

if __name__ == '__main__':
    print(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]))
    print()
    print(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]))
    print()
    print(get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]))
    print()
    print(get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]))