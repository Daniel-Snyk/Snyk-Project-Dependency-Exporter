# **Snyk Project Dependencies Exporter**

This script fetches and generates a Software Bill of Materials (SBOM) for all the projects in a given Snyk organization, listing their dependencies in a single JSON file.

## **Requirements**

- Python 3.6 or higher
- Snyk API key with access to the organization you want to analyze

## **Installation**

1. Clone this repository or download the script.
2. Install the required Python packages using the following command:

```
pip install -r requirements.txt

```

## **Usage**

To use the script, you need to provide your Snyk API key and the name of the Snyk organization as command-line arguments.

Run the script as follows:

```
python snykgetalldepsfororg.py <API_KEY> <ORG_NAME>

```

Replace **`<API_KEY>`** with your Snyk API key and **`<ORG_NAME>`** with the name of the Snyk organization you want to analyze.

The script will generate an **`sbom.txt`** file containing the Software Bill of Materials for all the projects in the specified organization. The file will contain a JSON object for each project, with its name, dependencies, dependency versions, types, and licenses.

## **Example**

If your API key is **`abcd1234`** and the organization name is **`my-organization`**, run the script like this:

```
python snykgetalldepsfororg.py abcd1234 my-organization

```

After the script finishes, you'll find the generated **`sbom.txt`** file in the same directory.

## **Troubleshooting**

If you encounter any issues or errors, please make sure you are using the correct API key and organization name. If the problem persists, double-check the installed dependencies and the Python version.

## **License**

This project is released under the **[MIT License](https://opensource.org/licenses/MIT)**.
