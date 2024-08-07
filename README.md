# Distributed LLM Assignment (python, node.js)_240801
## Installation

```bash
# Clone the repo.
git clone https://github.com/Mundiaem/Distributed-LLM-Assignment-python-node.git;

# Goto the cloned project folder.
cd Distributed-LLM-Assignment-python-node;
```

## Running Docker Images


```bash
# With Docker

# Note: It is assumed here that you have Docker running in the background.

# Run the app in docker as a foreground process
docker-compose up --build 

# Run the app in docker as a background process
docker-compose up -d
```

## Python app
Using Flask to build a Restful API Server.
#### Features
1. When program starts, User can select model (**Llama2** and **mistral)**
2. User can send query on the selected model. and get answer from LLM.
3. Keeps communication context between user and llm (previous questions continuously, like chatgpt keeping conversation context)


### Extension:


- Testing: [Flask-Testing](http://flask.pocoo.org/docs/0.12/testing/)

### Prerequisites
 - huggingface-hub==0.24.5
 - Flask==3.0.3
- Flask-Cors==4.0.1
 - numpy==1.26.4
 - tokenizers==0.19.1
 - transformers==4.44.0

### Install, Configure & Run

```bash
# Without Docker
$  cd python-dist

$  python3 -m venv venv

$  source venv/bin/activate.csh
# Install pip3 packages.
$  pip3 install -r requirements.txt
# Run the program
$  python3 app.py
```

## Node api

 ### Features

1. Send query to the above python program
   - it sends selected model, and question on the body
2. list conversation history.(order by Date DESC)
3. specific conversation’s detail
   - list of the questions and responses on a specific conversation

### Install, Configure & Run 

```bash
# Without Docker

# Install NPM dependencies.
cd node-app
npm install;

# Run the app
npm start;
```
    
 