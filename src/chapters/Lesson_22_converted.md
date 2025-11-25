```markdown
# Lesson 22: Internet Data

Owner: Saban, Michael  
Reviewer: Jason for Saban, Michael

Per the Guidelines for Content the following items are missing:  
Overview & Introduction  
Assessment  
Summary  
Next steps  
Everything else looks fine.

## Learning Objectives

- Explain what an API is and how it provides structured access to online data.  
- Make HTTP requests to public APIs using Python’s `requests` module.  
- Parse JSON data returned from APIs.  
- Handle simple API errors (bad request, missing key, invalid parameters).  
- Use query parameters to customize requests.  
- Save API responses to files for later analysis.

## Introduction

Every day, you interact with online services powered by data: weather apps, maps, search 
engines, movie databases, translation tools, sports scores, and more. Much of this data is 
accessible to programmers through tools called APIs. APIs provide a structured way to 
request information from websites without needing to scrape messy HTML.

In this lesson, you’ll learn how to access real online data from Python, work with JSON, and 
handle basic errors that arise when requesting data.

---

# 1. What is an API?

API stands for Application Programming Interface. It defines a predictable way for 
applications to communicate with each other. Many websites expose public APIs that let you 
request data directly.

Examples:

- Weather services  
- News headlines  
- Public transportation schedules  
- Currency exchange rates  
- Sports statistics  
- GitHub repository information  

Most APIs use HTTP requests.

---

# 2. HTTP Basics

Common request types:

- **GET** – retrieve data  
- **POST** – send data  
- **PUT/PATCH** – update data  
- **DELETE** – remove data  

In this lesson, we will use only GET requests.

Example URL with query parameters:

```

[https://api.example.com/weather?city=Chicago&units=metric](https://api.example.com/weather?city=Chicago&units=metric)

```

---

# 3. Using the `requests` Module (15 min)

Install (if needed):

```

pip install requests

````

Basic example:

```python
import requests

url = "https://api.github.com"
response = requests.get(url)

print(response.status_code)
print(response.text)
````

Check status codes:

* 200 – OK
* 404 – Not Found
* 500 – Server Error
* 401 – Unauthorized

---

# 4. Parsing JSON

Most APIs return JSON.

```python
import requests

url = "https://api.github.com/repos/python/cpython"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["full_name"])
    print(data["stargazers_count"])
```

JSON is similar to Python dictionaries.

---

# 5. Query Parameters

```python
import requests

url = "https://api.example.com/search"
params = {"q": "python", "limit": 5}

response = requests.get(url, params=params)
print(response.url)
print(response.json())
```

---

# 6. Handling API Errors

```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code != 200:
    print("Error:", response.status_code)
else:
    print(response.json())
```

---

# 7. Saving Results to a File

```python
import requests
import json

url = "https://api.github.com/users/octocat"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("octocat.json", "w") as f:
        json.dump(data, f, indent=2)
```

---

# 8. Guided Practice

## Exercise 1: GitHub User Lookup

Write a program that:

* asks for a GitHub username
* requests user data
* prints number of followers, number of public repos

## Exercise 2: Country Information API

Use:

```
https://restcountries.com/v3.1/name/canada
```

Print:

* population
* region
* capital

## Exercise 3: Weather API (Mock Endpoint Provided)

Use:

```
https://api.open-meteo.com/v1/forecast?latitude=41.88&longitude=-87.62&hourly=temperature_2m
```

Print:

* first 5 temperature values
````markdown
# 9. Reflection & Discussion (5 min)

1. Why do APIs usually return JSON instead of plain text or HTML?  
2. What kinds of applications could you build using public data sources?  
3. Why is it important to check status codes before using API results?  
4. How could saving API data to files be useful for later analysis?  
5. What problems might occur when working with unreliable internet connections?

---

# 10. Assessment & Checks for Understanding (5 min)

- **Quick Questions**
  - What Python module do we use for making HTTP requests?
  - What method retrieves JSON directly from a response?
  - What does a 404 error mean?
  - What is the difference between a URL and query parameters?
  - Why should you handle API errors?

- **Mini Exercise**
  - Request data from:
    ```
    https://api.github.com/events
    ```
  - Print the type of the top-level data structure  
    (hint: it's usually a list).

---

# 11. Homework Assignment

Write a Python script named `city_info.py` that:

- Accepts a city name from the user  
- Uses an online API to look up:
  - coordinates  
  - population  
  - timezone  
- Prints out the data in a readable format  
- Saves the JSON response to `city_data.json`  
- Includes basic error handling:
  - invalid city  
  - connection errors  
  - missing fields  

Hint: Use the endpoint:

````

[https://geocoding-api.open-meteo.com/v1/search?name=Chicago](https://geocoding-api.open-meteo.com/v1/search?name=Chicago)

```

---

# 12. Challenge Problems (Optional)

### Challenge 1: API Pagination

Some APIs split large datasets across multiple pages.

Write a program that:

- automatically requests all pages  
- merges the results  
- prints the total number of items retrieved  

### Challenge 2: Build a Simple Data Dashboard

Request data from:

```

[https://api.publicapis.org/entries](https://api.publicapis.org/entries)

```

Display:

- number of public APIs  
- number of categories  
- first 10 API names  

### Challenge 3: Rate Limit Handling

Modify your programs to detect:

- HTTP 429 (Too Many Requests)

If detected:

- print a warning  
- wait 5 seconds  
- retry automatically  

---

# 13. Summary

In this lesson you learned how to:

- Use HTTP GET requests to retrieve online data  
- Work with public APIs  
- Parse JSON responses into Python dictionaries and lists  
- Handle errors from bad requests or invalid parameters  
- Use query parameters to customize API output  
- Save results for later use  

APIs allow your programs to interact with real-world information. Combined with skills from 
previous lessons—files, dictionaries, lists, loops—you now have the ability to collect, store, 
and analyze live data from the internet.

Next steps: In the upcoming lessons, you'll use internet data to build more advanced 
projects and explore topics like data visualization and automated workflows.
```

If you'd like this as a downloadable `.md` file or converted to `.rst`, just let me know.



