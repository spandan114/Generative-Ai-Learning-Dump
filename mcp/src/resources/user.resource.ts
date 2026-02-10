import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

// Mock user data
const users: User[] = [
  { id: 1, name: "Alice Johnson", email: "alice@example.com", role: "Admin" },
  { id: 2, name: "Bob Smith", email: "bob@example.com", role: "User" },
  { id: 3, name: "Charlie Brown", email: "charlie@example.com", role: "User" },
];

export function registerUserResource(server: McpServer) {
  // List all users - static resource
  server.registerResource(
    "All Users",
    "users://all",
    {
      description: "List of all users in the system",
      mimeType: "application/json",
    },
    async () => {
      return {
        contents: [
          {
            uri: "users://all",
            mimeType: "application/json",
            text: JSON.stringify(users, null, 2),
          },
        ],
      };
    }
  );

  // Get individual user by ID - template resource
  server.registerResource(
    "User by ID",
    new ResourceTemplate("users://{id}", {
      list: undefined, // No listing callback needed
    }),
    {
      description: "Get a specific user by ID",
      mimeType: "application/json",
    },
    async (uri, variables) => {
      const userId = parseInt(Array.isArray(variables.id) ? variables.id[0] : variables.id);
      const user = users.find((u) => u.id === userId);

      if (!user) {
        throw new Error(`User with ID ${userId} not found`);
      }

      return {
        contents: [
          {
            uri: uri.href,
            mimeType: "application/json",
            text: JSON.stringify(user, null, 2),
          },
        ],
      };
    }
  );
}