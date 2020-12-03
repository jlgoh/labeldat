# LabelDat

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) [![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg)](https://microsoft.github.io/codeofconduct/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

<p align="center">
    <img src="https://raw.githubusercontent.com/jlgoh/labeldat/master/logo.png" width="553" height="261">
</p>

LabelDat is a web application built to streamline the labelling process for machine learning users.

## Background

As companies are moving to digitalisation, data volume has rapidly increased. Machine learning systems often require massive amounts of data to set up a foundation for reliable learning patterns. Data labelling is an important part of data processing in supervised machine learning, which uses labelled data for classification to supply a learning basis for future data processing.

## Features

LabelDat helps in labelling datasets of various forms such as image, audio, video, and text. LabelDat also provides an intuitive interface for users to carry out labelling and helps to keep track of progress through comprehensive dashboards. Data can be imported and exported seamlessly.
LabelDat incorporates machine learning assisted suggestions to speed up the labelling process than pure manual work while keeping an error rate below what a pure artificial intelligence labelled dataset would do, reducing both time and cost of labelling data.

## Tech Stack Used

<b>Built with</b>

- [React](https://reactjs.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [MySQL Database](https://www.mysql.com/)

## Installation

### Frontend: React.js

1. Install dependencies for frontend
   ```
   cd frontend
   npm install
   ```
2. Run development server
   ```
   npm start
   ```

### Backend: Flask

1. Setup virtual environment, activate and install necessary packages

   For Windows :

   ```
   python3 -m venv venv
   venv\Scripts\activate
   pip3 install -r requirements.txt
   ```

   For Mac :

   ```
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```

2. If you install other packages, please add them to requirements.txt
   ```
   venv\Scripts\activate
   pip3 freeze > requirements.txt
   ```
3. Start the Flask server
   ```
   venv\Scripts\activate
   python3 main.py
   ```

### Database: MySQL

For Windows :

1. Go to SQL's [Windows MSI Installer Download Page](https://dev.mysql.com/downloads/installer/) and follow setup instructions (Default port should be 3306)
2. Create a database for our data with the following commands on MySQL Shell.
   ```
   \sql
   \connect root@localhost
   ```
3. Type in password for root.
4. Continue with the command below on MySQL Shell.
   ```
   create schema ase;
   ```

For Mac :

1. Download mysql 8.0.x using Homebrew, then start MySQL server
   ```
   brew install mysql@8.0
   brew services start mysql
   ```
2. Create a database for our data.
   ```
   mysql -u root < "create schema ase;"
   ```
3. Change password for root user. Run `mysql -u root` first to get into mysql console. Then run this to change password to **toor** (standardised)
   ```
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'toor';
   ```

## License

MIT © [Jun Le Goh](https://github.com/jlgoh/labeldat/blob/master/LICENSE.txt)
