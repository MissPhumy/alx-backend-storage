#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """
    Function to print stats about Nginx logs stored in MongoDB
    """
    # Count total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Print count for each HTTP method
    print("Methods:")
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count logs with method GET and path /status
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    # Connect to the MongoDB server and access the collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    # Run the log_stats function
    log_stats(nginx_collection)
