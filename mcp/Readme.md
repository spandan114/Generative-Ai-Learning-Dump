### What the hack is mcp ?
You have multiple services
Your AI agent needs data from them
The agent should NOT access them directly
MCP sits in the middle, talks to services, structures the data, and hands it to the agent

![alt text](mcp.png)

#### MCP contains:

- Tools – executable actions (APIs, DB ops)
- Resources – readable data (files, tables, docs)
- Prompts – reusable prompt templates
- Sampling – control over how the model generates (temperature, max tokens, etc.) in simple terms the MCP server asks the MCP client to run a prompt on the model and return the generated output.
- Permissions – access control
- Schemas – strict input/output contracts

### To run use 
```
npm run inspect
```
this will give you a playable link where you can test tool, prompt, resource