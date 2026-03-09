import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export function registerCalculatorTool(server: McpServer) {
  server.registerTool(
    "calculator",
    {
      description: "Performs basic arithmetic operations",
      inputSchema: {
        operation: z.enum(["add", "subtract", "multiply", "divide"]).describe("The operation to perform"),
        a: z.number().describe("First number"),
        b: z.number().describe("Second number"),
      },
    },
    async ({ operation, a, b }) => {
      let result: number;
      
      switch (operation) {
        case "add":
          result = a + b;
          break;
        case "subtract":
          result = a - b;
          break;
        case "multiply":
          result = a * b;
          break;
        case "divide":
          if (b === 0) {
            return {
              content: [
                {
                  type: "text" as const,
                  text: "Error: Division by zero",
                },
              ],
              isError: true,
            };
          }
          result = a / b;
          break;
      }
      
      return {
        content: [
          {
            type: "text" as const,
            text: `${a} ${operation} ${b} = ${result}`,
          },
        ],
      };
    }
  );
}