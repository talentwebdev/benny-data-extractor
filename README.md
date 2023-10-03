# Benny Interview Task - Data Extractor

## Overview

This project is small demo to extract data elements from unstructured data. 

- Data to extract:
    - When the contribution or offering period starts
    - When the contribution or offering period ends
    - What is the minimum that one can contribute
    - What is the maximum that one can contribute

## Approach 

Based on data inputs that are provided in the requirement, they seem to be complex and random 
text which doesn't have any rules to extract elements that we're looking for. 

The initial idea was to use RegEX to extract the elements but that requires to specify different 
patterns for each input. This sounds like not a best practice and not scalable in the future. 

To make it dynamic and scalable, I decided to integrate NLP library called `spaCy`. [Here's](https://spacy.io/) 
their official website. It's an open source. 

Knowing that I'm not a expert for ML and NLP, I'm not able to integrate it 100% correctly but, 
the approach that I took is to split the text by entities and check it's label if it's a date, money, or
percentage. Based on that, we're checking leading verbs, pronouns, and adjectives to detect if it's end or start date, 
min or maximum value. 

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
