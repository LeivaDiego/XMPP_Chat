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

# Project Report

## **1. Introduction**

The objective of this project was to implement an instant messaging client that supports the XMPP protocol, adhering to established standards. The project aimed to provide a deep understanding of the XMPP protocol, including how its services function, and to apply the knowledge acquired in network programming, along with best development practices.

The project was expected to implement key features such as account management, one-on-one communication, group chats, file transfers, and notifications, all within a graphical user interface (GUI).

## **2. Project Objectives**

- **Implement a Protocol Based on Standards:** The project aimed to develop an XMPP client that complies with established standards.
- **Understand the Purpose of the XMPP Protocol:** A key goal was to gain a comprehensive understanding of XMPP's purpose and functionality.
- **Learn How XMPP Services Work:** The project included learning about the various services provided by XMPP and how to use them effectively.
- **Apply Knowledge in Web and Mobile Programming:** The project sought to leverage skills from Web and Mobile programming, adhering to proper development practices.

## **3. Implemented Features**

As of now, the following features have been implemented:

- **Account Management:**
  - **Register a New Account:** Users can create a new XMPP account on the server.
  - **Login with an Account:** Users can log in to their XMPP account.
  - **Logout of an Account:** Users can log out of their XMPP account.
  - **Delete Account from the Server:** Users can delete their XMPP account.

- **Communication:**
  - **Message Receiver:** The client can receive messages from other users.
  - **Echo Bot:** An echo bot has been implemented, which replies to incoming messages with the same content.

**Important:** There's no GUI, this code is for console only.

## **4. Features Not Implemented**

Unfortunately, due to time constraints and technical challenges, several key features were not implemented:

- **Show All Users/Contacts and Their Status**
- **Add a User to Contacts**
- **Show Contact Details**
- **One-on-One Communication with Any User/Contact**
- **Participate in Group Conversations**
- **Define Presence Message**
- **Send/Receive Notifications**
- **Send/Receive Files**

## **5. Difficulties Encountered**

Several challenges impacted the progress of the project:

- **Time Constraints:** Supporting my family business left me with very little time to work on the project. Balancing these responsibilities significantly reduced the time available for coding and learning new concepts.
- **Lack of Front-End Development Experience:** I had no prior experience with front-end development as I have not yet taken the corresponding course in college. The steep learning curve, combined with my limited time, made it difficult to acquire the necessary skills within the project's timeframe.
- **Challenges with Python and Asyncio:** Using Python, particularly with the asyncio library, proved to be a challenging choice. The complexities of managing asynchronous operations, especially when combined with other libraries like Tkinter, led to significant issues such as process blocking and program freezes.

## **6. Lessons Learned**

Throughout the project, several important lessons were learned:

- **Asyncio and Tkinter Compatibility Issues:** Slixmpp and Tkinter both rely on asyncio, which caused them to block each other's processes, leading to program freezes. This highlighted the need for alternative libraries or strategies to manage asynchronous tasks effectively.
- **Understanding XMPP Stanzas and Services:** I gained a deeper understanding of XMPP stanzas and how various services work. Specifically, I worked with:
  - **Message Carbons (XEP-0280):** This service enables message synchronization across multiple clients.
  - **In-Band Registration (XEP-0077):** This service facilitates account registration directly through the XMPP server.


## **7. Setup and Installation**

### **7.1. Prerequisites**

Before setting up the project, ensure you have the following installed on your system:

- **Conda:** A package, dependency, and environment management system.
- **Python 3.8+**

### **7.2. Setting Up the Environment**

To set up the environment for this project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/LeivaDiego/XMPP_Chat.git

2. **Create a Conda Environment:**

You can create a new Conda environment using the provided environment.yml file:

    conda env create -f environment.yml

This command will create a new Conda environment with all the necessary dependencies.

1. **Activate the Conda Environment:**

    ```bash
    conda activate your-environment-name

4. **Running the Application**
After setting up the environment, you can run the application:

    ```bash
    python main.py

This will start the XMPP client, and you will be prompted with the initial menu to log in, register, or exit.

5. **Dependencies**
The project uses the following dependencies, which are specified in the environment.yml file:

```yaml
    name: xmpp-client-env
    channels:
    - defaults
    dependencies:
    - python=3.8
    - slixmpp
    - pyqt=5
```

8. **Key Libraries**
- slixmpp: The core library used to implement the XMPP protocol.
- Asyncio: For managing asynchronous tasks within the application.
