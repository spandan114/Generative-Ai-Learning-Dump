import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

// Import all components
import { registerEchoTool } from "./tools/echo.tool.ts";
import { registerCalculatorTool } from "./tools/calculator.tool.ts";
import { registerWeatherTool } from "./tools/weather.tool.ts";
import { registerUserResource } from "./resources/user.resource.ts";
import { registerProjectResource } from "./resources/project.resource.ts";
import { registerSummaryPrompt } from "./prompts/summary.prompt.ts";
import { registerSampling } from "./sampling/enrich.sampling.ts";

async function main() {
  const server = new McpServer({
    name: "example-mcp-server",
    version: "0.1.0",
  });

  console.error("Registering MCP server components...");

  // Register tools
  registerEchoTool(server);
  registerCalculatorTool(server);
  registerWeatherTool(server);
  console.error("✓ Tools registered (echo, calculator, get_weather)");

  // Register resources
  registerUserResource(server);
  registerProjectResource(server);
  console.error("✓ Resources registered (users, projects)");

  // Register prompts
  registerSummaryPrompt(server);
  console.error("✓ Prompts registered (summarize)");

  // Register sampling (informational only)
  registerSampling(server);
  console.error("✓ Sampling configuration noted");

  // Connect to transport
  const transport = new StdioServerTransport();
  await server.connect(transport);
  
  console.error("MCP Server running on stdio");
  console.error("Ready to accept requests from MCP clients");
}

main().catch((error) => {
  console.error("Fatal error in main():", error);
  process.exit(1);
});