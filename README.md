# URL Endpoints Fetcher

This Python script, `endpoints.py`, fetches and parses the content of a given URL for all embedded links, returning a comprehensive list of absolute URLs. It's particularly useful for web developers, security researchers, and SEO specialists for collecting and analyzing webpage endpoints. Additionally, the script saves these URLs into a JSON file, named after the base URL's hostname, facilitating further analysis or record-keeping.

## Features

- **Link Extraction:** Fetches all links from the specified URL and converts them into absolute URLs.
- **Data Storage:** Organizes and saves the collected URLs into a JSON file for easy access and analysis.

## Installation Requirements

Before using the script, ensure you have Python 3.x installed on your system. You will also need to install the `requests` and `beautifulsoup4` libraries. These can be installed using pip, Python's package installer, as follows:

```bash
pip install requests beautifulsoup4
```

## How to Use

1. **Clone the Repository:** Start by cloning this repository to your local machine.
2. **Navigate to the Directory:** Open your terminal/command prompt, and navigate to the directory where you have cloned the repository.
3. **Run the Script:** Execute the script by running the following command in your terminal:

```bash
python endpoints.py
```

4. **Enter a URL:** When prompted, input the URL you wish to fetch endpoints from. The script will then process the URL, display the fetched URLs in the terminal, and save them to a JSON file in the same directory.

# Donation

Your support is appreciated:

- USDt (TRC20): `TGCVbSSJbwL5nyXqMuKY839LJ5q5ygn2uS`
- BTC: `13GS1ixn2uQAmFQkte6qA5p1MQtMXre6MT`
- ETH (ERC20): `0xdbc7a7dafbb333773a5866ccf7a74da15ee654cc`
- LTC: `Ldb6SDxUMEdYQQfRhSA3zi4dCUtfUdsPou`

## Contributing

We welcome contributions from the community! If you'd like to improve the `endpoints.py` script, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.