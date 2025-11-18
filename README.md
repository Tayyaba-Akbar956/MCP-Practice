# MCP Practice Repository

A comprehensive learning project for understanding Model Context Protocol (MCP) implementation using FastMCP and JSON-RPC 2.0. This repository demonstrates server-client communication, error handling, and protocol compliance testing.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## 🎯 Overview

This project implements a simple MCP server with a division tool and includes comprehensive testing for:
- Valid JSON-RPC 2.0 requests
- Error handling and validation
- Protocol compliance
- HTTP and JSON response analysis

## 📁 Project Structure
```
MCP PRACTICE/
├── main.py              # FastMCP server implementation
├── client.py            # Python client for testing server endpoints
├── instructions.md      # Detailed testing instructions
├── questions.md         # Learning questions and concepts
└── responses.md         # Expected responses for each request
```

## ✨ Features

- **FastMCP Server**: Stateless HTTP-based MCP server
- **Division Tool**: Simple mathematical operation exposed via MCP
- **Comprehensive Testing**: 11+ test cases covering various scenarios
- **Error Validation**: Tests for malformed requests and edge cases
- **Dual Testing Methods**: Support for both Python client and Postman

## 🔧 Prerequisites

- Python 3.8+
- `uv` package manager
- Postman (optional, for manual testing)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Tayyaba-Akbar956/MCP-Practice.git
cd "MCP PRACTICE"
```

2. Install dependencies:
```bash
uv pip install fastmcp requests uvicorn
```

## 🚀 Usage

### Starting the Server

Run the MCP server using uvicorn:
```bash
uv run uvicorn main:app --reload
```

The server will start at `http://localhost:8000/mcp/`

### Running the Client

Execute the test client:
```bash
uv run client.py
```

## 🧪 Testing

### Method 1: Using Python Client (client.py)

The client tests the following scenarios:

#### ✅ Valid Requests
1. **Tools List**: Lists all available tools
2. **Division Operation**: Performs valid division (10 ÷ 2)

#### ❌ Error Cases
3. **Missing `jsonrpc` field**: Tests protocol validation
4. **Wrong JSON-RPC version**: Tests version compatibility (1.0 instead of 2.0)
5. **Missing `id` field**: Tests required field validation
6. **Invalid method name**: Tests method existence (`tools/unknown_method`)
7. **Missing `params` field**: Tests parameter requirement
8. **Missing `name` in params**: Tests tool name requirement
9. **Missing `arguments` in params**: Tests argument requirement
10. **Wrong tool name**: Tests tool existence (`Add` instead of `Divide`)
11. **Division by zero**: Tests error handling (10 ÷ 0)

**Best Practice**: Test one scenario at a time by uncommenting the specific test case.

### Method 2: Using Postman

1. **Setup Request**:
   - Method: `POST`
   - URL: `http://localhost:8000/mcp/`

2. **Configure Headers**:
```
   Key: Accept
   Value: application/json,text/event-stream
```

3. **Send Request Body** (example):
```json
   {
       "jsonrpc": "2.0",
       "method": "tools/call",
       "id": 2,
       "params": {
           "name": "Divide",
           "arguments": {
               "a": 10,
               "b": 2
           }
       }
   }
```



## 📝 Notes

- Always run the server before executing client tests
- Test one scenario at a time for clear output analysis
- Review `responses.md` for expected responses for each request
- Check `instructions.md` for detailed testing steps

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Learning! 🚀**
