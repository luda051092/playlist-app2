### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is an open-source object-relational database. It is used to organize data into rows and columns.
PostgreSQL supports SQL in order to query the data. 
PostgreSQL supports ACID(Atomicity, Consistency, Isolation, Durability), which ensures data integrity even if there is a system failure.
PostgreSQL is extensible, which allows clients to define data types, operators, functions, and aggregates. It also
supports data types such as arrays, key-value pairs, JSON, and others. 
Multiple data transactions are allowed to occur at the same time without compromising data consistency. 
Vertical and horizontal scalability are supported on PostgreSQL, meaning that it is scalable on a both a single server,
or distributed among many servers.   


- What is the difference between SQL and PostgreSQL?
The difference between SQL and PostgreSQL is SQL is a language for managing and changing relational databases. PostgreSQL is a relational database management system that uses SQL. 
While SQL is a standardized language, PostgreSQL includes different features unique to itself while also supporting SQL. There are other database management systems that implement SQL in different manners.

- In `psql`, how do you connect to a database?
You can connect to a database in `psql` using:
psql - U (the postgreSQL username you wish to connect with) 
- d (the database name you wish to connect with)
-h (the host where the PostgreSQL server is running)
-p (the port on which the PostgreSQL server is listening)
example: psql -U myusername -d mydatabasename -h localhost -p 5432

- What is the difference between `HAVING` and `WHERE`?
`WHERE` is used to filter individual rows before any grouping/aggregating has taken place.
`HAVING` filters results of aggregate functions applied to rows already grouped.
`HAVING` is almost always followed by `GROUP BY`, to the point that `WHERE` is practically always
the appropriate choice if `GROUP BY` is not the follow up qualifier.

- What is the difference between an `INNER` and `OUTER` join?
`INNER JOIN` returns matching rows, `OUTER JOIN` returns all rows from one table and matching rows from another table,
missing values are filled in with `NULLS`.
`INNER JOIN` is the default type of join when the `JOIN` keyword is used on its own. If there is is not a matching value, nothing will be returned.
`OUTER JOIN` has a number of types: `LEFT OUTER JOIN`, `RIGHT OUTER JOIN` and `FULL JOIN`.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
In a `LEFT OUTER` join, all the rows from the left table are included in the result set. 
`NULL` will be returned if there is no match for a row in the right column.
In a `RIGHT OUTER` join, all rows from the right table are included in the results. If there is no corresponding match
in the left table, `NULL` will be returned, as in a `LEFT OUTER` join.

- What is an ORM? What do they do?
An Object-Relational Mapping allows data to be converted between the object-oriented programming language and a relational database management system. ORM's "bridge the gap" between the way data is represented in and application, and how it is stored as a table in a database. 
ORMs use object oriented languages such as Python to map the database tables to classes, and to map rows to objects. 
They allow for operations such as reading, deleting, and updating to be performed on the database records in the programming language as opposed to SQL. 


- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  - AJAX requests begin  and run from the client side, from the client's web browser. They are asynchronous, allowing for requests to be made without having to reload an entire page.
  `requests` are server-side, ansd are performed when HTTP requests are made from the server to external APIs.
  Becuase they originate from the client side, AJAX requests are subject to browser restrictions and have the possiblity of exposing sensitive information. 
  On the other hand, server side requests are less restricted by browser policies, are more secure due to their origin on a server, and are enabled to make requests to almost any domain, due to easier server-to-server communication.These types of requests are also able to manipulate a server's internal state, whereas AJAX, client-side requests are often used to simply fetch data. Thery update the UI without having to referesh the webpage. 



  
- What is CSRF? What is the purpose of the CSRF token?
CSRF is Cross-Site-Request-Forgery. These malicious attacks forge the user's login credentials and other authentication data if the user visits certain malicious websites. For example, if a user was doing some online shopping on a website,
and in the process visited a correspondng website with CSRF (such as, maybe, one with a function that could update a user's shipping address without their knowledge or consent), the malicious website could trigger a function that enables the nonconsensual update to occur, and the items purchased through the website could end up never reaching the user/customer. There are much more malicious types of CSRF, especially with regards to sensitive info such as bank accounts and social security numbers. 
CSRF tokens protect against these types of attacks. When a user logs onto a website that requires authentication, a unique CSRF token is created. The token is carried along in a hidden field in every form generated by a server. 
When a form is submitted by a user, the CSRF form is also included. The server checks the token submitted with every form 
against the token which belongs to the user's session. If the tokens do not match, the server rejects the made request. 

- What is the purpose of `form.hidden_tag()`?
`form.hidden_tag()` is used to include hidden forms and HTML markup in the WTForms in Flask-WTF (which is used for handling web forms and WTForms). It does this so that all hidden fields are included in the HTML form, and that the values associated with the hidden fields will be included in the form's HTML and will therefore be submitted along with visible form fields.  CSRF tokens, for example would need to be included using this method. 

