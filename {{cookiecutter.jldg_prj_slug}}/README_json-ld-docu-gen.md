# json-ld-docu-gen

**Automated Documentation Generation from JSON-LD Data**

A powerful toolkit for enterprises to automatically generate comprehensive documentation from JSON-LD instance data. Visualize complex organizational data flows, technical system topologies, and process swimlanes through semantic linked data.

---

## Introduction

In modern organizations, data flows across multiple departments, systems, and technical landscapes. Understanding these complex relationships requires more than static diagrams—it requires **dynamic documentation** generated directly from authoritative data sources.

**json-ld-docu-gen** bridges this gap by transforming JSON-LD microservice instances into comprehensive, professionally formatted documentation. Whether you're documenting:

- **Organizational structures** (units, functions, products)
- **System landscapes** (technical topology and dependencies)
- **Process flows** (swimlane diagrams with data movement)
- **Product catalogs** (instances linked to abstract functions)

...this toolkit generates **reusable, maintainable, and versioned documentation** automatically.

### Key Benefits

- **Single Source of Truth**: Documentation generated from live JSON-LD data
- **Multi-Format Output**: HTML, PDF, and interactive documentation
- **Enterprise-Ready**: Customizable branding, styling, and layouts
- **Semantic Integration**: Full support for RDF reasoning and SPARQL queries
- **DevOps-Native**: Containerized, CI/CD-ready, Sphinx-based workflow

---

## Methods & Concepts

### Core Architecture

The toolkit is built on a **model-driven approach**, where JSON-LD data is parsed into domain objects that represent real-world entities:

#### 1. **Base Model Layer** (`model.base.Base`)
- Loads JSON-LD documents from REST microservices or local files
- Compacts JSON-LD using PyLD for consistency
- Builds RDF graphs using rdflib for semantic querying
- Provides SPARQL query interface for data extraction

```
┌─────────────────────┐
│   JSON-LD Source    │  (REST API / File)
│ (Microservice URI)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   PyLD Processor    │  (Compact & Validate)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   RDF Graph (rdflib)│ (SPARQL Queryable)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Domain Objects     │  (Product, Function, Process, etc.)
└─────────────────────┘
```


#### 2. **Domain Models**

- **`Product`**: Concrete instances (physical/virtual) that realize Functions
  - Properties: name, description, tags, serial numbers
  - Relationship: N Products implement 1-n Functions

- **`Function`**: Abstract value propositions (what you can buy/license)
  - Properties: capabilities, value description
  - Relationship: Functions can be realized by multiple Products

- **`Process`**: Business processes with data transformations
  - Swimlane-based visualization
  - Tracks data movement across organizational units

- **`OrgUnit`**: Organizational structure (departments, teams)
  - Hierarchical relationships
  - Ownership of Functions and Processes

- **`SysLandscape`**: Technical system topology
  - System components and dependencies
  - Integration points and data flows

- **`ProcData`**: Process data objects (what flows through processes)

#### 3. **Generator Layer**

- **PlantUML Generation** (`generator.puml.*`)
  - Converts domain models → PlantUML diagrams
  - Supports class diagrams, sequence diagrams, swimlanes
  - Generates SVG/PNG output

- **Sphinx Integration**
  - reStructuredText source files
  - HTML/PDF generation with enterprise styling
  - PlantUML rendering during build

#### 4. **Utilities**

- **Global Logger Manager**: Centralized, structured logging across all modules
- **Namespace Management** (`puml_namespaces.py`): Consistent identifier generation

### Key Concepts

**Semantic Linked Data**
All models leverage @context definitions and namespace URIs for unambiguous data representation. SPARQL queries extract specific properties from RDF graphs.

**Generate-Once, Use-Everywhere**
A single JSON-LD source generates multiple output formats (HTML, PDF, diagrams) through Sphinx pipeline.

**Topology-Driven Documentation**
Document organizational structure first (Topo), then visualize how work flows through it (Swimlanes).

---

## Project Structure

```
json-ld-docu-gen/
│
├── src/                          # Python source code
│   ├── model/                    # Domain object definitions
│   │   ├── base.py              # Base class (JSON-LD → RDF)
│   │   ├── product.py           # Product instances
│   │   ├── function.py          # Abstract functions
│   │   ├── process.py           # Processes & swimlanes
│   │   ├── org_unit.py          # Organizational units
│   │   ├── sys_landscape.py     # System topology
│   │   └── procdata.py          # Process data objects
│   │
│   ├── generator/               # Documentation generators
│   │   └── puml/               # PlantUML diagram generation
│   │
│   ├── simulator/              # Test data simulators
│   ├── utilities/              # Logging, helpers
│   ├── topo.py                 # Topology main module
│   ├── swimlanes.py            # Swimlane main module
│   └── puml_namespaces.py      # URI/ID namespace management
│
├── conf/                        # Sphinx configurations
│   ├── base.py                 # Base Sphinx config
│   └── acme.py                 # Example: ACME branding
│
├── rst/                         # reStructuredText documentation sources
│   ├── intro_topo_*.rst        # Topology documentation
│   └── intro_swim_*.rst        # Swimlane documentation
│
├── json-ld/                     # JSON-LD data files
│
├── puml/                        # Hand-written PlantUML diagrams
├── puml_generated/              # Auto-generated PlantUML output
│
├── conf.py                      # Main Sphinx configuration
├── index.rst                    # Documentation index
├── Makefile                     # Build automation
├── make_all.sh                  # Multi-format build script
├── docker-compose.yml           # Docker service setup (Nginx + docs)
├── default.conf                 # Nginx configuration
│
├── README.md                    # This file
├── LICENSE                      # BSD-3-Clause license
└── CONTRIBUTING.md              # Contribution guidelines
```

### Build & Deployment

**Local Development**
```bash
# Python environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generate documentation
make clean html pdf
```

**Docker Deployment**
```bash
docker-compose up -d
# Access: http://localhost:8880
```

The `docker-compose.yml` serves generated HTML documentation via Nginx at `data.amp.net:8880`.

### License

This project is licensed under the **BSD-3-Clause License**.

See [LICENSE](./LICENSE) file for full text.

**In summary:**
- ✅ You may use this software for any purpose (commercial, personal, research)
- ✅ You may modify and distribute it
- ✅ You must include the license text and copyright notice
- ✅ You must list significant changes
- ❌ There is NO WARRANTY - use at your own risk
- ❌ The author/contributors cannot be held liable

---

## Conclusion & Future Outlook

**json-ld-docu-gen** transforms how organizations manage technical documentation. By anchoring documentation in authoritative JSON-LD data sources, teams achieve:

- **Currency**: Documentation updates when data changes
- **Consistency**: Single source eliminates conflicting versions
- **Clarity**: Topology + swimlane visualizations explain complex flows
- **Compliance**: Audit trails and versioning built-in via Git/Sphinx

### Potential Enhancements

🔮 **Version 2.0 Roadmap**

1. **Interactive Web UI**
   - Real-time diagram filtering
   - Search across topology and swimlanes
   - Drill-down from Products → Functions → Processes

2. **Advanced Querying**
   - SPARQL endpoint for external queries
   - Export diagrams as editable PlantUML
   - Custom report generation

3. **Collaboration Features**
   - Annotation system for diagrams
   - Change tracking and diff visualization
   - Role-based documentation views

4. **Extended Integrations**
   - BPMN 2.0 process modeling
   - ArchiMate enterprise architecture format
   - API documentation auto-generation (OpenAPI)

5. **Performance Optimization**
   - Caching for large RDF graphs
   - Incremental builds
   - GraphQL API layer

### Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

---

**json-ld-docu-gen** — *Where data meets documentation.*
