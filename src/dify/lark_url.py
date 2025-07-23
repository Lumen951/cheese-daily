import json

def main(lark_url: str) -> dict:
    """
    从飞书提供的array[object] json数据中提取lark_url字段
    
    Args:
        lark_url: 包含飞书文档信息的JSON字符串或列表
        
    Returns:
        dict: 包含提取的lark_url信息
    """
    try:
        # 解析输入的JSON数据
        if isinstance(lark_url, str):
            data = json.loads(lark_url)
        else:
            data = lark_url
            
        # 处理不同的数据结构
        if isinstance(data, dict):
            # 如果是字典格式，提取lark_url数组
            lark_urls = data.get("lark_url", [])
        elif isinstance(data, list):
            # 如果直接是列表格式，直接使用
            lark_urls = data
        else:
            lark_urls = []
        
        # 提取每个文档的URL
        doc_urls = []
        for item in lark_urls:
            if isinstance(item, dict) and "url" in item:
                doc_urls.append(item["url"])
        
        # 如果有多个URL，用第一个，否则返回空字符串
        doc_url = doc_urls[0] if doc_urls else ""
        
        return {
            "lark_url": doc_url
        }
        
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        # 处理解析错误
        return {
            "lark_url": "error",
        }
