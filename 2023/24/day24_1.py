# Gets the y function in the form of y=kx+m
# Returns [k, m]
def get_y_function(positions, velocities):
    x, y = positions[:2]
    x_velocity, y_velocity = velocities[:2]

    k = y_velocity / x_velocity

    m = y - x * k
    #print(k, m)
    return (k, m)

hailstones = []
with open("W:\\adventofcode\\2023\\24\\day24_data.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        current_line = line.strip()
        positions = tuple(int(pos.strip()) for pos in line.split('@')[0].split(','))
        velocities = tuple(int(vel.strip()) for vel in line.split('@')[1].split(','))

        y_function = get_y_function(positions,velocities)

        hailstones.append((positions, velocities, y_function))


        #break

#print(hailstones)

printt = False

intersections = 0

test_area_min = 200000000000000
test_area_max = 400000000000000

for i, hailstone1 in enumerate(hailstones):
    y1 = hailstone1[2]
    init_x1 = hailstone1[0][0]
    init_y1 = hailstone1[0][1]
    vel_x1 = hailstone1[1][0]
    vel_y1 = hailstone1[1][1]

    #print(i)
    for j in range(i+1, len(hailstones)):
        y2 = hailstones[j][2]
        init_x2 = hailstones[j][0][0]
        init_y2 = hailstones[j][0][1]
        vel_x2 = hailstones[j][1][0]
        vel_y2 = hailstones[j][1][1]

        # print(y1, y2)
        # print(y1, y2)

        #print(y1[0])
        x = y1[0] - y2[0]

        m = y2[1] - y1[1]
        # print(m)

        if x == 0:
            if printt: print(f"The paths {i, j} do not intersect :(")
        else:
            intersect_x = m/x
            intersect_y = y1[0]*intersect_x + y1[1]
            # print(intersect_x, init_x1, init_x2)


            # # # (x - x1)/velocity1 >=0 would maybe work instead?
            #if intersect_x < init_x1 or intersect_x < init_x2:
            # print(init_x1 < intersect_x and vel_x1 < 0)
            # print(init_x2 < intersect_x and vel_x2 < 0)
            # print(init_x1 > intersect_x and vel_x1 > 0)
            # print(init_x2 > intersect_x and vel_x2 > 0)
            if (init_x1 < intersect_x and vel_x1 < 0 or init_x2 < intersect_x and vel_x2 < 0
                or init_x1 > intersect_x and vel_x1 > 0 or init_x2 > intersect_x and vel_x2 > 0):
                if printt: print(f"The paths {i, j} intersected in the past")
            elif test_area_min <= intersect_x <= test_area_max and test_area_min <= intersect_y <= test_area_max:
                intersections += 1
                if printt: print(f"The paths {i, j} intersects within the test area with x={intersect_x} and y={intersect_y}!")
            else:
                if printt: print(f"The paths {i, j} intersects outside the test area with x={intersect_x} and y={intersect_y} :(")
        
    #     break
    # break

print(intersections)

#8096 is too low