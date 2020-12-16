# **Web Reviews**
The purpose of this script is to upload feedback saved as text files automatically to the corporate website without having to format each file individually.

## **Structure**
* List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
```python
os.listdir("/data/feedback")
```
* Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively. Text files look like:
```
Good deal for a 2015 RAV4
Anonymous
2018-04-17
Called them to look for a second-hand RAV4 and they are very nice and patient 
to help me find a few matches then scheduled an appointment...
```
* Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
```python
review = [
  {
    "title": "Good deal for a 2015 RAV4",
    "name": "Anonymous",
    "date": "2018-04-17",
    "feedback": "Called them to look for a second-hand RAV4 and they are very nice and patient 
    to help me find a few matches then scheduled an appointment..."
  },
  {
  ...
  }
]
```
* Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to:
```
http://<corpweb-external-IP>/feedback/
```
Replace <corpweb-external-IP> with the corporate websites external IP address.
* Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
