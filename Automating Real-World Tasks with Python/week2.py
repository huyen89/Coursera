#!/usr/bin/env python3

import os
import requests

filepath = '/data/feedback'
filenames = os.listdir(filepath)
post_dict = {}
corpwebIP = "34.125.129.185"

for file in filenames:
    with open(os.path.join(filepath, file)) as review:
        post_dict["title"] = review.readline().rstrip()
        post_dict["name"] = review.readline().rstrip()
        post_dict["date"] = review.readline().rstrip()
        post_dict["feedback"] = review.readline().rstrip()

    response = requests.post(f"http://{corpwebIP}/feedback/", json=post_dict)
    print(response.request.body)
    print(response.ok)

    if response.status_code == 201:
        print("Post for file " + file + " was successful.")
    else:
        print("Post for file " + file + " occurred with error " + str(response.status_code) + ".")
