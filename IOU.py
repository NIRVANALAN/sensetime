import math


class Box:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
	
	# @staticmethod
	def area(self):
		return self.x * self.h


def check_intersection(a, b, **kwargs):
	if type(a) is not Box:
		return None
	if b.x < a.x < b.x + b.w or b.x < a.x + a.w < b.x + b.w:
		if b.y < a.y < b.y + b.h or b.y < a.y + a.h < b.y + b.h:
			return True
		return False


def iou(a, b):
	if check_intersection(a, b):
		x = sorted([a.x, a.x + a.w, b.x, b.x + b.w])[1:3]
		y = sorted([a.y, a.y + a.h, b.y, b.y + b.h])[1:3]
		return (x[1] - x[0]) * (y[1] - y[0])
	return None


if __name__ == '__main__':
	a = Box(20, 20, 80, 100)
	b = Box(50, 70, 100, 100)
	print(iou(a, b))
	
