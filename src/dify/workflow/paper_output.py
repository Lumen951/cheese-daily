import json

def main(explained_paper: list, classified_category: list, paper_url: list, cheese_summary: str) -> dict:
    """
    按照顺序合并explained_paper和classified_paper
    第一篇与第一篇合并，第二篇与第二篇合并，以此类推
    """
    result = []
    
    # 获取两个列表的最小长度，确保不会出现索引越界
    min_length = min(len(explained_paper), len(classified_category))
    
    for i in range(min_length):
        # 创建合并的JSON节点
        merged_item = {
            "explained_content": explained_paper[i],
            "classified_category": classified_category[i],
            "paper_url":paper_url[i]
        }
        result.append(json.dumps(merged_item, ensure_ascii=False))
    
    # 将cheese_summary添加到result的最后
    result.append(cheese_summary)
    
    return {"paper_output": result}