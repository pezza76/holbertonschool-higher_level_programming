

import requests
import csv


def fetch_and_print_posts():
    
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        result = response.json()

        for i in result:
            print(i['title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        
        with open('posts.csv', 'w') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for i in result:
                filtered_post = {}
                for j in fieldnames:
                    filtered_post[j] = i[j]
            writer.writerow(filtered_post)
