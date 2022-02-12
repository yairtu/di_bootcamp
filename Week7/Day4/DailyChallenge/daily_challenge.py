def divide(*args, **kwargs):
	try:
		return 5 / 0
	except ZeroDivisionError:
		print("Sorry cannot divide by zero" + e)
	except Exception:
		print("Another issue here")
	finally:
		print("This message will always print")


divide()