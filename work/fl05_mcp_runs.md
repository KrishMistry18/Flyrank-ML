# MCP Task Runs: Stitch UI Integration

*Below is the record of three tasks executed via the local `stitch` MCP server. These tasks demonstrate the AI assistant interacting with local workspace data through standardized MCP tool calls.*

## Task 1: Discovering Projects

**Request:** "Use the stitch MCP server to list all the UI projects I currently own in my workspace."
**MCP tool selected:** `list_projects` (from stitch server)
**Input arguments:** `{"filter": "view=owned"}`
**Tool output (abridged):** 
```json
{
  "projects": [
    {"name": "projects/2131883050067840857", "title": "EduCycle Design System"},
    {"name": "projects/6077728060193222897", "title": "AyurWell Premium Wellness Suite"},
    {"name": "projects/66121008557031477", "title": "PriceRadar: Full-Stack Price Comparison App"},
    {"name": "projects/4491010001425905043", "title": "Neighbourhood Hub Civic UI System"}
  ]
}
```
**Assistant result:** The assistant successfully reported that I have four owned projects: EduCycle, AyurWell, PriceRadar, and Neighbourhood Hub.
**Why ordinary chat alone isn't equivalent:** A standard LLM without MCP has no access to my private local environment or my IDE's active UI workspace. It could only guess or hallucinate project names, whereas the MCP connection allowed it to dynamically query the live local database via the `stitch` server tool.

## Task 2: Inspecting Project Screens

**Request:** "For the 'PriceRadar' project (ID: 66121008557031477), list all the associated screens."
**MCP tool selected:** `list_screens` (from stitch server)
**Input arguments:** `{"projectId": "66121008557031477"}`
**Tool output (abridged):**
```json
{
  "screens": [
    {"id": "4dd7d1fada264d24a9ae9ecfece79483", "width": 390, "height": 884},
    {"id": "7bd86ad9e0a648aeaef665a2bf965425", "width": 390, "height": 4399},
    {"id": "d85206f59be84fe7bbfe626572e9ee24", "width": 390, "height": 3156}
  ]
}
```
**Assistant result:** The assistant reported the screen IDs and confirmed that they are mobile-optimized screens, given the narrow width of 390px.
**Why ordinary chat alone isn't equivalent:** The assistant took an ID from the previous tool call, executed a second, more specific tool call, and extracted structural data about my private UI screens, which is entirely invisible to the public internet.

## Task 3: Extracting Design Metadata

**Request:** "Fetch the full project details for PriceRadar and tell me what its primary and secondary colors are, as well as the main headline font."
**MCP tool selected:** `get_project` (from stitch server)
**Input arguments:** `{"name": "projects/66121008557031477"}`
**Tool output (abridged):**
```json
{
  "designTheme": {
    "colorMode": "LIGHT",
    "customColor": "#6750A4",
    "namedColors": {
      "primary": "#4f378a",
      "secondary": "#63597c"
    }
  },
  "designMd": "typography:\n  display:\n    fontFamily: Syne\n    fontSize: 42px..."
}
```
**Assistant result:** The assistant extracted the specific design tokens: Primary Color (`#4f378a`), Secondary Color (`#63597c`), and Headline Font (`Syne`).
**Why ordinary chat alone isn't equivalent:** The assistant reached into a complex JSON object returned by the local server and parsed out my highly specific, custom-defined design system tokens. An ordinary chat model would just output generic hex codes.
