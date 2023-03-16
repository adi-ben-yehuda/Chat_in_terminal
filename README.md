# Chat

## Introduction
Create a chat using UDP Protocol that allows clients to communicate with each other. All the messages in the chat sent to the server that manage the chat.

## Table of contents
* [General Information](#general-information)
* [Installation](#installation)
* [Project status](#project-status)
* [Contact](#Contact)


## General Information
This project gets one vector from the user. If the user enters invalid values (such as empty data, only spaces, data that includes characters that aren't numbers, etc), the program will be closed. If the user enters valid data, such as a vector that includes only numbers (integer, double or negative numbers), the data will be saved into a vector.
If the data in the database is invalid (such as when the vector is not only numeric or double values, not equal to the size of the vector that entered by the user), the program will be closed.
The algorithm will check which of the tagged vectors in the database are the K vectors closest to the new vector (this k we get from the user as an argument). The distance between the new vector and each of the vectors from the database is calculated using one of five algorithms (euclidean distance- AUC, taxicab geometry- MAN, Chebyshev distance- CHB, Canberra distance- CAN, or Minkowski distance- MIN), depending on the algorithm that the user entered as an argument.
Then, the algorithm takes the K closest ("similar") vectors to the input and checks what their labeling is. The classification of the new vector is based on the most common labeling among the k vectors. In the end, the program prints this classification to the terminal.

## Installation
Before installing this project, you need to install on your computer:
* Git

After it, run the following commands in the terminal:

```
git clone https://github.com/ShaharMosh/network_ex_1.git
```
Run the server:
```
python server.py port
```
For example: 
```
python server.py 12345
```
Open new terminals for the clients and run the following command:

```
python client.py ip port
```
For example: 
```
python client.py 127.0.0.1 12345
```
## Project status 
The project is in the beginning stages and will develop over time.

## Contact
Created by @adi-ben-yehuda and @ShaharMosh - feel free to contact us!
