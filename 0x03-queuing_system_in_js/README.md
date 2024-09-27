# Redis and Queueing System with Node.js

## Project Overview

This project is focused on using Redis and a queuing system with Node.js. It covers setting up a Redis server, performing basic operations using the Redis client, and integrating Redis with a Node.js application. The project also introduces the usage of Kue as a queue system and how to build a basic Express app that interacts with Redis.

## Learning Objectives

By the end of this project, you will be able to:

- Run a Redis server locally on your machine.
- Perform simple Redis operations (such as setting and getting values) using the Redis client.
- Use a Redis client with Node.js to execute basic operations.
- Store and manage hash values in Redis.
- Handle asynchronous operations using Redis.
- Implement Kue as a queue system for handling background jobs.
- Build a basic Express app that interacts with a Redis server.
- Extend the Express app to interact with both a Redis server and a queue system.

## Requirements

- Your code will be compiled/interpreted on **Ubuntu 18.04**, using **Node.js 12.x**, and **Redis 5.0.7**.
- Ensure all files end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Use the `.js` file extension for all JavaScript files.

## Required Files

- **`package.json`**: Contains project metadata and dependencies. Make sure to run `$ npm install` to install the required dependencies.
- **`.babelrc`**: Configuration file for Babel, a JavaScript compiler.

## How to Run

1. **Install Dependencies**:
   Run the following command to install the necessary packages as specified in `package.json`:
   ```bash
   npm install
   ```

2. **Run Redis Server**:
   Start the Redis server by running:
   ```bash
   redis-server &
   ```

3. **Perform Redis Operations**:
   Use the Redis client interface to perform basic operations:
   ```bash
   redis-cli
   ```

4. **Build Express App**:
   Build and run a basic Express app that interacts with Redis for queue management and data storage.

## Additional Resources

- [Redis Quick Start](https://redis.io/topics/quickstart)
- [Redis Client Interface](https://redis.io/commands)
- [Redis Client for Node.js](https://github.com/NodeRedis/node-redis)
- [Kue (Deprecated but still used)](https://github.com/Automattic/kue)

## Notes

- Ensure you are using **Node.js 12.x** and **Redis 5.0.7** for compatibility with this project.
- Follow the instructions provided in the resources for a deeper understanding of Redis and queuing systems in Node.js.
