import sys
import json
import argparse

from snyk import SnykClient


def get_org_id(client, org_name):
    """Gets the organization ID."""

    organizations = client.organizations.all()

    for org in organizations:
        if org.name == org_name:
            return org.id

    return None


def get_dependencies(client, project):
    """Gets the project's dependencies."""

    # Get the project's dependencies.
    dependencies = project.dependencies.all()

    return dependencies


def generate_sbom(project_name, dependencies):
    """Generates a SBOM for the given dependencies."""

    # Create a SBOM object.
    sbom = {
        'project_name': project_name,
        'dependencies': []
    }

    # Add the dependencies to the SBOM.
    for dependency in dependencies:
        licenses = [{'license': l.license, 'id': l.id} for l in dependency.licenses]
        sbom['dependencies'].append({
            'name': dependency.name,
            'version': dependency.version,
            'type': dependency.type,
            'licenses': licenses
        })

    return sbom


def validate_json_file(filename):
    try:
        with open(filename, 'r') as f:
            json_data = json.load(f)
        print(f"JSON validation for {filename} succeeded.")
    except json.JSONDecodeError as e:
        print(f"JSON validation for {filename} failed. Error: {e}")


def main(api_key, org_name):
    """The main function."""

    client = SnykClient(api_key)

    org_id = get_org_id(client, org_name)
    if not org_id:
        print(f"Organization not found: {org_name}")
        return

    organization = client.organizations.get(org_id)
    projects = organization.projects.all()

    all_projects_sbom = []

    # Iterate through all projects in the Snyk org.
    for index, project in enumerate(projects, start=1):
        print(f"Processing Project # {index}/{len(projects)}: {project.name}")

        # Get the project's dependencies.
        dependencies = get_dependencies(client, project)

        # Generate the SBOM.
        project_sbom = generate_sbom(project.name, dependencies)
        all_projects_sbom.append(project_sbom)

    # Write the SBOM to a text file.
    with open('sbom.txt', 'w') as f:
        json.dump(all_projects_sbom, f, indent=2)

    validate_json_file('sbom.txt')




def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate SBOM for Snyk projects")
    parser.add_argument("api_key", type=str, help="Snyk API key")
    parser.add_argument("org_name", type=str, help="Snyk organization name")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    main(args.api_key, args.org_name)