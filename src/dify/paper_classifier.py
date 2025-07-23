import json

def main(explained_paper: list, classified_paper: list) -> dict:
    result = []
    for exp, cls in zip(explained_paper, classified_paper):
        # 去除代码块标记，提取纯 JSON
        exp_clean = exp.strip()
        if exp_clean.startswith("```json"):
            exp_clean = exp_clean[7:]
        if exp_clean.startswith("```"):
            exp_clean = exp_clean[3:]
        if exp_clean.endswith("```"):
            exp_clean = exp_clean[:-3]
        exp_clean = exp_clean.strip()
        # 解析 JSON
        try:
            exp_json = json.loads(exp_clean)
        except Exception as e:
            continue
        # 构造新的结构并转为字符串
        merged = {
            "paper_body": exp_json,
            "category": cls
        }
        result.append(json.dumps(merged, ensure_ascii=False))
    return {"result": result}