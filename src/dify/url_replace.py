def main(input_dict: dict) -> dict:
    # 获取abstract_url列表
    urls = input_dict.get("abstract_url", [])
    # 替换每个url中的'abs'为'pdf'
    replaced_urls = [url.replace('/abs/', '/pdf/') for url in urls]
    # 返回新dict，包含replaced_url字段
    return {
        "replaced_url": replaced_urls
    }