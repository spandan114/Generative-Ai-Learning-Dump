import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export function registerEchoTool(server: McpServer) {
  server.registerTool(
    "echo",
    {
      description: "Echoes back the provided message, optionally repeating it",
      inputSchema: {
        message: z.string().describe("The message to echo back"),
        repeat: z.number().optional().describe("Number of times to repeat (default: 1)"),
      },
    },
    async ({ message, repeat = 1 }) => {
      const result = Array(repeat).fill(message).join("\n");
      
      return {
        content: [
          {
            type: "text" as const,
            text: result,
          },
        ],
      };
    }
  );
}