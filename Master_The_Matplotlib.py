# Importing Matplot Library
import matplotlib.pyplot as plt

# <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#      Introductory Example What we gonna read
#               You Can Skip for Now
# <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
X = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
Y = [10, 15, 7, 20, 12, 15, 20]

plt.plot(X, Y)
plt.title("Bakery Sales this week")
plt.xlabel("Day of the week")
plt.ylabel("Sales per Day")
plt.show()


# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
#                   Pyplot Functions
# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
# <<<<<<<<<<<<<<<<<<<<<
#     1. plot() 
# <<<<<<<<<<<<<<<<<<<<<
# - Definition: A function that plots Y versus X as lines and/or markers.
# - Why we use it: To visualize trends, patterns, and relationships in continuous or sequential data over time.
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.show()


# <<<<<<<<<<<<<<<<<<<<<>>>>>>>
#    2. xlabel() , ylabel()
# <<<<<<<<<<<<<<<<<<<<<>>>>>>>
# - Definition: Functions that assign text labels to the horizontal (X) and vertical (Y) axes.
# - Why we use it: To give crucial context to the numbers on the grid so the viewer immediately knows what metrics are being measured.
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.xlabel("months")
plt.ylabel("sales per month")
plt.show()



# <<<<<<<<<<<<<<<<<<<<<
#      3. title()
# <<<<<<<<<<<<<<<<<<<<<
# 3 title()
# - Definition: A function that sets a central header text centered at the top of the plot canvas.
# - Why we use it: To immediately inform the audience about the core subject matter or main message of the entire visualization.
plt.title("Monthly Sales Data") # Fixed spelling typo "Mongthly"
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.xlabel("months")
plt.ylabel("sales per month")
plt.show()


 
# <<<<<<<<<<<<<<<<<<<<<
#      4.legend() it tell us what each line represent
# <<<<<<<<<<<<<<<<<<<<<
# you can pass location and fontsize inside it like 
# legend(loc = "upper left" , fontsize=12) top left
# (loc = "lower right")bottom right
# these are optional
# it will show only if we set the label
# - Definition: An overlay box that displays labels matching the color/style codes of your dataset plots.
# - Why we use it: Essential when tracking multiple datasets on a single grid to distinguish which line or shape belongs to which data category.
plt.title("Monthly Sales Data") # Fixed spelling typo "Mongthly"
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.xlabel("months")
plt.ylabel("sales per month")
plt.legend(loc="upper left")
plt.show()



# <<<<<<<<<<<<<<<<<<<<<
#       5. grid()
# <<<<<<<<<<<<<<<<<<<<<
# it is used to make box type line at the back side of the graph
# - Definition: Draws intersecting horizontal and vertical background line grids over the data canvas area.
# - Why we use it: It acts as a visual guide, allowing readers to accurately trace data point locations back to their precise axis values.
plt.title("Monthly Sales Data") # Fixed spelling typo "Mongthly"
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.xlabel("months")
plt.ylabel("sales per month")
plt.legend(loc="upper left")
plt.grid(color='gray', linestyle='--', alpha=0.6, linewidth=1)
plt.show()



# <<<<<<<<<<<<<<<<<<<<<
#       6. xlim() use to handle the x axis and y axis limit
# <<<<<<<<<<<<<<<<<<<<<
# - Definition: Configures explicit minimum and maximum boundary ranges for the display axis coordinates.
# - Why we use it: To crop out empty white margins, focus in heavily on specific coordinate windows, or standardize axes across separate charts.
plt.title("Monthly Sales Data") # Fixed spelling typo "Mongthly"
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.xlabel("months")
plt.ylabel("sales per month")
plt.legend(loc="upper left")
plt.grid(color='gray', linestyle='--', alpha=0.6, linewidth=1)
plt.ylim(0, 2000)
plt.show()


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     8. xticks() yticks()  we can give meaning full name to x and y axis points
# <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>
# plt.xticks([original] , [replace]) # Fixed spelling typo "orignal"
# - Definition: Customizes the placement positions and text labels of the ticks along the plot margins.
# - Why we use it: To replace plain, confusing numerical increments with custom human-readable text categories (like conversion of index values to 'Month' labels).
plt.title("Monthly Sales Data") # Fixed spelling typo "Mongthly"
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.xlabel("months")
plt.ylabel("sales per month")
plt.legend(loc="upper left")
plt.grid(color='gray', linestyle='--', alpha=0.6, linewidth=1)
plt.ylim(0, 2000)
plt.xticks([1, 2, 3, 4], ['M1', 'M2', 'M3', 'M4'])
plt.show()


# <<<<<<<<<<<<<<<<<<<<<
#      9. show() it used to to show everything on the screen like we read setVisible(true) in java swing # Fixed spelling typo "setVisable"
# <<<<<<<<<<<<<<<<<<<<<
# plt.xticks([original] , [replace]) # Fixed spelling typo "orignal"
# - Definition: Renders and pushes all currently active configured figures out onto your user-interface window layers.
# - Why we use it: It signals to Matplotlib that your chart design configuration steps are finished and internally flushes/resets the drawing canvas memory state clean for future commands.
plt.title("Monthly Sales Data") # Fixed spelling typo "Mongthly"
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1000]
plt.plot(months, sales, color='blue', linewidth=1.5, linestyle='--', label='2026 sales', marker='o')
plt.xlabel("months")
plt.ylabel("sales per month")
plt.legend(loc="upper left")
plt.grid(color='gray', linestyle='--', alpha=0.6, linewidth=1)
plt.ylim(0, 2000)
plt.xticks([1, 2, 3, 4], ['M1', 'M2', 'M3', 'M4'])
plt.show()









# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
#                Data Visualization
# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><

# <<<<<<<<>>>>>>>>>
#  1. Bar Charts
#       bar()
# <<<<<<<<>>>>>>>>>
# - **Why we use them:** To compare distinct **categories** against each other based on a specific metric or value count.
# - **Core Purpose:** Category comparison and comparative data analysis.
# vertical:  plt.bar(categories, headcount, color='skyblue', label = "Courses ML" , edgecolor='black', alpha=0.85) # Fixed spelling typo "verticle"
# horizontal: plt.barh(categories, headcount, color='skyblue', label = "Courses ML" , edgecolor='black', alpha=0.85)

categories = ['Data Science', 'Development', 'Design', 'HR', 'Finance']
headcount = [12, 18, 7, 4, 6]
plt.bar(categories, headcount, color='skyblue', label="Courses ML", edgecolor='black', alpha=0.85)
plt.xlabel('Departmental Resource Deployments')
plt.ylabel('Active Headcount Profiles')
plt.title("Data Science Scope")
plt.legend()
plt.show()



# <<<<<<<<>>>>>>>>>
#  2. Pie Charts
#      pie()
# <<<<<<<<>>>>>>>>>
# - **Why we use them:** To show how a static total dataset is divided up into slices, illustrating **proportions or percentages** of a whole.
# - **Core Purpose:** Proportion illustration and total "whole" representation (best used with a small number of categories that equal 100%)
# plt.pie(values = values list , labels=for 4 quadrants, colors = as a list of 4, autopct='%1.1f%%') # Fixed spelling typo "vales", "quardants"
# *Correction note: In Matplotlib, pass data as the first positional argument. 'values=' is invalid syntax.*

regions = ['North', 'East', 'West', 'South']
revenue = [3000, 2000, 1500, 1000]
plt.pie(revenue, labels=regions, colors=['gold', 'skyblue', 'yellow', 'pink'], autopct='%1.1f%%')
plt.title("Revenue contribution by region") # Fixed spelling typo "Revenu", "reagion"
plt.show()



# <<<<<<<<>>>>>>>>>
#   3. Histograms
#      hist()
# <<<<<<<<>>>>>>>>>
# hist(data , bins=number of bins , color , edgecolor) # Fixed functional typo from "his" to "hist"
# To show the distribution of the continuous data by dividing into the ranges
# - **Why we use them:** To show how a continuous set of numerical data is **distributed** across intervals or "bins" (e.g., seeing which age groups or price ranges are most common).
# - **Core Purpose:** Identifying numerical distribution patterns and uncovering statistical data insights.

scores = [50, 23, 44, 46, 56, 24, 77, 88, 23, 99, 56, 12]
plt.hist(scores, bins=5, color='purple', edgecolor='black')
plt.title("Score distribution of the student")
plt.xlabel('Score ranges')
plt.ylabel('Score Distribution ranges')
plt.show()















# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
#                    Scatter Plot
# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
# A Scatter plot is the graph where each point represent one observation # Fixed spelling typo "obsevation"
#  with two values x and y
# It is used to find co relation between values like if we improve input does out is improving # Fixed spelling typo "co relation"
# plt.scatter(x ,y ,color ,marker='style' ,label)

hours_study = [1, 2, 3, 4, 5, 6, 7, 8]
exam_score =  [50, 55, 60, 65, 70, 75, 80, 85] # Fixed missing closing bracket ']' here
plt.scatter(hours_study, exam_score, color='blue', marker='x', label='Student Data')
plt.xlabel('Hours study')
plt.ylabel('Exam_score')
plt.legend()
plt.title("Comparison of hours and score") # Fixed spelling typo "Camparetion"
plt.grid(True)
plt.show()




# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
#                    multi Example
# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
# We were working every thing single like single scatter
#  ,single plot , single pie chart now we will see single more 
# than one eg on it like single graph more that one plot

plt.scatter([1, 2, 3], [55, 60, 70], color='blue', marker='x', label='Class A')
plt.scatter([1, 2, 3], [50, 55, 65], color='red', marker='x', label='Class B')
plt.xlabel('Hours study')
plt.ylabel('Exam_score')
plt.title("Comparison of two classes") # Fixed spelling typo "Comparition"
plt.legend()
plt.grid(True)
plt.show()










# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
#                   Subplots and Layout Adjustments
# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
# Advantages:
# multi chart
# space
# Analyze related graphs # Fixed spelling typo "Analize"


# ><><><><>><><><><>><><><><>><><><><><><><><>
#               1. Subplots()
# ><><><><>><><><><>><><><><>><><><><><><><><>
# Can create in two ways
# Object oriented->   # a. subplot() # this is unprofessional we it set implicitly # Fixed spelling typo "un professional"
# Prefered Methods->  # b. fig,axes = plt.subplots() # Corrected method call from singular to plural "subplots()" to align with Object-Oriented style
                                  # we fix every thing explicit in our own way # Fixed spelling typo "explit"

# ><><><><>><><><
# a. subplot()
# ><><><><>><><><
# subplot(nrow ,ncol ,index ,figsize) #index start from 1 # Fixed spelling typo "insex strt"
X = [1, 2, 3, 4]
Y = [10, 20, 15, 25]

plt.subplot(1, 2, 1) # it means 1 row 2 column and 1st subplot # Fixed spelling typo "ccolumn"
plt.plot(X, Y)
plt.title("Line chart")

plt.subplot(1, 2, 2) # it means 1 row 2 column and 2nd subplot # Fixed spelling typo "ccolumn"
plt.bar(X, Y)
plt.title("Bar chart")

plt.tight_layout()
plt.show()

# ><><><><>><><><><>><><><><>><
# 2. fig, axes = plt.subplots()
# ><><><><>><><><><>><><><><>><
# fig, axes = plt.subplots(nrows,ncols, figsize=(width, height))
# in this we tell inside this that frame will be of this size and it will # Fixed spelling typo "fram"
# these rows and these column we can set then with index
# used when we need equal side of each graph

X = [1, 2, 3, 4]
Y = [10, 20, 15, 25]
fig, axes = plt.subplots(1, 2, figsize=(10, 5)) 

axes[0].plot(X, Y)
axes[0].set_title("Line chart")

axes[1].bar(X, Y)
axes[1].set_title("Bar chart")

plt.tight_layout()
plt.show()




# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
#               2. tight_layout()
# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
# And what if want to set global title here so it will another way to # Fixed spelling typo "an other"
# to set like fig.suptitle('Comparison of line and Bar charts')
# for separate on every graph we use set_title() here # Fixed spelling typo "grapg"
# it is used just before like when plot are not formatting good we do use it # Fixed spelling typo "formating"
X = [1, 2, 3, 4]
Y = [10, 20, 15, 25]
fig, axes = plt.subplots(1, 2, figsize=(10, 5)) 

axes[0].plot(X, Y)
axes[0].set_title("Line chart")

axes[1].bar(X, Y)
axes[1].set_title("Bar chart")

fig.suptitle('Comparison of line and Bar charts')
plt.tight_layout()
plt.show()














# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><
#             Saving Figures (Simple Beginner Guide) 
# ><><><><>><><><><>><><><><>><><><><><><><><><><><><><><><

# ><><><><>><><><><>
#     savefig() 
# ><><><><>><><><><>
# savefig(filename .extension , dpi = value , bbox_inches = 'tight')
# DPI: It controls the image resolution
# bbox_inches = 'tight' : It is used to crop the side white space and only the main chart

X = [1, 2, 3, 4]
Y = [10, 20, 15, 20]

plt.plot(X, Y, color='blue', marker='o', label='Plot')
plt.title("Simple Time plot")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.savefig('line_plot.png', dpi=100, bbox_inches='tight')
plt.show()