"""CLI: python screen.py --resume resume.pdf --jd job.txt"""
import argparse, json
from pathlib import Path
from src.pdf_extractor import extract_text
from src.jd_parser import parse_jd
from src.matcher import match

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", required=True)
    parser.add_argument("--jd", required=True)
    args = parser.parse_args()

    resume_text = extract_text(args.resume)
    jd_text = Path(args.jd).read_text(encoding="utf-8")

    print("Parsing job description...")
    requirements = parse_jd(jd_text)

    print("Matching resume...")
    result = match(resume_text, requirements)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
