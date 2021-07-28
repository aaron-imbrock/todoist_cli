#!/home/aimbrock/src/todoist_cli/env/bin/python3

import sys, requests, uuid, json
from common.env import Data

if __name__ == "__main__":
    
    api_key = Data.todoist_api_key
    tasks = sys.stdin
    
    try:
        for task in tasks:
            task = task.rstrip()
            requests.post(
                "https://api.todoist.com/rest/v1/tasks",
                data=json.dumps({
                    "content": task,
                    "due_string": "tomorrow at 12:00",
                    "due_lang": "en",
                    "priority": 4
                }),
                headers={
                    "Content-Type": "application/json",
                    "X-Request-Id": str(uuid.uuid4()),
                    "Authorization": "Bearer %s" % api_key
                }).json()
        print(f'Added to Inbox: {task}')
    except:
        sys.stdout.flush()
