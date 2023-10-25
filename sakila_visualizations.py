from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

pymysql.install_as_MySQLdb()



'''
NOTES
connect mysql 
run query
access it via panda (es: input(rental_data) => data frame)
execute the quary -> connected to dataframe with n colums input(rental_data[column_name])

'''



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




#####################################################################################################




query = '''
SELECT customer.customer_id, SUM(payment.amount) AS total_payment_amount
FROM customer
JOIN payment ON customer.customer_id = payment.customer_id
group by customer.customer_id, customer.first_name;
'''
# Execute the SQL query and load the results into a pandas DataFrame
rental_data = pd.read_sql(query, engine)
# Set the figure size
plt.figure(figsize=(10, 6))
# Create a bar chart
plt.bar(rental_data['customer_id'], rental_data['total_payment_amount'])
# Customize the chart
plt.title('Rank customer by total payment')
plt.xlabel('customer ID')
plt.ylabel('total payment')
plt.xticks(rotation=45)  # Rotate category labels for readability
# Display the chart
plt.tight_layout()
plt.show()




#####################################################################################################




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




#####################################################################################################




query = '''
SELECT category.name AS category, film.rating
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
ORDER BY film.rating DESC;
'''

# Execute the SQL query and load the results into a pandas DataFrame
rental_data = pd.read_sql(query, engine)

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart
plt.bar(rental_data['category'], rental_data['rating'])

# Customize the chart
plt.title('Films with High Ratings in Each Category')
plt.xlabel('Category')
plt.ylabel('Rating')
plt.xticks(rotation=45)  # Rotate category labels for readability

# Display the chart
plt.tight_layout()
plt.show()




#####################################################################################################




query = '''
SELECT film.film_id,
    film.title,
    SUM(payment.amount) AS total_revenue
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN payment ON rental.rental_id = payment.rental_id
GROUP BY film.film_id, film.title
ORDER BY total_revenue DESC;
'''

# Execute the SQL query and load the results into a pandas DataFrame
rental_data = pd.read_sql(query, engine)

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart
plt.bar(rental_data['title'], rental_data['total_revenue'])

# Customize the chart
plt.title('movies with the highest revenue')
plt.xlabel('film title')
plt.ylabel('total_revenue')
plt.xticks(rotation=45)
# Reduce the font size of x-axis labels
plt.xticks(fontsize=2)
# Display the chart
plt.tight_layout()
plt.show()




#####################################################################################################