# this is a comment

color = ["red", 'red' ,'yellow', "green", "blue", "pink", "black", "purple", "red", "indigo"]
print(color)
selected_list = color[2:5]
print(selected_list)
# finding the length of lists
number_of_selected_colors = len(selected_list)
print(number_of_selected_colors)
print(len(color))
# counting words
number_of_times = color.count("red")
print(number_of_times)
print(color.count("yellow"))
index_for_green = color.index("green")
print("index for green is: %d" %index_for_green)
color.append("violet")
color.append("turquiose")
print(color)
