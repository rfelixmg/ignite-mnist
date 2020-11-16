
if __name__ == "__main__":


	with open('/pvc/hello.text', 'w') as file_handler:
		file_handler.write("Hello world from file!\n")

	print("Hello world")