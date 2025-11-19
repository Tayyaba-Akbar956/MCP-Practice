1. What is the main purpose of the “2xx” class of status codes? How does 200 OK differ from 201 Created?

2. When are “3xx” redirection codes used, and what is the difference between 301 Moved Permanently and 302 Found?

3. What defines a “4xx” class error, and how is it different from a “5xx” class error?

4. What do “5xx” status codes represent?

5. If an API frequently returns 429 Too Many Requests, what does it mean, and how should clients respond?6. In REST API design, what are the best practices for assigning and evaluating HTTP status codes?

6. Discuss two major performance limitations of HTTP/1.1 (specifically concerning TCP connection usage), and explain how HTTP/2 addresses both of these issues through features like multiplexing and header compression.

7. Describe the performance function of the Connection: keep-alive header in HTTP/1.1.

8. what is the common factos in all HTTP versions (0.9 to 3)?

9. What is meant by context in terms of MCP?

10. If you get  200 HTTP code but error in jsonrpc, what could be the possible reason?

11. What problem does the Model Context Protocol (MCP) solve in AI applications?

12. How does MCP differ from traditional REST APIs when connecting AI models to external data sources?

13. Explain the client-server architecture in MCP. Which component is the AI model, and which provides the data?

14. What are the three main primitives (building blocks) that MCP uses to enable AI-data integration?

15. What is a "tool" in the context of MCP, and how does it differ from a traditional function call?

16. How does an MCP server expose tools to AI clients? What information must be provided?

17. Explain the concept of tool "discovery" in MCP. How does the client know what tools are available?

18. How does resource URI structure work in MCP? What makes a good resource identifier?

19. Explain the concept of resource "templates" in MCP. Why are they useful?

20. When would you expose data as a resource versus creating a tool to fetch that data?

