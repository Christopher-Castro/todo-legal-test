# Test Todo-Legal

This project was carried out using flask and Vue.js and is part of a test carried out for Todo-Legal company.

It consists of a simple login interface.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all python requirements.

```bash
pip install -r requirements.txt
```

Use npm package manager to install all Vue.js requirements.

```bash
cd frontend
npm install
```

## Build


Since flash (back-end) is rendering the project made in Vue.js (front-end), it is necessary to carry out a construction of said project; all this in order to just initialize the flask service instead of initializing the flask and Vue services separately.

```bash

cd frontend
npm run build
```

## Usage

Initialize the flask service

```python
python3 ./app.py
```

## AWS deploy example


Both services, including the mysql database, have been deployed using an AWS EC2 virtual machine.


[link to AWS example](http://ec2-13-58-131-42.us-east-2.compute.amazonaws.com:5000/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
