def _is_degenerate_triangle(sides):
	check_degenerate = [sides[0] + sides[1] == sides[2],
		sides[1] + sides[2] == sides[0],
		sides[2] + sides[0] == sides[1]]
		
	if True in check_degenerate:
		return True
	
	return False

def _is_triangle(sides):
	# Check all sides are greater than 0
	sides_gt0 = [side > 0 for side in sides]

	# Check any 2 sides >= last side
	sides_2_gtoe_3 = [sides[0] + sides[1] >= sides[2],
		sides[1] + sides[2] >= sides[0],
		sides[2] + sides[0] >= sides[1]]
		
	if False in sides_gt0 + sides_2_gtoe_3:
		return False

	return True

def equilateral(sides):
	if _is_triangle(sides):
		return sides[0] == sides[1] and sides[1] == sides[2] and sides[2] == sides[0]
	else:
		return False


def isosceles(sides):
	if _is_triangle(sides):
		return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]
	else:
		return False


def scalene(sides):
	if _is_triangle(sides):
		return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
	else:
		return False