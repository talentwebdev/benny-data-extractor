# Benny Interview Task - Data Extractor

## Overview

This project is small demo to extract data elements from unstructured data. 

- Data to extract:
    - When the contribution or offering period starts
    - When the contribution or offering period ends
    - What is the minimum that one can contribute
    - What is the maximum that one can contribute

## Approach 

The provided data inputs appear to be complex, consisting of intricate and seemingly random text. 
This lack of consistent patterns makes it challenging to extract the desired elements.

Initially, I considered using RegEX (Regular Expressions) for extraction. However, 
this would necessitate the creation of unique patterns for each input, which
may not be scalable or efficient in the long run. 

To foster scalability and flexibility, I chose to integrate the NLP library, spaCy. 
You can find more about it on [their official website](https://spacy.io/). It's worth noting that spaCy is open-source.

While I don't profess to be an expert in ML (Machine Learning) or NLP (Natural Language Processing), 
the approach I've adopted involves segmenting the text by entities. I then evaluate 
these entities based on their labels—namely date, money, or percentage. 
To further classify these as start or end dates, or minimum or maximum values, 
I examine preceding verbs, pronouns, and adjectives.

## How to Install and Run application? 

### Install `virtualenv` 

```bash
python venv -m env3
```

Activate virtual env. 
```bash
source env3/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Install or Download spacy model. 

```bash
python -m spacy download en_core_web_sm
```

### Run application

```bash
python main.py
```

## Additional Notes

From my perspective, to get better results, we'd like to setup own ML process 
by utilizing NLP libraries. 

I had some experience in NLP project before which is authorship determination, 
and contract cheating module. We used `spacy` there to determine authorship of document
and detect contract cheating. 

I'd like to elaborate about that in interview. 

**Elapsed Time**: 4 hours
