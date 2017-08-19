#BAR CHART

'''Import pyplot library with plt abbreviation'''

import matplotlib.pyplot as plt

'''Create some data series'''

x1 = [1, 2, 3, 4]
y4 = [1, 3, 8, 4]

'''Instead of using the numbers in the data series we can replace
them with labels. Below we created a list of labels and then assigned
them to the x values using 'xticks'. We could do the same thing with 
the y values and use 'yticks'''

labels = ['Test 1', 'Test 2', 'Test 3', 'Test 4']
plt.xticks(x1, labels)

'''Here we made a my_color variable which contains a string of four colors 
which we will use to fill each bar.'''

my_colors = 'rgby'  #red, green, blue, yellow


'''Instead of plt.plot we use plt.bar to make a bar graph. The first two
arguments are again the x and y data series. The third argument is the bar color
which we set equal to my_colors which was our string of colors. The fourth
argument is the percentage with of the bar. If 1 is used the bars will run together.'''

plt.bar(x1, y4, color=my_colors, width=.8)

'''We again set the following three attributes of our graph.'''

plt.ylabel('Students Proficient')
plt.xlabel('Competencies')
plt.title('My Amazing Bar Chart', loc='center', fontsize=20)

'''Don't forget to SHOW your graph after all of your hard work!'''

plt.show()