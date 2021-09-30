### **Beyonic API Python Examples.** 


**Install the Beyonic API Python Official client library** 


```python
pip install beyonic
```



**Docker file**

```Dockerfile
FROM python:3.6

COPY . .

COPY ./requirements.txt ./requirements.txt

WORKDIR .

RUN pip install -r requirements.txt


CMD [ "python3", "getExamples.py" ]
```

**Build docker image called demo** 

```docker
>>> docker build -t bey .
``` 

**Run docker image called demo**

```docker
>>>docker run -t -i bey 
```

