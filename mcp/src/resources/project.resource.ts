import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";

interface Project {
  id: string;
  name: string;
  status: "active" | "completed" | "on-hold";
  team: string[];
  deadline: string;
}

// Mock project data
const projects: Project[] = [
  {
    id: "proj-001",
    name: "Website Redesign",
    status: "active",
    team: ["Alice", "Bob"],
    deadline: "2026-03-15",
  },
  {
    id: "proj-002",
    name: "Mobile App Development",
    status: "active",
    team: ["Charlie", "Diana"],
    deadline: "2026-04-30",
  },
  {
    id: "proj-003",
    name: "API Migration",
    status: "completed",
    team: ["Alice", "Charlie"],
    deadline: "2026-01-20",
  },
];

export function registerProjectResource(server: McpServer) {
  // List all projects - static resource
  server.registerResource(
    "All Projects",
    "projects://all",
    {
      description: "List of all projects",
      mimeType: "application/json",
    },
    async () => {
      return {
        contents: [
          {
            uri: "projects://all",
            mimeType: "application/json",
            text: JSON.stringify(projects, null, 2),
          },
        ],
      };
    }
  );

  // Get projects by status - template resource
  server.registerResource(
    "Projects by Status",
    new ResourceTemplate("projects://status/{status}", {
      list: undefined,
    }),
    {
      description: "Get projects filtered by status (active, completed, on-hold)",
      mimeType: "application/json",
    },
    async (uri, variables) => {
      const status = variables.status as Project["status"];
      const filteredProjects = projects.filter((p) => p.status === status);

      return {
        contents: [
          {
            uri: uri.href,
            mimeType: "application/json",
            text: JSON.stringify(filteredProjects, null, 2),
          },
        ],
      };
    }
  );

  // Get project by ID - template resource
  server.registerResource(
    "Project by ID",
    new ResourceTemplate("projects://{id}", {
      list: undefined,
    }),
    {
      description: "Get a specific project by ID",
      mimeType: "application/json",
    },
    async (uri, variables) => {
      const projectId = variables.id;
      const project = projects.find((p) => p.id === projectId);

      if (!project) {
        throw new Error(`Project with ID ${projectId} not found`);
      }

      return {
        contents: [
          {
            uri: uri.href,
            mimeType: "application/json",
            text: JSON.stringify(project, null, 2),
          },
        ],
      };
    }
  );

  // Get team members for a project - template resource
  server.registerResource(
    "Project Team",
    new ResourceTemplate("projects://{id}/team", {
      list: undefined,
    }),
    {
      description: "Get team members for a specific project",
      mimeType: "application/json",
    },
    async (uri, variables) => {
      const projectId = variables.id;
      const project = projects.find((p) => p.id === projectId);

      if (!project) {
        throw new Error(`Project with ID ${projectId} not found`);
      }

      return {
        contents: [
          {
            uri: uri.href,
            mimeType: "application/json",
            text: JSON.stringify(
              {
                project_id: project.id,
                project_name: project.name,
                team: project.team,
              },
              null,
              2
            ),
          },
        ],
      };
    }
  );
}