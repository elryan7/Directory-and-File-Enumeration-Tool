# Directory and File Enumeration Tool
*Author*: elryan7  
*Repository*: https://github.com/elryan7/dir-file-enumerator  
*License*: MIT  

## Description
This Python tool performs directory and file enumeration on a web server using a wordlist. It supports multithreading for speed and customizable wordlists for targeted enumeration.

## Features
- Discovers hidden directories and files
- Multithreaded HTTP requests
- Customizable wordlists
- Detailed reporting of findings

## Prerequisites
- Python 3.8+
- Libraries: `requests`, `concurrent.futures`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/elryan7/dir-file-enumerator.git
   cd dir-file-enumerator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the enumerator with:
```bash
python3 dir_enumerator.py http://example.com wordlist.txt
```
- Results are saved to `enum_report.txt`.

## Example Output
```
URL: http://example.com/admin
Status: 200 OK
URL: http://example.com/backup.zip
Status: 200 OK
```

## Project Structure
- `dir_enumerator.py`: Main script for enumeration
- `wordlist.txt`: Sample wordlist for enumeration
- `requirements.txt`: List of required Python libraries
- `enum_report.txt`: Output report file
