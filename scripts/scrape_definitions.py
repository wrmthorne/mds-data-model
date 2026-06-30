import argparse
import json
import re
from pathlib import Path

import httpx
import lxml.html as html
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

BASE_URL = "https://collectionstrust.org.uk"
INDEX_URL = "https://collectionstrust.org.uk/spectrum/information-requirements/procedural-information-groups/"
HEADERS = {"User-Agent": "Mozilla/5.0 (research-scraper; spectrum-docs)"}

client = httpx.Client(timeout=30, follow_redirects=True, headers=HEADERS)


def is_retriable(exc: BaseException) -> bool:
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in (429, 500, 502, 503, 504)
    return isinstance(exc, (httpx.TimeoutException, httpx.ConnectError))


@retry(
    retry=retry_if_exception(is_retriable),
    wait=wait_exponential(multiplier=2, min=2, max=60),
    stop=stop_after_attempt(5),
)
def fetch(url: str) -> html.HtmlElement:
    r = client.get(url)
    r.raise_for_status()
    return html.fromstring(r.content)


def parse_unit_information(root):
    definition = root.xpath("//div[@id='unit-definition']")
    if definition:
        if _definition := definition[0].xpath("/p"):
            definition = _definition
        definition = definition[0].text_content().strip()
    else:
        definition = ""

    use = use[0].text_content().strip() if (use := root.xpath("//div[@id='unit-use']/p")) else ""

    return {
        "definition": definition,
        "how_to_record": root.xpath("//div[@id='unit-recording']/p")[0].text_content().strip(),
        "examples": [e.strip() for e in root.xpath("//div[@id='unit-examples']/p")[0].text_content().split("; ")],
        "use": use,
    }


def parse_li(li: html.HtmlElement, depth: int = 0) -> dict:
    anchor = (li.xpath("em/a") or li.xpath("a") or li.xpath("ul/li/em/a"))[0]
    name = anchor.text_content().lower().strip()
    name = re.sub(r"[^\w\s/]", "", name)
    name = re.sub(r"\s+|/", "_", name)
    unit_info = parse_unit_information(fetch(BASE_URL + anchor.get("href")))
    print(" " * (depth + 1) * 4 + f"Complete: {name}")
    for child_li in li.xpath("ul/li"):
        unit_info.update(parse_li(child_li, depth + 1))
    return {name: unit_info}


def parse_units(url: str) -> dict:
    root = fetch(url)
    unitlist = root.xpath("//div[@id='unitlist']/ul/li")
    if not unitlist:
        unitlist = root.xpath("//div[@id='resource_content']/ul/li")
        if not unitlist:
            unitlist = root.xpath("//div[@id='resource_content']/div/ul/li")
    return {k: v for li in unitlist for k, v in parse_li(li).items()}


def process_units_list(url: str, output_dir: Path):
    print(f"Processing {url}")
    output_filename = url.removesuffix("/").split("/")[-1]
    output_file = (output_dir / output_filename).with_suffix(".json")

    if output_file.exists():
        return

    parsed_units = parse_units(url)
    with open(output_file, "w") as f:
        json.dump(parsed_units, f, indent=4)


def main():
    parser = argparse.ArgumentParser("Scraper for spectrum documentation")
    parser.add_argument("--url", type=str, default=None, help="Target URL")
    args = parser.parse_args()

    output_dir = Path(__file__).parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not args.url:
        root = fetch(INDEX_URL)
        for link in root.xpath("//div[@class='further-description']//a/@href"):
            process_units_list(BASE_URL + link, output_dir)
    else:
        process_units_list(args.url, output_dir)


if __name__ == "__main__":
    main()
