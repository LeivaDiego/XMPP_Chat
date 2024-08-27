# XMPP Chat Client
---
**Universidad del Valle de Guatemala**\
**Facultad de Ingeniería**\
**Departamento de Ciencias de la Computación**\
**Redes**

---

## Author
- **Diego Leiva**

---
## Project Overview
### 1. Introduction
The primary objective of this project was to develop an instant messaging client that supports the XMPP protocol, adhering to industry standards. The project aimed to provide a comprehensive understanding of the XMPP protocol, including the functionality of its services, while applying the knowledge acquired in network programming and adhering to best development practices.


### 2. Project Objectives
- **Standards-Based Protocol Implementation**: Develop an XMPP client that complies with established protocol standards.
- **Comprehension of XMPP Protocol**: Gain a deep understanding of the XMPP protocol, its purpose, and functionality.
- **Understanding XMPP Services**: Learn how XMPP services work and how to effectively utilize them.
- **Application of Web and Mobile Programming Skills**: Leverage skills from Web and Mobile programming while adhering to best development practices.

## Setup and Installation
### 1. Prerequisites
Ensure you have the following prerequisites before setting up the project:

- `Python 3.8+` (Recommended)
- `Conda` (Optional, but recommended for better environment management)

### 2. Setting Up the Environment
You can set up the environment using either Conda or Python's built-in venv. Follow the steps below based on your preference:

#### 2.1. Clone the Repository
Begin by cloning the project repository from GitHub:
```bash
git clone https://github.com/LeivaDiego/XMPP_Chat.git
```

#### 2.2. Setting Up with Conda
1. **Create a Conda Environment**
    Use the provided `environment.yml` file to create a new **Conda** environment with all necessary dependencies:
    ```bash
    conda env create -f environment.yml
    ```
2. **Activate the Conda Environment**
    After creating the environment, activate it using the following command:

    ```bash
    conda activate <your-environment-name>
    ```

#### 2.3. Setting Up with Python venv
Alternatively, if you prefer using `pip`, you can set up the environment with **venv**:

1. **Create a Virtual Environment**
    Navigate to the project directory and create a virtual environment:
    ```bash
    python -m venv xmpp_env
    ```

2. **Activate the Virtual Environment**
    Activate the environment:

    - On Windows:
        ```commandline
        .\xmpp_env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source xmpp_env/bin/activate
        ```
3. **Install Dependencies**
    Install the required dependencies from the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Running the Application
Once the environment is set up, you can run the application using the following command:

```bash
python main.py
```

This command starts the XMPP client and presents you with the initial menu to log in, register, or exit.

### 4. Dependencies
The project relies on the following key libraries and dependencies:

- `Slixmpp`: The core library for implementing the XMPP protocol.
- `Asyncio`: Used for managing asynchronous tasks within the application.
- `Tkinter`: For the graphical user interface (GUI).

These dependencies are listed in the following files:

- `Conda`: environment.yml
- `Pip`: requirements.txt
  

### 5. Additional Notes
Both `environment.yml` and `requirements.txt` files are provided to accommodate different environment setups.
Make sure to activate the environment (**conda** or **venv**) each time before running the application.

---

## Project Report


### 1. Implemented Features
The following features have been successfully implemented:

- **Graphical User Interface (GUI)**: Developed using Tkinter.
<br>

- **Account Management**:
    - `Register a New Account`: Users can create a new XMPP account on the server.
    - `Login with an Account`: Users can log in to their XMPP account.
    - `Logout`: Users can log out of their XMPP account.
    - `Delete Account`: Users can delete their XMPP account from the server.
<br>

- **Communication**:
    - `Display All Contacts and Their Status`: Users can view a list of all contacts and their current status.
    - `Add a User to Contacts`: Users can add new contacts to their roster.
    - `Display Contact Details`: Users can view details of individual contacts.
    - `Presence Message Definition`: Users can set and update their presence message.

### 2. Features Not Implemented
Due to time constraints and technical challenges, the following features were not implemented:

- One-on-One Communication with Any User/Contact
- Participation in Group Conversations
- Send/Receive Notifications
- Send/Receive Files

### 3. Challenges Encountered
Several challenges impacted the progress of the project:

#### a. Time Constraints: 
Working on my family business consumed nearly half of my day, and the challenge of balancing that with attending classes, studying, and completing assignments left me with limited time and energy. Despite these constraints, I remained committed and was able to make significant progress, successfully implementing key features.

#### b. Lack of Front-End Development Experience: 
Initially, with no prior experience in front-end development and not having taken the corresponding course in college, the learning curve was steep. However, I was able to overcome this challenge and successfully implement the GUI using Tkinter.

#### c. Complexities with Python and Asyncio: 
Managing asynchronous operations with Python, especially when integrating asyncio with other libraries like Tkinter, presented significant challenges, leading to issues such as process blocking and program freezes.

### 4. Lessons Learned
Key lessons learned during the project include:
- Managing the interaction between Slixmpp and Tkinter, both relying on asyncio, highlighted the need for alternative libraries or strategies to handle asynchronous tasks without causing process conflicts.
- Gained a deeper understanding of XMPP stanzas and services, particularly:
- Message Carbons (XEP-0280): Enables message synchronization across multiple clients.
- In-Band Registration (XEP-0077): Facilitates account registration directly through the XMPP server.
- Learned to manually create custom stanzas using Slixmpp’s ElementTree (ET), which was a valuable experience.