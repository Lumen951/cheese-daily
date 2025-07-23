import re
import json

def main(paper_info: str) -> dict:
    # 用正则分割每一组 { ... }
    paper_blocks = re.findall(r'\{.*?\}', paper_info, re.DOTALL)
    titles = []
    abstracts = []
    urls = []
    for block in paper_blocks:
        try:
            paper = json.loads(block)
            titles.append(paper.get("Title", ""))
            abstracts.append(paper.get("Abstract", ""))
            urls.append(paper.get("Abstract_URL", ""))
        except Exception as e:
            continue
    return {
        "title": titles,
        "abstract": abstracts,
        "abstract_url": urls,
        "paper_count": len(titles)
    }