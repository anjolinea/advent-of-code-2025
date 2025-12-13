
steps = list()
with open("input.txt") as f:
    for line in f:
        dir = line[0]
        rot = int(line[1:])
        steps.append((dir, rot))
        

def part_one():
    ans = 0
    point = 50
    for dir, rot in steps:
        if dir == 'R':
            point += rot
        else:
            point -= rot
        point = point % 100
        if point == 0:
            ans += 1

    print(ans)

def part_two():
    ans = 0

    before_point = None
    point = 50
    for dir, rot in steps:
        before_point = point
        if dir == 'R':
            point += rot
        else:
            point -= rot
        full_rot = abs(point) // 100
        if before_point > 0 and point <= 0:
            full_rot += 1
        point = point % 100
        ans += full_rot

    print(ans)

part_two()