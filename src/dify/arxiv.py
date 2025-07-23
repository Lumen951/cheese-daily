import json
import pandas as pd
import io

def main(papers_data):
    """提取每篇论文的标题、摘要和链接地址"""
    # 获取文本内容
    text = papers_data.get("text", [""])[0]
    # 读取为DataFrame
    df = pd.read_csv(io.StringIO(text), sep='|', engine='python', skipinitialspace=True)
    # 去除空白列名
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # 去除首尾空白
    df.columns = df.columns.str.strip()
    # 提取需要的字段
    result = []
    for _, row in df.iterrows():
        title = str(row.get('Title', '')).strip()
        abstract = str(row.get('Abstract', '')).strip()
        url = str(row.get('Abstract_URL', '')).strip()
        if title and abstract and url:
            result.append({
                'title': title,
                'abstract': abstract,
                'url': url
            })
    return {"result": result}