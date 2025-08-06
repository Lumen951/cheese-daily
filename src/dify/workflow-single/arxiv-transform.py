
def main(arxiv_abs_url: str) -> dict:
    # 替换每个url中的'abs'为'pdf'
    replaced_urls = arxiv_abs_url.replace('/abs/', '/pdf/')
    
    return {
        "pdf_url": replaced_urls
    }