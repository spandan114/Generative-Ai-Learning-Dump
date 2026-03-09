import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export function registerWeatherTool(server: McpServer) {
  server.registerTool(
    "get_weather",
    {
      description:
        "Get current weather information for a city (mock data for demo)",
      inputSchema: {
        city: z.string().describe("City name to get weather for"),
        units: z
          .enum(["metric", "imperial"])
          .optional()
          .describe("Temperature units (default: metric)"),
      },
    },
    async ({ city, units = "metric" }) => {
      // In a real implementation, you would call a weather API
      // For this example, we'll return mock data

      const mockWeatherData = {
        city: city,
        temperature: units === "metric" ? 22 : 72,
        unit: units === "metric" ? "°C" : "°F",
        condition: "Partly Cloudy",
        humidity: 65,
        wind_speed: units === "metric" ? 15 : 9.3,
        wind_unit: units === "metric" ? "km/h" : "mph",
      };

      const weatherReport = `
Weather for ${mockWeatherData.city}:
🌡️  Temperature: ${mockWeatherData.temperature}${mockWeatherData.unit}
☁️  Condition: ${mockWeatherData.condition}
💧 Humidity: ${mockWeatherData.humidity}%
💨 Wind: ${mockWeatherData.wind_speed} ${mockWeatherData.wind_unit}
      `.trim();

      return {
        content: [
          {
            type: "text" as const,
            text: weatherReport,
          },
        ],
      };
    },
  );
}

// Example of how to integrate a real API:
/*
import fetch from 'node-fetch';

export function registerWeatherTool(server: McpServer) {
  server.registerTool(
    "get_weather",
    {
      description: "Get current weather information for a city",
      inputSchema: {
        city: z.string().describe("City name to get weather for"),
        units: z.enum(["metric", "imperial"]).optional().describe("Temperature units (default: metric)"),
      },
    },
    async ({ city, units = "metric" }) => {
      try {
        const apiKey = process.env.WEATHER_API_KEY;
        const response = await fetch(
          `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=${units}&appid=${apiKey}`
        );
        
        if (!response.ok) {
          throw new Error(`Weather API error: ${response.statusText}`);
        }
        
        const data = await response.json();
        
        return {
          content: [
            {
              type: "text" as const,
              text: JSON.stringify(data, null, 2),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: "text" as const,
              text: `Error fetching weather: ${error.message}`,
            },
          ],
          isError: true,
        };
      }
    }
  );
}
*/

// Example of how to integrate a real API:
/*
import fetch from 'node-fetch';

export function registerWeatherTool(server: McpServer) {
  server.tool(
    "get_weather",
    "Get current weather information for a city",
    WeatherSchema,
    async ({ city, units = "metric" }) => {
      try {
        const apiKey = process.env.WEATHER_API_KEY;
        const response = await fetch(
          `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=${units}&appid=${apiKey}`
        );
        
        if (!response.ok) {
          throw new Error(`Weather API error: ${response.statusText}`);
        }
        
        const data = await response.json();
        
        return {
          content: [
            {
              type: "text" as const,
              text: JSON.stringify(data, null, 2),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: "text" as const,
              text: `Error fetching weather: ${error.message}`,
            },
          ],
          isError: true,
        };
      }
    }
  );
}
*/
