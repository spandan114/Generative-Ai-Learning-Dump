import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export function registerSummaryPrompt(server: McpServer) {
  server.registerPrompt(
    "summarize",
    {
      description: "Generate a concise summary of the provided text",
      argsSchema: {
        text: z.string().describe("The text to summarize"),
        max_length: z.number().optional().describe("Maximum length of summary in words"),
      },
    },
    async ({ text, max_length = 100 }) => {
      return {
        messages: [
          {
            role: "user" as const,
            content: {
              type: "text" as const,
              text: `Please provide a concise summary of the following text in no more than ${max_length} words:\n\n${text}`,
            },
          },
        ],
      };
    }
  );
}