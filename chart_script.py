# Create mermaid flowchart for GitHub Pages setup process
diagram_code = """
flowchart TD
    A[Start Setup] --> B{Choose Repo Type}
    B -->|User Site| C[Create username<br/>.github.io]
    B -->|Project Site| D[Create project<br/>repo]
    C --> E[Set Public &<br/>Create]
    D --> E
    E --> F[Upload Files:<br/>index.html<br/>style.css<br/>README.md]
    F --> G[Settings → Pages<br/>Deploy from<br/>main branch]
    G --> H[Wait Deploy<br/>5-10 min]
    H --> I[Access Live<br/>Site]
"""

# Create the flowchart using the helper function
create_mermaid_diagram(diagram_code, 'github_pages_flowchart.png', 'github_pages_flowchart.svg')