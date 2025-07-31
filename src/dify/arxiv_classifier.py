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
    
    # 替换每个url中的'abs'为'pdf'
    replaced_urls = [url.replace('/abs/', '/pdf/') for url in urls]
    
    return {
        "title": titles,
        "abstract": abstracts,
        "abstract_url": urls,
        "replaced_url": replaced_urls,
        "paper_count": len(titles)
    }