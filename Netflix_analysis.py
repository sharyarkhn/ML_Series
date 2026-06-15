import matplotlib.pyplot as plt  # For creating all the charts and plots
import numpy as np  # For handling numerical operations
import pandas as pd  # For data loading and manipulation

# Load the raw CSV file into a structured DataFrame
df = pd.read_csv("netflix_titles.csv")

# Remove rows where crucial visualization data is missing
df = df.dropna(subset=["type", "release_year", "rating", "duration"])

# ====================================================
# CHART 1: MOVIES VS TV SHOWS BAR CHART
# ====================================================

# Count occurrences of 'Movie' and 'TV Show' in the type column
type_count = df["type"].value_counts()

plt.figure(figsize=(6, 4))  # Initialize a canvas of 6x4 inches
# Use index (labels) for x-axis, values (counts) for y-axis
plt.bar(type_count.index, type_count.values, color=["teal", "red"])
plt.title("Number of Movies vs TV shows on Netflix")  # Set chart title
plt.xlabel("Type")  # Label the horizontal axis
plt.ylabel("Count")  # Label the vertical axis
plt.tight_layout()  # Adjust margins to prevent text clipping
plt.savefig("Movies vs TV shows Bar.png")  # Save the figure to local storage
plt.show()  # Display the plot in the output window

# ====================================================
# CHART 2: CONTENT RATING PIE CHART
# ====================================================

# Count total titles belonging to each content rating group (TV-MA, PG-13, etc.)
rating_counts = df["rating"].value_counts()

plt.figure(figsize=(6, 4))  # Initialize a canvas of 6x4 inches
# autopct calculates percentages to 1 decimal place; startangle=90 starts from the top
plt.pie(
    rating_counts,
    labels=rating_counts.index,
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Percentage of Content Rating")  # Set chart title
plt.tight_layout()  # Automatically adjust layout spacing
plt.savefig("content_rating.png")  # Export chart as an image
plt.show()  # Display the pie chart

# ====================================================
# CHART 3: MOVIE DURATION HISTOGRAM
# ====================================================

# Isolate movie entries and make a explicit copy to prevent slice warning flags
movie_df = df[df["type"] == "Movie"].copy()

# Strip out the string ' min' and force convert the numbers into integer format
movie_df["duration_int"] = pd.to_numeric(
    movie_df["duration"].str.replace(" min", "", regex=False), errors="coerce"
)
# Drop any rows where the duration conversion failed (turned into NaN)
movie_df = movie_df.dropna(subset=["duration_int"])

plt.figure(figsize=(8, 6))  # Setup an 8x6 inch plot window
# Plot distribution grouped into 30 distinct historical runtime buckets
plt.hist(
    movie_df["duration_int"], bins=30, color="purple", edgecolor="black"
)
plt.title("Distribution of Movies Duration")  # Title the chart
plt.xlabel("Duration (minutes)")  # X-axis label
plt.ylabel("Number of movies")  # Y-axis label
plt.tight_layout()  # Keep margins tight and neat
plt.savefig("Movies Duration Histogram.png")  # Save plot locally
plt.show()  # Display histogram

# ====================================================
# CHART 4: RELEASE YEAR SCATTER PLOT
# ====================================================

# Compute content counts by release year and order them sequentially by year
release_counts = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10, 6))  # Open a wider 10x6 canvas for time data
# Plot individual dots using year as X and volume count as Y
plt.scatter(release_counts.index, release_counts.values, color="blue")
plt.title("Release Year VS Number of Shows")  # Add chart title
plt.xlabel("Release year")  # Add X axis text
plt.ylabel("Number of Shows")  # Add Y axis text
plt.tight_layout()  # Optimize canvas layout
plt.savefig("release_year_scatter.png")  # Save file to disk
plt.show()  # Render the scatter plot

# ====================================================
# CHART 5: TOP 10 COUNTRIES BAR CHART
# ====================================================

# Group counts by country and pull out only the top 10 highest entries
country_counts = df["country"].value_counts().head(10)

plt.figure(figsize=(8, 6))  # Initialize an 8x6 inch window
# Draw horizontal bars (barh) so country text strings are easily readable
plt.barh(country_counts.index, country_counts.values, color="teal")
plt.title("Top 10 Countries By Number of Shows")  # Set visual title
plt.xlabel("Number of Shows")  # Set scale axis label
plt.ylabel("Country")  # Set category axis label
plt.gca().invert_yaxis()  # Invert axis so the top producer stays at the peak
plt.tight_layout()  # Format layout margins
plt.savefig("Top10_countries.png")  # Export the chart as an image
plt.show()  # Render horizontal bars

# ====================================================
# CHART 6: SIDE-BY-SIDE TREND LINES
# ====================================================

# Group data by year + type, separate types into columns, fill empty gaps with zero
content_by_year = (
    df.groupby(["release_year", "type"]).size().unstack().fillna(0)
)

# Build a grid layout containing 1 row and 2 distinct subplots
fig, Axes = plt.subplots(1, 2, figsize=(12, 5))

# Draw a continuous line plot for Movies in the first (left side) layout box
Axes[0].plot(content_by_year.index, content_by_year["Movie"], color="blue")
Axes[0].set_title("Movies Released Per Year")  # Subplot 1 title
Axes[0].set_xlabel("Year")  # Subplot 1 X label
Axes[0].set_ylabel("Number of movies")  # Subplot 1 Y label

# Draw a continuous line plot for TV Shows in the second (right side) layout box
Axes[1].plot(content_by_year.index, content_by_year["TV Show"], color="green")
Axes[1].set_title("TV shows Released Per Year")  # Subplot 2 title
Axes[1].set_xlabel("Year")  # Subplot 2 X label
Axes[1].set_ylabel("Number of TV Shows")  # Subplot 2 Y label

fig.suptitle(
    "Comparison of Movies and TV Shows Released Per Year"
)  # Global main title
plt.tight_layout()  # Fit both charts safely inside the window bounds
plt.savefig("Comparison.png")  # Save dual line comparison figure
plt.show()  # Output final visualization panel
