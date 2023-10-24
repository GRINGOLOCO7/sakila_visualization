from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

pymysql.install_as_MySQLdb()

# Replace 'username' and 'password' with your MySQL username and password
engine = create_engine('mysql://root:Stambek7@localhost/sakila')

query = """
SELECT c.name AS category, COUNT(r.rental_id) AS rental_count
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY category;
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data = pd.read_sql(query, engine)


# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart
plt.bar(rental_data['category'], rental_data['rental_count'])

# Customize the chart
plt.title('Number of Rentals by Category')
plt.xlabel('Category')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)  # Rotate category labels for readability

# Display the chart
plt.tight_layout()
plt.show()

query = """
SELECT DATE(rental_date) AS rental_day, COUNT(rental_id) AS rental_count
FROM rental
GROUP BY rental_day;
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data = pd.read_sql(query, engine)

# Set the figure size
plt.figure(figsize=(12, 6))

# Create a time-series line chart
plt.plot(rental_data['rental_day'], rental_data['rental_count'], marker='o', linestyle='-')

# Customize the chart
plt.title('Rental Count Over Time')
plt.xlabel('Rental Day')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

# Display the chart
plt.tight_layout()
plt.show()